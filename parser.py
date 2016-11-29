Cpp_keywords = ['int','float','string','double','unsigned','signed']
lines = []
with open ('test.cpp', 'rt') as in_file: # Open file lorem.txt for reading of text data.
	for line in in_file:# For each line of text, store it in a string variable named "line", and 
		lines.append(line.rstrip('\n')) # add that line to our list of lines. print(lines) # print the list object.
print lines

for i in range(0, lines.len): #first pass, find functions
	if(containsKeyword(lines[i]):
		
	
