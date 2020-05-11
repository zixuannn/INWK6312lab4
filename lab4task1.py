import string

punc = string.punctuation

file = open("book.txt",mode="r")

for line in file:
	tmp = line.split(" ")
	for word in tmp:
		word = word.strip(punc)
		word = word.lower()
		print(word, end=" ")
	print()