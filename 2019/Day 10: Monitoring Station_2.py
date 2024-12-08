#!/usr/bin/env python
# -*- coding: utf-8 -*-
fn,part="d10.txt",3
sep="\n\n"
data=open(fn).read().split(sep)[part].splitlines()
R=[]
for r,line in enumerate(data):
	for c,s in enumerate(line):
		if s=="#":R.append((r,c))
print(len(R))
def pgcd(a,b):
	while b:a,b=b,a%b
	return abs(a)
record=0
for rock in R:
	D=set()
	for target in R:
		if rock==target:continue
		dr=target[0]-rock[0]
		dc=target[1]-rock[1]
		f=pgcd(dr,dc)
		dr/=f
		dc/=f
		D.add((dr,dc))
	visible=len(D)
	if visible>record:
		record=visible
		print(visible,rock)
		bestset=D.copy()
		startrock=rock
# ~ print(bestset)
from math import atan2,pi
class V():
	def __init__(self,coord):
		r,c=coord
		self.coord=coord
		self.x,self.y=c,-r
		self.alpha=atan2(c,-r)
		if self.alpha<0:self.alpha+=2*pi
	def __lt__(self,other):
		# ~ print(f"comparing{self} to {other}")
		if self.alpha-other.alpha<0:return True
		return False
		# ~ return other.alpha-self.alpha
	def __str__(self):
		return f"({self.coord}:{self.x},{self.y})  : {self.alpha}"
print(startrock)
LV=[V(t) for t in bestset]
LV=sorted(LV)
print(startrock+LV[199].coord)
print(100*(startrock[1]+LV[199].coord[1])+startrock[0]+LV[199].coord[0])
