#!/usr/bin/env python
# -*- coding: utf-8 -*-
import itertools as it
D={}
P=set()
for line in open("d13.txt").read().splitlines():
	a,_,gl,am,_,_,_,_,_,_,b=line[:-1].split()
	fac=1 if gl=="gain" else -1
	D[a,b]=fac*int(am)
	P.add(a)
	P.add(b)
rec=0
for comb in it.permutations(P):
	comb=list(comb)
	comb.append(comb[0])
	tt=0
	for a,b in zip(comb,comb[1:]):
		tt+=D[a,b]
		tt+=D[b,a]
	if tt>rec:rec=tt
print(rec)
