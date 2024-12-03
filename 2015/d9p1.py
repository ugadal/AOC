#!/usr/bin/env python
# -*- coding: utf-8 -*-
import itertools as it
D={}
C=set()
res=float('Inf')
for line in open(0).read().strip().splitlines():
	a,_,b,_,d=line.split()
	D[a,b]=D[b,a]=int(d)
	C.add(a)
	C.add(b)
for tour in it.permutations(C):
	tr=sum([D[a,b] for a,b in zip(tour,tour[1:])])
	print(tr,tour)
	if tr<res:res=tr
print(res)
