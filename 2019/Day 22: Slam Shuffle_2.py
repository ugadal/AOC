#!/usr/bin/env python
# -*- coding: utf-8 -*-
fn,part="d22.txt",0
import sys
from functools import cache
from intcodegen import computer
import itertools as it
pgm=open(fn).read().splitlines()
def dwi(inc):
	def fun(x):return (x*inc)%ld
	return fun
def dins(x):return ld-x-1
def cut(cp):
	def fun(x):return (x-cp)%ld
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
# ~ ld=int(sys.argv[1])
ld=119315717514047
# ~ sp=int(sys.argv[2])
# ~ st=101741582076661
cp=2020
t=0
while True:
	t+=1
	print(t,end="\r")
	for f in P:cp=f(cp)
	if cp==2020:print(t)
