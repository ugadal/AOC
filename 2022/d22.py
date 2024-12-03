#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import re
# ~ import itertools as it
# ~ from collections import deque
# ~ from tqdm import tqdm
day=sys.argv[0].split(".")[0][1:]
print(day)
import re
exp=f"exp{day}.txt"
real=f"d{day}.txt"
grid,instructions=open(exp).read().split("\n\n")
grid,instructions=open(real).read().split("\n\n")
G=grid.splitlines()
instructions=instructions.strip()
NR=len(G)
NC=max([len(l) for l in G])
NG=[]
for l in G:
	nl=l+" "*(NC-len(l))
	NG.append(nl)
G=NG
c=next(i for i,c in enumerate(G[0]) if c==".")
start=(0,c)
print(start)
class cardin():
	def __init__(self,dx,dy,v):
		self.offset=(dx,dy)
		self.R=None
		self.L=None
		self.v=v
	def nx(self,lr):
		if lr=="L":return self.L
		if lr=="R":return self.R
		return self

N=cardin(-1,0,3)
E=cardin(0,1,0)
S=cardin(1,0,1)
W=cardin(0,-1,2)
F=cardin(0,0,-1)
for a,b in zip((N,E,S,W),(E,S,W,N)):
	a.R=b
	b.L=a
print(instructions)
s=re.compile("R|L")
V=list(map(int,s.split(instructions)))
D=s.findall(instructions)
D.append(F)
print(V,D)
cr,cc=start
cd=E
pdv,cdv=0,0
for step,nxd in zip(V,D):
	dr,dc=cd.offset
	stepsdone=0
	print(f"begin :cr {cr} cc {cc} step {step} dr {dr} dc {dc}")
	while stepsdone<step:
		print(f"in movement:cr {cr} cc {cc}")
		nr=(cr+dr)%NR
		nc=(cc+dc)%NC
		if G[nr][nc]==".":
			cr,cc=nr,nc
			stepsdone+=1
			lr,lc=cr,cc
			continue
		if G[nr][nc]==" ":
			cr,cc=nr,nc
			continue
		else:
			cr,cc=lr,lc
			break
	cd=cd.nx(nxd)
	pdv,cdv=cdv,cd.v
print(1000*(cr+1)+4*(cc+1)+pdv)
