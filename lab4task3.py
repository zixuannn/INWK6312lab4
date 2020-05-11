import lab4task1 as t
import math as m
import matplotlib.pyplot as pl

r = 1
y = []
x = []
for k,v in t.word_dict.items():
	f = m.log(t.count) - 0.6*m.log(r)
	#print(k, "f:",f, "r:",r)
	y.append(f)
	x.append(r)
	r += 1

pl.clf()
pl.xscale("log")
pl.yscale("log")
pl.title("title string")
#pl.xlable("log r")
#pl.ylable("log f")
pl.plot(x, y)
pl.show()