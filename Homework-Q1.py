import string

punc = string.punctuation + string.whitespace

file = open("book.txt",mode="r")
word = open("words.txt")
word = [i for i in word]
word_dict = {}

res = []
set_book = set()
for line in file:
	tmp = line.split(" ")
	for w in tmp:
		w = w.strip(punc)
		w = w.lower()
		set_book.add(w)
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

print()

# Q1 Part2 Use Python Set

set_word = set(word)
set_ans = set_book - set_word
for i in set_ans:
	print(i)
print("Use Python Set, the difference is",len(set_ans))
