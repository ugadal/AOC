#!/usr/bin/env python
# -*- coding: utf-8 -*-
part=3
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
def isincluded(a,b):
	abx,aby,abz,aex,aey,aez=a
	bbx,bby,bbz,bex,bey,bez=b
	if bbx<=abx and aex<=bex:
		if bby<=aby and aey<=bey:
			if bbz<=abz and aez<=bez:return True
	return False
	
def nonoverlap(a,b):
	abx,aby,abz,aex,aey,aez=a
	bbx,bby,bbz,bex,bey,bez=b
	if aex<bbx or abx>bex:return True
	if aey<bby or aby>bey:return True
	if aez<bbz or abz>bez:return True
	return False
	
def addcube(Cubes,newcube):
	print("nc",newcube)
	torem=set()
	for c in Cubes:
		if isincluded(c,newcube[1:]):
			torem.add(c)
			# ~ print(f"removing {c} as fully included in {newcube}")
	Cubes-=torem
	print("cubes remaining:",len(Cubes))
	lx=[]
	ly=[]
	lz=[]
	ON=set()
	OV=set()
	for c in Cubes:
		if nonoverlap(c,newcube[1:]):ON.add(c)
		else:OV.add(c)
	for bx,by,bz,ex,ey,ez in list(OV)+[newcube[1:]]:
		lx.append(bx)
		lx.append(ex+1)
		ly.append(by)
		ly.append(ey+1)
		lz.append(bz)
		lz.append(ez+1)
	lx=sorted(list(set(lx)))
	ly=sorted(list(set(ly)))
	lz=sorted(list(set(lz)))
	for bx,by,bz,ex,ey,ez in list(OV)+[newcube[1:]]:
		pxr=[(cx,cex) for cx,cex in zip(lx,lx[1:]) if bx<=cx<cex<=ex+1]
		pyr=[(cy,cey) for cy,cey in zip(ly,ly[1:]) if by<=cy<cey<=ey+1]
		pzr=[(cz,cez) for cz,cez in zip(lz,lz[1:]) if bz<=cz<cez<=ez+1]
		for (cx,cex),(cy,cey),(cz,cez) in it.product(pxr,pyr,pzr):
			ON.add((cx,cy,cz,cex-1,cey-1,cez-1))
	print("lon",len(ON))
	return ON
def remcube(Cubes,newcube):
	print("nc",newcube)
	torem=set()
	for c in Cubes:
		if isincluded(c,newcube[1:]):
			torem.add(c)
			# ~ print(f"removing {c} as fully included in {newcube}")
	Cubes-=torem
	print("cubes remaining:",len(Cubes))
	lx=[]
	ly=[]
	lz=[]
	ON=set()
	OV=set()
	for c in Cubes:
		if nonoverlap(c,newcube[1:]):ON.add(c)
		else:OV.add(c)
	for bx,by,bz,ex,ey,ez in list(OV)+[newcube[1:]]:
		lx.append(bx)
		lx.append(ex+1)
		ly.append(by)
		ly.append(ey+1)
		lz.append(bz)
		lz.append(ez+1)
	lx=sorted(list(set(lx)))
	ly=sorted(list(set(ly)))
	lz=sorted(list(set(lz)))
	st,bx,by,bz,ex,ey,ez=newcube
	# ~ ON=set()
	for bx,by,bz,ex,ey,ez in list(OV):
		pxr=[(cx,cex) for cx,cex in zip(lx,lx[1:]) if bx<=cx<cex<=ex+1]
		pyr=[(cy,cey) for cy,cey in zip(ly,ly[1:]) if by<=cy<cey<=ey+1]
		pzr=[(cz,cez) for cz,cez in zip(lz,lz[1:]) if bz<=cz<cez<=ez+1]
		for (cx,cex),(cy,cey),(cz,cez) in it.product(pxr,pyr,pzr):
			ON.add((cx,cy,cz,cex-1,cey-1,cez-1))	
	torem=set()
	bx,by,bz,ex,ey,ez=newcube[1:]
	pxr=[(cx,cex) for cx,cex in zip(lx,lx[1:]) if bx<=cx<cex<=ex+1]
	pyr=[(cy,cey) for cy,cey in zip(ly,ly[1:]) if by<=cy<cey<=ey+1]
	pzr=[(cz,cez) for cz,cez in zip(lz,lz[1:]) if bz<=cz<cez<=ez+1]
	for (cx,cex),(cy,cey),(cz,cez) in it.product(pxr,pyr,pzr):
		torem.add((cx,cy,cz,cex-1,cey-1,cez-1))	
	ON-=torem
	print("lon",len(ON))
	return ON
C=set()
for il,cube in enumerate(I):
	st,bx,by,bz,ex,ey,ez=cube
	if st:C=addcube(C,cube)
	else:C=remcube(C,cube)
# ~ print(C)
res=0
for bx,by,bz,ex,ey,ez in C:
	res+=(1+ex-bx)*(1+ey-by)*(1+ez-bz)
repres(2,res)
