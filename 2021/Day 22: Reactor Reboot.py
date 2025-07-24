#!/usr/bin/env python
# -*- coding: utf-8 -*-
part=1
def repres(p,v):print(f"p{p}: {v}")
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
for x,ex in zip(lx,lx[1:]):
	for y,ey in zip(ly,ly[1:]):
		for z,ez in zip(lz,lz[1:]):
			cube(x,y,z,ex,ey,ez)
print(len(cube.a))
for line in block.splitlines():
	print("\r",line,end="")
	st,coord=line.split()
	st=True if st=="on" else False
	rx,ry,rz=coord.split(",")
	V=[tuple(map(int,(r[2:].split("..")))) for r in coord.split(",")]
	(bx,ex),(by,ey),(bz,ez)=V
	for c in cube.a:
		# ~ c.rep()
		# ~ print(c.x,c.ex,bx,ex)
		if bx<=c.x<c.ex<=ex+1:
			if by<=c.y<c.ey<=ey+1:
				if bz<=c.z<c.ez<=ez+1:
					# ~ print("ok")
					c.status=st
	# ~ break
repres (2,sum(c.v for c in cube.a if c.status))
