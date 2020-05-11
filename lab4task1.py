import string

punc = string.punctuation + string.whitespace

file = open("book.txt",mode="r")

count = 0
word_dict = {}
res = []

for line in file:
	tmp = line.split(" ")
	count += len(tmp)
	for word in tmp:
		word = word.strip(punc)
		word = word.lower()
		if word_dict.get(word) is None:
			word_dict[word] = 1
		else:
			word_dict[word] += 1

for k,v in word_dict.items():
	res.append((v,k))
res.sort(reverse=True)

for i in res[:20]:
	print(i[1], i[0])

print("The # of different words used in the book is", len(word_dict))