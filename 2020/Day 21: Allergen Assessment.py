#!/usr/bin/env python
# -*- coding: utf-8 -*-
part=1
import re
import sys
import itertools as it
from functools import cache
import uuid
cp=str(sys.argv[0])
dre=re.compile(r"^Day (\d+):")
day=dre.findall(cp)[0]
fn=f"d{day}.txt"
blocks=open(fn).read().split("\n\n")[part]
IL=set()
AL=set()
R=[]
IL=[]
AL={}
for line in blocks.splitlines():
	il,al=line.split(" (contains ")
	il=il.split()
	al=al[:-1].split(", ")
	IL+=il
	for a in al:
		if a in AL:AL[a]&=set(il)
		else:AL[a]=set(il)
print(IL)
for k,v in AL.items():print(k,v)
# ~ af=s
AF = set([i for v in AL.values() for i in v])
SF = [i for i in IL if i not in AF]
print(f'p1: {len(SF)} ')

fixed={}
while AL:
	K=[(k,list(v)[0]) for k,v in AL.items() if len(v)==1]
	print(K)
	for k,v in K:
		fixed[k]=v
		del AL[k]
		for a,b in AL.items():
			if v in b:b.remove(v)
for k,v in fixed.items():print(f"{k} -> {v}")
print("p2:",",".join([v for k,v in sorted(fixed.items())]))
