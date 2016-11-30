import library as lib
import cpp_vams_parser as p

import sys, getopt, os.path

# Driver prototype for C++/Verilog translator
# Constraints: 
# 1. limited set of data types, no arrays. Only primitives, no hardware keywords in Verilog. 
# C++ : signed, unsigned, char, short, int, float, double, string 
# Verilog : signed, unsigned, byte, shortint, integer, shortreal, real, string
# 2. no typecasting
# 3. Conditionals allowed : if, else, for
# 4. printf and $display only accept integer and string values
# 5. one statement per line
# 6. "=" surrounded by whitespace
# 7. last non-whitespace character of line followed by ;
# 8. VAMS procedural code encapsulated in analog begin/end blocks
# 9. no macros
# 10. no comments
# 11. no consts
# 12. simple scoping

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
    lib.print_Functions()
    parser = p.Parser(inputfile, inputtype)
    
