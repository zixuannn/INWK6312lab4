"""
matplotlib code got from Lab4 material
Author: Lab Instructor
Date: May 12, 2020
"""

import lab4task1 as t
import math as m
import matplotlib.pyplot as pl

r = 1
y = []
x = []
for k,v in t.word_dict.items():
	f = m.log(t.count) - 0.8*m.log(r)
	y.append(f)
	x.append(r)
	r += 1


pl.clf()
pl.xscale("log")
pl.yscale("log")
pl.title("Zipf's Law")
pl.xlabel("rank")
pl.ylabel("log f")
pl.plot(x, y)
pl.show()