#!/usr/bin/env python
# -*- coding: utf-8 -*-

def mkgen(pv,f):
	while True:
		pv*=f
		pv%=2147483647
		yield pv
A=mkgen(722,16807)
B=mkgen(354,48271)
m=0
for k in  range(40000000):
	a=next(A)
	b=next(B)
	if bin(a)[-16:]==bin(b)[-16:]:
		m+=1
		print(k,m)
print(m)
