#!/usr/bin/env python
# -*- coding: utf-8 -*-
part=0

import re
import sys
import itertools as it
from functools import cache
import uuid
import numpy as np
cp=str(sys.argv[0])
dre=re.compile(r"^Day (\d+):")
day=dre.findall(cp)[0]
fn=f"d{day}.txt"
block=open(fn).read().split("\n\n\n")[part]
# ~ block=open(fn).read().split("\n\n")[part]
scre=re.compile(r"^--- scanner (\d+) ---$")
scanners={}
class scanner():
	asc={}
	def __init__(self,n):
		scanner.asc[n]=self
		self.n=n
		self.p=set()
		self.off=None
for line in block.splitlines():
	if line=="":continue
	if scre.match(line):
		n=int(scre.findall(line)[0])
		cs=scanner(n)
		print(line)
		continue
	cs.p.add(tuple(map(int,(line.split(",")))))
AS=scanner.asc.values()
for s in AS:
	print(s.n)
	print(s.p)
	minx=min(p[0] for p in s.p)
	miny=min(p[1] for p in s.p)
	minz=min(p[2] for p in s.p)
	s.p=set((a-minx,b-miny,c-minz) for a,b,c in s.p)
	s.off=(minx,miny,minz)
for s in AS:
	print(s.n)
	print(s.p)
	print(s.off)
for a,b in it.combinations(AS,2):
	print (a.n,b.n,len(a.p&b.p))
V=np.array([(1,0,0),(0,1,0),(0,0,1)])
OR=[]
for a,b in it.permutations(V,2):
	OR.append(np.array([a,b,np.cross(a,b)]))
	OR.append(np.array([-a,b,np.cross(-a,b)]))
	OR.append(np.array([a,-b,np.cross(a,-b)]))
	OR.append(np.array([-a,-b,np.cross(-a,-b)]))
print(OR)
