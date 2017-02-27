# Prototype for constucting library object

# ---------- CONSTANTS ---------- #
# define the substring to be replaced in definitions in the dictionary 
VARIABLE_ID = "unknown"
# ---------- CONSTANTS ---------- #

# ---------- RESOURCE COMMANDS ---------- #
class Dictionary(object):

	ATE = {
	'example1'		: "Give me values for parameters {0}, {1}, and {2}",
	'example2'		: "But now only give me {0} {1}.",
	'example3'		: "Jeff Gordon drives number {2}",
	'examplary'		: ['example1','example2','example3'],
	'cbitclose' 	: "Stuff goes here",
	'cbitopen' 		: "Stuff goes here",
	'connect'		: "Stuff goes here",
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

# ---------- TRANSLATE COMMAND ---------- #
# Recursively search function dictionary for line by line translation
def translate(funcName, variables):
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

# ---------- TRANSLATE COMMAND ---------- #

string = 'examplary'
vars = ['blue','applesauce', 24]
result = translate(string,vars)
print (result)
