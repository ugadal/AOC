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
print(gp("esew"))
print(gp("nwwswee"))
F=[gp(s) for s in blocks.splitlines()]
print(F,len(F))
B={}
for p in F:
	if p in B:
		B.pop(p)
	else:B[p]=True
print(B,len(B))
