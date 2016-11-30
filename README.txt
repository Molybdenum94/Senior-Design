C++/Verilog translator prototype

Note: the .cpp and .vams test files only contain sequential lines of code to be executed. Function definitions are not included in the test files, so functions are assumed to be defined on the input side.
The output files are the functionally equivalent statements in the translated language. Function definitions 

Constraints: 
# 1. limited set of data types, no arrays. Only primitives, no hardware keywords in Verilog. 
# C++ : char, short, int, float, double, string 
# Verilog : byte, shortint, integer, shortreal, real, string
# 2. no typecasting
# 3. Conditionals allowed : if, else, for
# 4. printf and $display only accept integer and string values
# 5. one statement per line
# 6. "=" surrounded by whitespace
# 7. last non-whitespace character of line followed by ;
# 9. no macros
# 10. no comments
# 11. no consts
# 12. simple scoping (all variables accessible from outer scope)
