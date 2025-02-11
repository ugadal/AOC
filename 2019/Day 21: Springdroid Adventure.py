#!/usr/bin/env python
# -*- coding: utf-8 -*-
fn,part="d21.txt",0
from functools import cache
from intcodegen import computer
import itertools as it
pgm=open(fn).readline().strip()
pc=list(it.product(("AND","OR","NOT"),("A","B","C","D","T","J"),("T\n","J\n")))
# ~ for p in pc:print(" ".join(p))
pc=[" ".join(p) for p in pc]
# ~ pc.remove("NOT D J\n")
for r in range(4,16):
	print("\n",r)
	for x,p in enumerate(it.product(pc,repeat=r)):
		print(x,end="\r")
		if x<566200:continue
		c=computer(pgm)
		c.inp.extend([*map(ord,"".join(p))])
		c.inp.extend([*map(ord,"WALK\n")])
		res=list(c.flow)
		if res[34:40]!=list(map(ord,"Didn't")):
			print (p)
			print(res)
			for v in res:
				try:print(chr(v),end="")
				except:continue
			input()
exit()

# ~ 'OR A T\n'
# ~ 'AND C T\n'
# ~ 'NOT T J\n'
# ~ 'AND D J\n'
