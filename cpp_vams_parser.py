import regex as re
# Parser prototype for C++/Verilog translator
# categorizes statements into 4 types: 
# 1. variable assignment
# 2. conditional (if, else. replace '{','}', with 'begin','end' and vice versa)
# 3. print (replace printf with $display and vice versa)
# 4. compatible (either a function call or variable declaration, no need to process)
#
cppKeywords = [ #contains mappings of both Verilog-C++ and C++-Verilog data types
    "string",
    "int",
    "double",
] 

vamsKeywords = [
	"string",
	"integer",
	"real",
]

conditionalKeywords = [
	"if",
	"else"
]

printKeywords = [
	"printf",
	"$display"
]
		
#regex1 = '^(\w*)(?=\()' #case 1: function call at beginning of line
#regex2 = '(?<=\s)(\w*)(?=\()' #case 2: function call following whitespace
#regex3 = '(?<=\W)(\w*)(?=\()' #case 3: function call following non-alphanumeric character

class Parser:

	def __init__(self,filename,language):
		self.lines = [] #lines of input file
		self.functions = []
		self.variables = []
		self.statements = []
		self.language = language
		with open (filename, 'rt') as in_file: # Open input file for reading of text data.
			for line in in_file: # For each line of text, store it in a string variable named "line", and 
				self.lines.append(line) # add that line to our list of lines.
			if(self.language == ".cpp"):
				self.lines = self.lines[1:-1] #remove int main(){ and } lines
			else:
				self.lines = self.lines[2:-2] #remove module declaration, module begin and end lines

		for i in range(0, len(self.lines)): #find functions and variables
			self.processFunctions(self.lines[i])
			breakdown = self.lines[i].split()
			if(self.language == ".cpp"): #process .cpp statements
				if(breakdown[0] in cppKeywords): #variable declaration
					#breakdown1 = breakdown[1].split(",")
					#for name in breakdown1:
					self.variables.append({"type":breakdown[0],"name":breakdown[1]})
					if("=" in breakdown):
						statement = {"line":self.lines[i],"type":"assignment", "datatype":breakdown[0]}
						self.statements.append(statement)
				elif("=" in breakdown): #variable assignment without declaration
					statement = {"line":self.lines[i],"type":"compatible"}
					self.statements.append(statement)
				elif(self.isConditional(self.lines[i]) == True):
					if(self.lines[i].find('}') != -1):
						self.statements.append({"line":self.lines[i],"type":"conditional","open":False})
					else:
						self.statements.append({"line":self.lines[i],"type":"conditional","open":True})			
				elif(self.isPrint(self.lines[i]) == True):
					self.statements.append({"line":self.lines[i],"type":"print"})
				else:
					self.statements.append({"line":self.lines[i],"type":"compatible"})
			else: #process .vams statements
				if(breakdown[0] in vamsKeywords): #variable declaration
					#breakdown1 = breakdown[1].split(",")
					#for name in breakdown1:
					self.variables.append({"type":breakdown[0],"name":breakdown[1]})
					if("=" in breakdown):
						statement = {"line":self.lines[i],"type":"assignment", "datatype":breakdown[0]}
						self.statements.append(statement)
				elif("=" in breakdown): #variable assignment without declaration
					statement = {"line":self.lines[i],"type":"compatible"}
					self.statements.append(statement)
				elif(self.isConditional(self.lines[i]) == True):
					if(self.lines[i].find('end') != -1):
						self.statements.append({"line":self.lines[i],"type":"conditional","open":False})
					else:
						self.statements.append({"line":self.lines[i],"type":"conditional","open":True})			
				elif(self.isPrint(self.lines[i]) == True):
					self.statements.append({"line":self.lines[i],"type":"print"})
				else:
					self.statements.append({"line":self.lines[i],"type":"compatible"})

	def isConditional(self,inputstring):
		m1 = re.match(r'^(\bif\b)(?=\()', inputstring)
		m2 = re.match(r'^(\belse\b)(?=\()', inputstring)
		if(m1 != None or m2 != None):
			return True
		elif(inputstring.find('}') != -1):
			return True
		elif(inputstring.find('end') != -1): #not robust to variables including 'end'
			return True
		else:
			return False	

	def isPrint(self,inputstring):
		return (re.match(r'\bprintf\b',inputstring) != None or re.match(r'\$\bdisplay\b',inputstring) != None)

	def processFunctions(self,inputstring):
		if(self.isConditional(inputstring) == True or self.isPrint(inputstring) == True):
			pass
		m1 = re.match('^(\w*)(?=\()', inputstring)
		m2 = re.search('(?<=\s)(\w*)(?=\()', inputstring) #Use search function for regexes with lookbehind assumptions (will search beginning of string)
		m3 = re.search('(?<=\W)(\w*)(?=\()', inputstring)
		if(m1 != None):
			for function in m1.captures(0):
				if(function not in self.functions and function not in conditionalKeywords and function not in printKeywords):
					self.functions.append(function)
		if(m2 != None):
			for function in m2.captures(0):
				if(function not in self.functions and function not in conditionalKeywords and function not in printKeywords):
					self.functions.append(function)
		if(m3 != None):
			for function in m3.captures(0):
				if(function not in self.functions and function not in conditionalKeywords and function not in printKeywords):
					self.functions.append(function)
	def getFunctions(self):
		return self.functions
	def getVariables(self):
		return self.variables
	def getStatements(self):
		return self.statements
