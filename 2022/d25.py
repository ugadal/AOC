#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ~ import sympy
import sys
from random import shuffle as shf
day=sys.argv[0].split(".")[0][1:]
exp=f"exp{day}.txt"
real=f"d{day}.txt"
"""
x%5 : 0 -> 0
	 1  -> 1
	 2  -> 1
	 3 -> =
	 4 -> -
x- %   /5:
	rinse and repeat
"""
# ~ while True:
	# ~ x=int(input())
def dectosnaf(x):
	s=""
	while x:
		m=x%5
		match str(m):
			case "3":
				s="="+s
				x+=7
			case "4":
				s="-"+s
				x+=8
			case _:s=str(m)+s
		x-=m
		x//=5
	return(s)
def snaftodec(s):
	r=0
	p=1
	for c in s[::-1]:
		if c in ["0","1","2"]:
			r+=int(c)*p
			p*=5
		elif c=="-":
			r-=p
			p*=5
		else:
			r-=2*p
			p*=5
	return r
su=0
for line in open(0).read().splitlines():su+=snaftodec(line)
print(su)
print(dectosnaf(su))
