#!/usr/bin/env python
# -*- coding: utf-8 -*-
part=1
def repres(p,v):print(f"p{p}: {v}")
import re
import sys
import itertools as it
from functools import cache
# ~ import uuid
# ~ import numpy as np
cp=str(sys.argv[0])
dre=re.compile(r"^Day (\d+):")
day=dre.findall(cp)[0]
fn=f"d{day}.txt"
block=open(fn).read().split("\n\n\n")[part]
# ~ block=open(fn).read().split("\n\n")[part]

G={}
I=[]
for line in block.splitlines():
	st,coord=line.split()
	st=True if st=="on" else False
	V=[tuple(map(int,(r[2:].split("..")))) for r in coord.split(",")]
	(bx,ex),(by,ey),(bz,ez)=V
	I.append((st,bx,by,bz,ex,ey,ez))
	skip=any(b>50 or a<-50	for a,b in V)
	if skip:continue
	for p in ((x,y,z) for x in range(V[0][0],V[0][1]+1) for y in range(V[1][0],V[1][1]+1) for z in range(V[2][0],V[2][1]+1)):
		G[p]=st
repres(1,list(G.values()).count(True))
for i in I[:5]:print(i)
def ana(TI):
	lx=[]
	ly=[]
	lz=[]
	for st,bx,by,bz,ex,ey,ez in TI:
		lx.append(bx)
		lx.append(ex+1)
		ly.append(by)
		ly.append(ey+1)
		lz.append(bz)
		lz.append(ez+1)
	lx=sorted(list(set(lx)))
	ly=sorted(list(set(ly)))
	lz=sorted(list(set(lz)))
	ON=[]
	st,bx,by,bz,ex,ey,ez=TI[0]
	for cx,cex in zip(lx,lx[1:]):
		if bx<=cx<cex<=ex+1:
			for cy,cey in zip(ly,ly[1:]):
				if by<=cy<cey<=ey+1:
					for cz,cez in zip(lz,lz[1:]):
						if bz<=cz<cez<=ez+1:
							ON.append((cx,cy,cz,cex-1,cey-1,cez-1))
	ON=set(ON)
	for st,bx,by,bz,ex,ey,ez in TI[1:]:
		toremove=[]
		for cx,cy,cz,cex,cey,cez in ON:
			if bx<=cx<cex<=ex+1:
				if by<=cy<cey<=ey+1:
					if bz<=cz<cez<=ez+1:
						toremove.append((cx,cy,cz,cex-1,cey-1,cez-1))
		ON=ON-set(toremove)
	return ON
def isincluded(a,b):
	abx,aby,abz,aex,aey,aez=a
	bbx,bby,bbz,bex,bey,bez=b
	if bbx<=abx and aex<=bex:
		if bby<=aby and aey<=bey:
			if bbz<=abz and aez<=bez:return True
	return False
U=set()
print("collecting")
for ix,quad in enumerate(I):
	st,bx,by,bz,ex,ey,ez=quad
	if not st:continue
	print("\r",ix,quad,end="")
	Z=[quad]
	Z.extend(q for q in I[ix+1:] if not q[0])
	res=ana(Z)
	# ~ print("removing included from new")
	torem=set()
	for a,b in it.product(U,res):
		if isincluded(a,b):torem.add(a)
	U=U-torem
	# ~ print("removing new from included")
	torem=set()
	for a,b in it.product(res,U):
		if isincluded(a,b):torem.add(a)
	res=res-torem
	# ~ print(len(res))
	U=U|res
	# ~ print(len(U))
print("collecting done")
print(len(U))
lx=[]
ly=[]
lz=[]
for bx,by,bz,ex,ey,ez in U:
	lx.append(bx)
	lx.append(ex)
	ly.append(by)
	ly.append(ey)
	lz.append(bz)
	lz.append(ez)
lx=sorted(list(set(lx)))
ly=sorted(list(set(ly)))
lz=sorted(list(set(lz)))
res=0
ON=set()
mx=len(U)
for iq,quad  in enumerate(U):
	bx,by,bz,ex,ey,ez=quad
	print(f"\r{iq+1}/{mx}",quad,end="")
	for cx,cex in zip(lx,lx[1:]):
		if bx<=cx<cex<=ex+1:
			for cy,cey in zip(ly,ly[1:]):
				if by<=cy<cey<=ey+1:
					for cz,cez in zip(lz,lz[1:]):
						if bz<=cz<cez<=ez+1:
							ON.add((cx,cy,cz,cex,cey,cez))
							# ~ res+=(ex-bx)*(ey-by)*(ez-cz)
							# ~ res+=(cex-cx)*(cey-cy)*(cez-cz)
						
res=0
# ~ for ON in UNIQ:
# ~ print(ON)
for cx,cy,cz,cex,cey,cez in ON:
	res+=(cex-cx)*(cey-cy)*(cez-cz)
repres (2,res)
print('expected 39769202357779 p0 ok')
