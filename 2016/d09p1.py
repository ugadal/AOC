#!/usr/bin/env python
# -*- coding: utf-8 -*-
test="""ADVENT
A(1x5)BC
(3x3)XYZ
A(2x2)BCD(2x2)EFG
(6x1)(1x3)A
X(8x2)(3x3)ABCY
"""
tt=0
for line in open("d09.txt").read().splitlines():
	ep=len(line)
	R=[]
	while line.count("("):
		op=next(i for i,c in enumerate(line) if c=="(")
		cp=next(i for i,c in enumerate(line) if c==")")
		code=line[op+1:cp]
		l,r=map(int,code.split("x"))
		R.append(line[:op])
		for _ in range(r):
			R.append(line[cp+1:cp+1+l])
		line=line[cp+l+1:]
	R.append(line)
	R="".join(R)
	print(R,len(R))
	tt+=len(R)
print(tt)
