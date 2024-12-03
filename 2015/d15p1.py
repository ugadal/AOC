#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ~ Frosting: capacity 4, durability -2, flavor 0, texture 0, calories 5
import itertools as it
import re
dig=re.compile("-?\d+")
V=[]
for ingr,line in enumerate(open("d15.txt").read().splitlines()):
	vals=list(map(int,dig.findall(line)))
	V.append(vals)
for v in V:print(v)
ing=range(len(V))
cols=len(V[0])-1
rec=0
for comb in it.combinations_with_replacement(ing,r=100):
	fac=[comb.count(x) for x in ing]
	p=1
	cal=sum([v[-1]*f for v,f in zip(V,fac)])
	if cal!=500:continue
	for v in [max(0,sum([v[col]*f for v,f in zip(V,fac)])) for col in range(cols)]:p*=v
	if p>rec:rec=p
print(rec)
