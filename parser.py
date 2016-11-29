import re
import library as lib
Cpp_keywords = ["int","float","string","double","unsigned","signed"]
lines = []
def containsKeyword(inputstring):
	found = False
	for key in Cpp_keywords:
		regex = '^' + key
		result = re.search(regex, inputstring)
		if(result != None):
			found = True
	return found

def isFunctionCall(inputstring):
	regex1 = '^\w*(?=[(])'
	regex2 = '(?<=\s)\w*(?=[(])'
	print re.match(regex1, inputstring)
	print re.match(regex2, inputstring)

with open ('test2.cpp', 'rt') as in_file: # Open file lorem.txt for reading of text data.
	for line in in_file:# For each line of text, store it in a string variable named "line", and 
		lines.append(line.rstrip('\n')) # add that line to our list of lines. print(lines) # print the list object.


for i in range(0, len(lines)): #first pass, find functions and variables
	if(containsKeyword(lines[i]) == True):
		print lines[i] #processes int, float, string, double, unsigned
	isFunctionCall(lines[i])
