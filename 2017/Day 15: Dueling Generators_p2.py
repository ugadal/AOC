#!/usr/bin/env python
# -*- coding: utf-8 -*-

def mkgen(pv,f,m):
	while True:
		pv*=f
		pv%=2147483647
		if pv%m==0:yield pv
A=mkgen(722,16807,4)
B=mkgen(354,48271,8)
m=0
for k in  range(5000000):
	a=next(A)
	b=next(B)
	if bin(a)[-16:]==bin(b)[-16:]:
		m+=1
		print(k,m)
print(m)
