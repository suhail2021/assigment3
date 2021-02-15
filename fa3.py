def rem_vowel(string):
	vowels=("a","b","c","d")
	for x in string.lower():
		if x in vowels:
			string=string.replace(x,"")
	print(string)
string="birds are flying"	
rem_vowel(string)