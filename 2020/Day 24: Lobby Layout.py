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
def gp(s):
	r=c=0
	while s:
		if s.startswith("e"):
			r+=2
			s=s[1:]
		if s.startswith("w"):
			r-=2
			s=s[1:]
		if s.startswith("se"):
			r+=1
			c+=1
			s=s[2:]
		if s.startswith("sw"):
			r-=1
			c+=1
			s=s[2:]
		if s.startswith("ne"):
			r+=1
			c-=1
			s=s[2:]
		if s.startswith("nw"):
			r-=1
			c-=1
			s=s[2:]
	return r,c
F=[gp(s) for s in blocks.splitlines()]
B={}
for p in F:
	if p in B:
		B.pop(p)
	else:B[p]=True
print("p1:",len(B))
B={}
for p in F:
	if p in B:B[p]=not(B[p])
	else:B[p]=True
def nb(r,c):
	yield r+2,c
	yield r-2,c
	yield r+1,c+1
	yield r-1,c+1
	yield r+1,c-1
	yield r-1,c-1
def gnb(r,c):
	return [B.get(p,False) for p in nb(r,c)]
# ~ print(B,len(B))
for x in range(1,101):
	TF=[]
	Bl=[b for b,v in B.items() if v]
	Wh=[b for b,v in B.items() if not v]
	# ~ print(Bl,len(Bl))
	# ~ print(Wh,len(Wh))
	for b in Bl:
		ba=gnb(*b).count(True)
		if ba==0 or ba>2:TF.append(b)
	# ~ print("black to flip",TF)
	mir=min(r for r,c in Bl)
	mar=max(r for r,c in Bl)
	mic=min(c for r,c in Bl)
	mac=max(c for r,c in Bl)
	# ~ print(mir,mic,mar,mac)
	for r in range(mir-2,mar+3):
		for c in range(mic-2,mac+3):
			if (r+c)%2:continue   # !!!!!!!!
			if B.get((r,c),False):continue
			N=gnb(r,c)
			# ~ print(r,c,N)
			if N.count(True)==2:TF.append((r,c))
	# ~ print("tf",TF)
	for p in TF:
		B[p]=not B.get(p,False)
	Bl=[b for b,v in B.items() if v]
print("p2:",len(Bl))
	
