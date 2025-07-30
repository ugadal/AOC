#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
fe="exp18.txt"
fr="d18.txt"
from shapely.geometry import Polygon
import re
R=(0,1)
D=(1,0)
U=(-1,0)
L=(0,-1)
DD={}
for s,k in zip([0,1,3,2],(R,D,U,L)):	DD[s]=k
class grid():
	def __init__(self,fn):
		self.moves=[]
		for l in open(fn).read().splitlines():
			d,s,cc=l.split()
			s=int(cc[2:7],16)
			d=int(cc[7])
			self.moves.append((d,int(s)))
	def go(self):
		r=c=0
		coord=[(r,c)]
		for d,s in self.moves:
			dr,dc=DD[d]
			r+=s*dr
			c+=s*dc
			coord.append((r,c))
		coord.append((0,0))
		pol=Polygon(coord)
		print(pol.area+pol.length/2+1)
G=grid(fr)
G.go()
