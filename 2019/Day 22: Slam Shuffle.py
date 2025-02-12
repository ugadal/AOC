#!/usr/bin/env python
# -*- coding: utf-8 -*-
fn,part="d22.txt",0
from functools import cache
from intcodegen import computer
import itertools as it
pgm=open(fn).read().splitlines()
ld=10007
sp=2019
def dwi(inc):
	def fun(x):
		return (x*inc)%ld
	return fun
def dins(x):
	return ld-x-1
def cut(cp):
	def fun(x):
		return (x-cp)%ld
	return fun
P=[]
for line in pgm:
	match line.split():
		case ['deal','with','increment',*arg]:
			P.append(dwi(int(arg[0])))
			# ~ sp=(sp*inc)%ld
		case ["deal","into","new","stack"]:
			P.append(dins)
		case ["cut",*arg]:
			cp=int(arg[0])
			P.append(cut(cp))
			# ~ sp-=cp
			# ~ sp=sp%ld
# ~ print (sp)
for f in P:
	sp=f(sp)
print(sp)
