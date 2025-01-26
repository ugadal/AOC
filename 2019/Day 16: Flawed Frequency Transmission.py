#!/usr/bin/env python
# -*- coding: utf-8 -*-
fn,part="d16.txt",0
sep="\n\n"
import math
def gen(r):
	def ig(r):
		I=[0,1,0,-1]
		while True:
			for c in I:
				for x in range(r):
					yield c
	mg=ig(r+1)
	next(mg)
	while True:
		yield next(mg)
		
def ld(x):	return int(str(x)[-1])
z=list(map(int,list("69317163492948606335995924319873")))
z=open(fn).readline().strip()
z=list(map(int,list(z)))
ml=len(z)
print(ml)
for fft in range(100):
	print(fft)
	z=[ld(sum(a*b for a,b in zip(z,gen(l)))) for l in range(ml)]
print("".join(str(c) for c in z[:8]))
