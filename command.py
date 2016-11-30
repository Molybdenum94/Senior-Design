import sys, getopt, os.path, csv

def main(argv):
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
# Imports the text file into an array
            filetext = []
            with open(inputfile, newline='') as textfile:
                for row in csv.reader(textfile):
                    filetext.append(row)
            print (*filetext)
            sys.exit()
    elif ".vams" in inputfile:
        if ".cpp" in outputfile:
            print ("")
            print ("input file is in Verilog and output file is in C++ to be called:", outputfile)
            print ("")               
            filetext = []
            with open(inputfile, newline='') as textfile:
                for row in csv.reader(textfile):
                    filetext.append(row)
            print (*filetext)
            sys.exit()
    print ("")
    print ("command.py -i <inputfile> -o <outputfilename>")
    print ("#input and output must be .cpp or .vams; both cannot be the same")
    print ("")
    sys.exit()
    
if __name__ == "__main__":
   main(sys.argv[1:])
