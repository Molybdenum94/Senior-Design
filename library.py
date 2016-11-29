#hashmaps
Cpp_to_Verilog = {"function_a" : "function function_a: input x,y; begin ... end endfunction"}
Verilog_to_Cpp = {"function_a" : "void function_a(int x, int y){...}"}


#Returns corresponding Verilog code for given C++ function name
def find_Verilog(cpp_key): 
	return Cpp_to_Verilog.get(cpp_key, None) #returns None if no match


#Returns corresponding C++ code for given Verilog function name
def find_Verilog(verilog_key): 
	return Cpp_to_Verilog.get(verilog_key, None) #returns None if no match	

def print_Functions():
	print "C++ function definitions: \n"
	for function in Verilog_to_Cpp.values():
		print function + '\n'
	print "Verilog function definitions: \n"
	for function in Cpp_to_Verilog.values():
		print function + '\n'
	
