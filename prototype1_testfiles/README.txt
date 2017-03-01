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
# 13. structure of vams file is module with variable/function definitions followed by an analog block of executable statements

About test files
Cpp to Verilog:
input: testcvx.cpp
output: testcvx.vams

Verilog to Cpp:
input: testvcx.vams
output: testvcx.cpp

TRANSLATIONS ARE NOT REVERSIBLE (Only works 1 way, can't use the output file, translate, and get the original back)


About individual test cpp files:
testcv0.cpp:
-basic variable declarations/assignments, function call 
testcv1.cpp:
- same as previous, but with nested function call, logical operators (!, <<), if statement
testcv2.cpp:
- expressions including a function call, recursive function call (although this is not allowed in vams) 
testcv3.cpp:
- if/else statement, multiple variables of same type declared on one line
testcv4.cpp:
- multiple variables declared on one line (same type). multiple function calls used in expression

About individual test vams files:

testvc0.vams:
-basic variable declarations/assignments, function call, print function
testvc1.vams:
- nested function call, logical operators, if statement
testvc2.vams:
- expressions including a function call
testvc3.vams:
- if/else statement, multiple variables of same type declared on one line
testvc4.vams:
- nested if,if/else statements, multiple function calls used in expression, multiple variables declared on one line

