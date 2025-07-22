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
	tp=tuple(map(int,line.split(",")))
	cs.p.add(tp)
AS=list(scanner.asc.values())
def rebase(s):
	minx=min(p[0] for p in s)
	miny=min(p[1] for p in s)
	minz=min(p[2] for p in s)
	res=set((a-minx,b-miny,c-minz) for a,b,c in s)
	return (minx,miny,minz),res
V=np.array([(1,0,0),(0,1,0),(0,0,1)])
OR=[]
for a,b in it.permutations(V,2):
	OR.append(np.array([a,b,np.cross(a,b)]))
	OR.append(np.array([-a,b,np.cross(-a,b)]))
	OR.append(np.array([a,-b,np.cross(a,-b)]))
	OR.append(np.array([-a,-b,np.cross(-a,-b)]))
def loopor(s):
	P=[np.array(x) for x in s]
	for ori in OR:
		t=[np.dot(ori,p) for p in P]
		ofs,t=rebase(t)
		yield t
os,k=rebase(AS[0].p)
# ~ print(os,k)
done=0
for t in AS[1:]:
	for z in loopor(t.p):
		done+=1
		# ~ print(k)
		# ~ print(z)
		print(done,len(k),len(z),len(k&z))
		# ~ exit()
# ~ --- scanner 0 ---
# ~ 0,2  
# ~ 4,1  
# ~ 3,3	 

# ~ as vectors :
	# ~ 4,-1
	# ~ 3,1
	# ~ -1,2

# ~ --- scanner 1 ---
# ~ -1,-1 
# ~ -5,0  
# ~ -2,1  
# ~ av 
# ~ -4,1
# ~ -1,2
# ~ 3,1
