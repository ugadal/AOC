#!/usr/bin/env python
# -*- coding: utf-8 -*-
part=0
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
	# ~ rx,ry,rz=coord.split(",")
	V=[tuple(map(int,(r[2:].split("..")))) for r in coord.split(",")]
	(bx,ex),(by,ey),(bz,ez)=V
	I.append((st,bx,ex,by,ey,bz,ez))
	skip=any(b>50 or a<-50	for a,b in V)
	# ~ print(V,skip)
	if skip:continue
	for p in ((x,y,z) for x in range(V[0][0],V[0][1]+1) for y in range(V[1][0],V[1][1]+1) for z in range(V[2][0],V[2][1]+1)):
		G[p]=st
repres(1,list(G.values()).count(True))
def ana(TI):
	lx=[]
	ly=[]
	lz=[]
	for st,bx,ex,by,ey,bz,ez in TI:
		lx.append(bx)
		lx.append(ex)
		ly.append(by)
		ly.append(ey)
		lz.append(bz)
		lz.append(ez)
	lx=sorted(list(set(lx)))
	ly=sorted(list(set(ly)))
	lz=sorted(list(set(lz)))
	ON=[]
	st,bx,ex,by,ey,bz,ez=TI[0]
	for cx,cex in zip(lx,lx[1:]):
		if bx<=cx<cex<=ex+1:
			for cy,cey in zip(ly,ly[1:]):
				if by<=cy<cey<=ey+1:
					for cz,cez in zip(lz,lz[1:]):
						if bz<=cz<cez<=ez+1:
							ON.append((cx,cy,cz,cex,cey,cez))
	ON=set(ON)
	for st,bx,ex,by,ey,bz,ez in TI[1:]:
		toremove=[]
		for cx,cy,cz,cex,cey,cez in ON:
			if bx<=cx<cex<=ex+1:
				if by<=cy<cey<=ey+1:
					if bz<=cz<cez<=ez+1:
						toremove.append((cx,cy,cz,cex,cey,cez))
		ON=ON-set(toremove)
	return ON
for ix,quad in enumerate(I):
	st,bx,ex,by,ey,bz,ez=quad
	Z=[quad]
	Z.extend(q for q in I[ix+1:] if not q[0])
	res=ana(Z)
	print(len(res))

# ~ res=0
# ~ for ON in UNIQ:
	# ~ for cx,cy,cz,cex,cey,cez in ON:
		# ~ res+=(cex-cx)*(cey-cy)*(cez-cz)
# ~ repres (2,res)
