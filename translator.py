import cpp_vams_library as lb
import cpp_vams_parser as p

import sys, getopt, os.path

# Driver prototype for C++/Verilog translator

Cpp_to_Verilog = { #contains mappings of both Verilog-C++ and C++-Verilog data types
    "string":"string",
    "int":"integer",
    "double":"real",
} 

Verilog_to_Cpp = {
	"string":"string",
	"integer":"int",
	"real":"double",
}

def main(argv): #command line input-checker
    inputfile = ''
    outputfile = ''
    results =[]
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print ("")
        print ("command.py -i <inputfile> -o <outputfile>")
        print ("")
        sys.exit()
    for opt, arg in opts:
        if opt == '-h':
            print ("")
            print ("command.py -i <inputfile> -o <outputfilename>")
            print ("#input and output must be .cpp or .vams; both cannot be the same")
            print ("")
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
            if os.path.exists(inputfile) == False:
                print ("")
                print ("input file not found")
                print ("")
                sys.exit()
        elif opt in ("-o", "--ofile"):
            outputfile = arg
            
# checks the files to make sure they are opposite types
    if ".cpp" in inputfile:
        if ".vams" in outputfile:
            print ("")
            print ("input file is in C++ and output file is Verilog to be called:", outputfile)
            print ("")
            return inputfile, ".cpp", outputfile
    elif ".vams" in inputfile:
        if ".cpp" in outputfile:
            print ("")
            print ("input file is in Verilog and output file is in C++ to be called:", outputfile)
            print ("")
            return inputfile, ".vams", outputfile
    print ("")
    print ("command.py -i <inputfile> -o <outputfilename>")
    print ("#input and output must be .cpp or .vams; both cannot be the same")
    print ("")
    sys.exit()
    
if __name__ == "__main__":
	inputfile, inputtype, outputfile = main(sys.argv[1:])
	parser = p.Parser(inputfile, inputtype)
	functions = parser.getFunctions()
	variables = parser.getVariables()
	statements = parser.getStatements()
	if(inputtype == ".cpp"): #translate .cpp to .vams
		with open(outputfile, 'w') as f:
			f.write("module " + outputfile.rstrip('.vams') + ';\n')
			for function in functions: #write function definitions
				f.write(lb.find_Verilog(function) + '\n')
			for variable in variables: #write variable declarations
				f.write(Cpp_to_Verilog[variable["type"]] + " " + variable["name"].rstrip(';') + ";\n")
			f.write("analog begin\n")
			for statement in statements:
				if(statement["type"] == "assignment"):
					f.write(statement["line"].replace(statement["datatype"] + " ", ""))
				elif(statement["type"] == "conditional"):
					if(statement["open"] == True):
						f.write(statement["line"].replace("{","begin"))
					else:
						f.write(statement["line"].replace("}","end"))
				elif(statement["type"] == "print"):
					f.write(statement["line"].replace("printf","$display"))
				else:
					f.write(statement["line"])
			f.write("end\n")
			f.write("endmodule")
	else: #translate .vams to .cpp
		with open(outputfile, 'w') as f:
			for function in functions:#write function definitions above main
				f.write(lb.find_Cpp(function) + '\n')
			f.write("int main(){\n")
			for variable in variables:#declare variables
				f.write(Verilog_to_Cpp[variable["type"]] + " " + variable["name"].rstrip(';') + ";\n")
			for statement in statements:
				if(statement["type"] == "assignment"):
					f.write(statement["line"].replace(statement["datatype"] + " ", ""))
				elif(statement["type"] == "conditional"):
					if(statement["open"] == True):
						f.write(statement["line"].replace("begin","{"))
					else:
						f.write(statement["line"].replace("end","}"))
				elif(statement["type"] == "print"):
					f.write(statement["line"].replace("$display","printf"))
				else:#write statement as is
					f.write(statement["line"])
			f.write("}")
	#print input and output file contents for convenient comparison
	f = open(inputfile, 'r')
	contents = f.read()
	print(contents)
	f.close()
	f = open(outputfile, 'r')
	contents = f.read()
	print(contents)
	f.close()	 
