#!/usr/bin/env python
# -*- coding: utf-8 -*-
part=1

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
V=np.array([(1,0,0),(0,1,0),(0,0,1)])
OR=[]
for a,b in it.permutations(V,2):
	OR.append(np.array([a,b,np.cross(a,b)]))
	OR.append(np.array([-a,b,np.cross(-a,b)]))
	OR.append(np.array([a,-b,np.cross(a,-b)]))
	OR.append(np.array([-a,-b,np.cross(-a,-b)]))
scanners={}
class scanner():
	asc={}
	def __init__(self,n):
		scanner.asc[n]=self
		self.n=n
		self.p=set()
		self.cp=None
		self.cv=None
	def read(self,frame):
		self.cp=[tuple(np.dot(frame,p)) for p in self.p]
		self.cv=set((ax-bx,ay-by,az-bz) for (ax,ay,az),(bx,by,bz) in it.combinations(self.cp,2))
		return self.cv
	def tovec(self):
		for (ax,ay,az),(bx,by,bz) in it.permutations(self.cp,2):
			self.V.add((ax-bx,ay-by,az-bz))
			self.V.add((bx-ax,by-ay,bz-az))
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
fs=scanner.asc[0]
reg=OR[0]
cd=fs.read(reg)
ss=scanner.asc[1]
cb=0
for ori in OR:
	common=len(cd&ss.read(ori))
	if common>cb:
		goodori=ori
		cb=common
print(goodori,cb)
ss.read(goodori)
print(ss.cv&cd)
offsets={}
def merge(a,b):
	rec=float("Inf")
	for ax,ay,az in a.cp:
		for bx,by,bz in b.cp:
			z=set(a.cp)
			dx,dy,dz=bx-ax,by-ay,bz-az
			for tx,ty,tz in b.cp:
				z.add((tx-dx,ty-dy,tz-dz))
			if len(z)<rec:
				rec=len(z)
				print(rec,dx,dy,dz)
				goodoffset=(-dx,-dy,-dz)			
				gs=z
	offsets[b.n]=goodoffset
	return gs
todo=AS[1:]
while todo:
	print(len(todo),todo)
	cb=0
	for ts in todo:
		for ori in OR:
			common=len(cd&ts.read(ori))
			if common>cb:
				goodscan=ts
				goodori=ori
				cb=common
	# ~ print("goodmap",goodscan.n)
	# ~ print(goodori)
	# ~ print(goodscan in todo)
	# ~ input()
	goodscan.read(goodori)
	cd=merge(fs,goodscan)
	fs.p=cd
	cd=fs.read(reg)
	print("final",len(fs.p))
	todo.remove(goodscan)
# ~ print(goodori,cb)
# ~ ss.read(goodori)
# ~ print(ss.cv&cd)
			
			
res=merge(fs,ss)
print(len(fs.cp),len(ss.cp),len(res),res)
print("p1:",len(fs.p))
# ~ print(offsets)
def md(a,b):
	return sum(abs(x-y) for x,y in zip(a,b))
r=max(md(a,b) for a,b in it.combinations(offsets.values(),2))
print("p2:",r)
