import cpp_vams_library as lb
import cpp_vams_parser as p
import tkinter
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

def main(i, o, outputName): #command line input-checker
	inputPath = i.get()
        outputPath = o.get()
	parser = p.Parser(inputPath, inputtype)
	functions = parser.getFunctions()
	variables = parser.getVariables()
	statements = parser.getStatements()
	if ".cpp" in inputPath: #translate .cpp to .vams
		with open(outputfile, 'w') as f:
			f.write("module " + outputName.rstrip('.vams') + ';\n')
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
