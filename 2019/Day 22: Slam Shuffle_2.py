#!/usr/bin/env python
# -*- coding: utf-8 -*-
fn,part="d22.txt",0
import sys
from functools import cache
from intcodegen import computer
import itertools as it
pgm=open(fn).read().splitlines()

ld=int(sys.argv[1])
ld=119315717514047
sp=int(sys.argv[2])
# ~ st=101741582076661
cp=sp
print(ld,sp)
t=0
while True:
	t+=1
	# ~ print(t,end="\r")
	for line in pgm:
		match line.split():
			case ['deal','with','increment',*arg]:
				inc=int(arg[0])
				cp=(cp*inc)%ld
			case ["deal","into","new","stack"]:
				cp=ld-cp-1
			case ["cut",*arg]:
				cutp=int(arg[0])
				cp-=cutp
				cp=cp%ld
	# ~ print(cp,end=" ")
	if sp==cp:
		print("\n",t)
		input()
	
