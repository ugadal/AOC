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
block=open(fn).read().split("\n\n\n")[part]
# ~ block=open(fn).read().split("\n\n")[part]
dots,fi=block.split("\n\n")
R=C=0
D=set()
for line in dots.splitlines():
	c,r=map(int,line.split(","))
	D.add((c,r))
	R=max(R,r)
	C=max(C,c)
print (f"R:{R+1} C:{C+1}")
# ~ exit()
G=[]
for r in range(R+2):
	G.append("".join(["#" if (c,r) in D else "." for c in range(C+1)]))
# ~ for r in G:print(r)
# ~ print()
def foldh(v):
	# ~ e=len(G)//2
	# ~ if e!=v:exit()
	# ~ assert 2*e+1==len(G)
	NG=[]
	for a,b in zip(G[:v],G[::-1]):
		assert len(a)==len(b)
		nr="".join(["#" if x=="#" or y=="#" else "." for x,y in zip(a,b)])
		NG.append(nr)
	return NG
def foldv(v):
	# ~ e=len(G[0])//2
	# ~ if e!=v:exit()
	NG=[]
	for row in G:
		nr="".join(["#" if x=="#" or y=="#" else "." for x,y in zip(row[:v],row[::-1])])
		NG.append(nr)
	return NG
todo=True
for inst in fi.splitlines():
	v=int(inst.split("=")[1])
	if inst.count("x"):G=foldv(v)
	else:G=foldh(v)
	d=0
	if todo:
		for r in G:
			d+=r.count("#")
		print("p1:",d)
		todo=False
for r in G:print(r)	
print(len(G),len(G[0]))
