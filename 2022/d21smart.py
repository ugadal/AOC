#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sympy
exp=f"exp21.txt"
real=f"d21.txt"
V={"humn":sympy.symbols("x")}
lines=open(exp).read().splitlines()
lines=open(real).read().splitlines()
ops={
"+": lambda x,y:x+y,
"-": lambda x,y:x-y,
"*": lambda x,y:x*y,
"/": lambda x,y:x/y}
for line in lines:
	print(line)
	k,f=line.split(": ")
	if k=="humn":continue
	if f.isdigit():
		V[k]=int(f)
		continue
	l,op,r=f.split()
	if l in V and r in V:
		if k=="root":
			print(V[l])
			print(V[r])
			res=sympy.solve(V[l]-V[r])
			print(res)
			exit()
		V[k]=ops[op](V[l],V[r])
	else:
		lines.append(line)
		print(len(lines))


