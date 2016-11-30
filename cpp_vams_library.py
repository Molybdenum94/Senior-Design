#Library prototype for C++/Verilog translator
#function name to definition hashmaps
Cpp_to_Verilog = {
	"function_a" : "function int function_a;\ninput x,y;\ninteger x,y;\nbegin\nfunction_a = x + y;\nend\nendfunction\n",
	"function_b" : "function real function_b;\ninput x;\nreal x;\nbegin\nfunction_b = x * x;\nend\nendfunction\n",
	"function_c" : "function void function_c;\nbegin\n$display('Hello World')\nend\nendfunction\n"   
}

Verilog_to_Cpp = {
	"function_a" : "int function_a(int x, int y){\nreturn x + y;\n}\n",
	"function_b" : "double function_b(double x){\nreturn x * x;\n}\n",
	"function_c" : "void function_c(){\nprintf('Hello World');\n}\n"
}


#Returns corresponding Verilog code for given C++ function name
def find_Verilog(cpp_key): 
	return Cpp_to_Verilog.get(cpp_key, None) #returns None if no match


#Returns corresponding C++ code for given Verilog function name
def find_Cpp(verilog_key): 
	return Verilog_to_Cpp.get(verilog_key, None) #returns None if no match	

def print_Functions():
	print "C++ function definitions: \n"
	for function in Verilog_to_Cpp.values():
		print function + '\n'
	print "Verilog function definitions: \n"
	for function in Cpp_to_Verilog.values():
		print function + '\n'
	
