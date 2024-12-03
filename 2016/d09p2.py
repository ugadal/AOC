#!/usr/bin/env python
# -*- coding: utf-8 -*-
test="""
(3x3)XYZ
X(8x2)(3x3)ABCY
(27x12)(20x12)(13x14)(7x10)(1x12)A
(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN
"""
tt=0
def ana(line,pos):
	if not line.count("("):
		return len(line)
	op=next(i for i,c in enumerate(line[pos:]) if c=="(")
	cp=next(i for i,c in enumerate(line[pos:]) if c==")")
	code=line[op+1:cp]
	l,r=map(int,code.split("x"))
	reppart=line[cp+1:cp+1+l]
	return op+r*ana(reppart,0)+ana(line[cp+l+1:],0)

for line in open("d09.txt").read().splitlines():
# ~ for line in test.splitlines():
	print(f"{line} returns {ana(line,0)}")
