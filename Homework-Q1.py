import string

punc = string.punctuation + string.whitespace

file = open("book.txt",mode="r")
word = open("words.txt")
word = [i for i in word]
word_dict = {}

res = []
for line in file:
	tmp = line.split(" ")
	for w in tmp:
		w = w.strip(punc)
		w = w.lower()
		if word_dict.get(w) is None:
			word_dict[w] = 1
		else:
			word_dict[w] += 1
for k,v in word_dict.items():
	if k not in word:
		res.append(k)
for i in res:
	print(i)
print("The # of words not in words.txt is", len(res)) 