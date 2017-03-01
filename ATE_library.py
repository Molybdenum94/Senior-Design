# ---------- EXAMPLE CALL ---------- #

# To call from another module
	# ATE_library.translate(string,variables)

# Translate returns an array for instructions
	# result = translate(string,vars)

# Print line by line
	# ATE_library.libPrint(result)

# ---------- EXAMPLE CALL ---------- #
# ---------- CONSTANTS ---------- #
# define the substring to be replaced in definitions in the dictionary 
VARIABLE_ID = "unknown"
# ---------- CONSTANTS ---------- #
# ---------- RESOURCE COMMANDS ---------- #
class Dictionary(object):
	ATE = {
	'cbitclose' 	: "Stuff goes here",
	'cbitopen' 	: "Stuff goes here",
	'connect'	: "Stuff goes here",
	'disconnect'	: "Stuff goes here"
	}
# ---------- RESOURCE COMMANDS ---------- #
# ---------- LIBRARY OBJECTS ---------- #
class libraryObject:

	def __new__(cls,name):
		if name in Dictionary.ATE:
			return super(libraryObject, cls).__new__(cls)
		else:
			raise NameError('resource command ' + repr(name) + ' is not defined')

	def __init__(self, name):
		self.name = name
		self.definition = False
		self.variables = []
	# print name of ATE resource command
	def printName(self):
		print (self.name)
	# retrieve ATE resource command
	def setDef(self):
		self.definition = Dictionary.ATE[self.name]
	def printDef(self):
		if self.definition is False:
			raise ValueError('no definition assigned to object')
		else:
			print (self.definition)
	# retrieve and set variables
	def numVars(self):
		return (len(self.variables))
	def setVars(self, list):
		if self.definition is False:
			self.setDef()
		self.variables = list
		self.definition = self.definition.format(*self.variables)
	def printVars(self):
		print (self.variables)

# ---------- LIBRARY OBJECTS ---------- #
# ---------- LIBRARY COMMANDS ---------- #
# Recursively search function dictionary for line by line translation
def translate(funcName, variables):
	if type(funcName) is str:
		function = libraryObject(funcName)
		function.setDef()
		if isinstance(function.definition, list):
			funcList = []
			for entry in range(0, len(function.definition)):
				nextFunction = translate(function.definition[entry], variables)
				funcList.append(nextFunction)
			return funcList
		elif isinstance(function.definition, str):
			function.setVars(variables)
			return function.definition
		else:
			raise TypeError('unsupported operand type for ' + repr(str))
	elif type(funcName) is list:
		funcList = []
		for singleFunc in funcName:
			nextFunction = translate(singleFunc, variables)
			if type(nextFunction) is str:
				funcList.append(nextFunction)
			if type(nextFunction) is list:
				funcList.extend(nextFunction)
		return funcList
	else:
		raise TypeError('unsupported operand type for ' + repr(funcName))

def libPrint(list):
	print ('\n'.join(list))

# ---------- LIBRARY COMMANDS ---------- #

