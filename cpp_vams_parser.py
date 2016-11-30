import regex as re
# Parser prototype for C++/Verilog translator
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

Cpp_to_Verilog = { #contains mappings of both Verilog-C++ and C++-Verilog data types
    "string":"string",
    "char":"byte",
    "short":"shortint",
    "int":"integer",
    "double":"real",
    "unsigned":"unsigned",
    "signed":"signed"
} 

Verilog_to_Cpp = {
	"string":"string",
	"byte":"char",
	"shortint":"short",
	"integer":"int",
	"real":"double",
	"unsigned":"unsigned",
	"signed":"signed"
}
		
regex1 = '^(\w*)(?=\()' #case 1: function call at beginning of line
regex2 = '(?<=\s)(\w*)(?=\()' #case 2: function call following whitespace
regex3 = '(?<=\W)(\w*)(?=\()' #case 3: function call following non-alphanumeric character

class Parser:

	def __init__(self,filename,language):
		self.lines = [] #lines of input file
		self.functions = []
		self.variables = []
		self.language = language
		with open ("test2.cpp", 'rt') as in_file: # Open input file for reading of text data.
			for line in in_file: # For each line of text, store it in a string variable named "line", and 
				self.lines.append(line.rstrip('\n')) # add that line to our list of lines.
		for i in range(0, len(self.lines)): #first pass, find functions and variables
			if(self.language == "cpp"):
				self.processKeywords(self.lines[i], Cpp_to_Verilog)
			else:
				self.processKeywords(self.lines[i], Verilog_to_Cpp)
				self.processFunctions(self.lines[i])

	def processKeywords(self,inputstring, keywordList):
		found = False
		for key in keywordList:
			regex = '^' + key
			result = re.search(regex, inputstring)
			if(result != None):
				found = True
		return found

	def processFunctions(self,inputstring):
		m1 = re.match(regex1, inputstring)
		m2 = re.search(regex2, inputstring) #Use search function for regexes with lookbehind assumptions (will search beginning of string)
		m3 = re.search(regex3, inputstring)
		if(m1 != None):
			print m1.captures(0)
		if(m2 != None):
			print m2.captures(0)
		if(m3 != None):
			print m3.captures(0)
