#!/usr/bin/env python
# -*- coding: utf-8 -*-
part=2
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
for line in block.splitlines():
	st,coord=line.split()
	st=True if st=="on" else False
	rx,ry,rz=coord.split(",")
	V=[tuple(map(int,(r[2:].split("..")))) for r in coord.split(",")]
	skip=any(b>50 or a<-50	for a,b in V)
	# ~ print(V,skip)
	if skip:continue
	for p in ((x,y,z) for x in range(V[0][0],V[0][1]+1) for y in range(V[1][0],V[1][1]+1) for z in range(V[2][0],V[2][1]+1)):
		G[p]=st
repres(1,list(G.values()).count(True))
lx=[]
ly=[]
lz=[]
class cube():
	a=[]
	def __init__(self,x,y,z,ex,ey,ez):
		self.x=x
		self.y=y
		self.z=z
		self.ex=ex
		self.ey=ey
		self.ez=ez
		self.v=(ex-x)*(ey-y)*(ez-z)
		cube.a.append(self)
		self.status=False
	def rep(self):
		print(self.x,self.ex,self.y,self.ez,self.z,self.ez,self.v,self.status)
for line in block.splitlines():
	st,coord=line.split()
	rx,ry,rz=coord.split(",")
	V=[tuple(map(int,(r[2:].split("..")))) for r in coord.split(",")]
	lx.append(V[0][0])
	lx.append(V[0][1]+1)
	ly.append(V[1][0])
	ly.append(V[1][1]+1)
	lz.append(V[2][0])
	lz.append(V[2][1]+1)
lx=sorted(list(set(lx)))
ly=sorted(list(set(ly)))
lz=sorted(list(set(lz)))
# ~ print(lx,ly,lz)
# ~ for x,ex in zip(lx,lx[1:]):
	# ~ for y,ey in zip(ly,ly[1:]):
		# ~ for z,ez in zip(lz,lz[1:]):
			# ~ cube(x,y,z,ex,ey,ez)
# ~ print(len(cube.a))
ON=[]
mx=len(block.splitlines())
UNIQ=[]
for lix,line in enumerate(block.splitlines()):
	print(lix,"/",mx,line)
	ON=[]
	st,coord=line.split()
	st=True if st=="on" else False
	if not st:continue
	rx,ry,rz=coord.split(",")
	V=[tuple(map(int,(r[2:].split("..")))) for r in coord.split(",")]
	(bx,ex),(by,ey),(bz,ez)=V
	# ~ if st:
	for cx,cex in zip(lx,lx[1:]):
		if bx<=cx<cex<=ex+1:
			for cy,cey in zip(ly,ly[1:]):
				if by<=cy<cey<=ey+1:
					for cz,cez in zip(lz,lz[1:]):
						if bz<=cz<cez<=ez+1:
							ON.append((cx,cy,cz,cex,cey,cez))
		ON=list(set(ON))
	for offline in block.splitlines()[lix+1:]:
		st,coord=offline.split()
		st=True if st=="on" else False
		if st:continue
		V=[tuple(map(int,(r[2:].split("..")))) for r in coord.split(",")]
		(bx,ex),(by,ey),(bz,ez)=V
		toremove=[]
		for cx,cy,cz,cex,cey,cez in ON:
			if bx<=cx<cex<=ex+1:
				if by<=cy<cey<=ey+1:
					if bz<=cz<cez<=ez+1:
						toremove.append((cx,cy,cz,cex,cey,cez))
		ON=set(ON)-set(toremove)
	for uniq in UNIQ:
		ON=ON-uniq
	UNIQ.append(ON)
		# ~ ON=[x for x in ON if not x in toremove]
	print("\r-",len(ON),"-",end="")
	# ~ break
res=0
for ON in UNIQ:
	for cx,cy,cz,cex,cey,cez in ON:
		res+=(cex-cx)*(cey-cy)*(cez-cz)
repres (2,res)
