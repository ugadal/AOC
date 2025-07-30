#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
from copy import deepcopy as dcp
import numpy as np
fe="exp22.txt"
fr="d22.txt"
Rocks=[]
for l in open(fr).read().splitlines():
	a,b=l.split("~")
	ax,ay,az=map(int,a.split(","))
	bx,by,bz=map(int,b.split(","))
	Rocks.append((ax,ay,az,bx,by,bz))
for rock in Rocks:
	print(rock)
	ax,ay,az,bx,by,bz=rock
	if ax>bx or ay>by or az>bz:
		print(rock,' !!!')
		input()
def getgridim():
	minx=min([min(ax,bx) for ax,_,_,bx,_,_ in Rocks])
	maxx=max([max(ax,bx) for ax,_,_,bx,_,_ in Rocks])
	miny=min([min(ay,by) for _,ay,_,_,by,_ in Rocks])
	maxy=max([max(ay,by) for _,ay,_,_,by,_ in Rocks])
	minz=min([min(az,bz) for _,_,az,_,_,bz in Rocks])
	maxz=max([max(az,bz) for _,_,az,_,_,bz in Rocks])
	return (minx,maxx,miny,maxy,minz,maxz)
def fill():
	# ~ print("dims:",getgridim())
	minx,maxx,miny,maxy,minz,maxz=getgridim()
	G=np.zeros((maxx+1,maxy+1,maxz+1))
	# ~ print(G)
	for ri,rock in enumerate(Rocks):
		ax,ay,az,bx,by,bz=rock
		for x in range(ax,bx+1):
			for y in range(ay,by+1):
				for z in range(az,bz+1):
					# ~ print(x,y,z,rock)
					G[x,y,z]=ri+1
	# ~ print(G)
	return G
G=fill()
print(G)
def canfall(rock):
	# ~ print ("checking rock",rock)
	ax,ay,az,bx,by,bz=rock
	if min(az,bz)==1:return False
	base=min(az,bz)
	delta=1
	if (ax==bx and ay==by and az==bz) or az!=bz:
		delta=1
		while not G[ax,ay,az-delta] and az-delta>=1:delta+=1
		return delta-1
	if ax!=bx:
		# ~ print("extending toward X")
		C=list([(x,ay,az-delta) for x in range(ax,bx+1)])
		while all([G[x,y,z]==0 for x,y,z in C]) and az-delta>=1:
			delta+=1
			C=list([(x,ay,az-delta) for x in range(ax,bx+1)])
		return delta-1
	if ay!=by:
		# ~ print("extending toward Y")
		C=list([(ax,y,az-delta) for y in range(ay,by+1)])
		while all([G[x,y,z]==0 for x,y,z in C]) and az-delta>=1:
			delta+=1
			C=list([(ax,y,az-delta) for y in range(ay,by+1)])
		return delta -1
def under(rock):
	ax,ay,az,bx,by,bz=rock
	if min(az,bz)==1:return set()
	if (ax==bx and ay==by and az==bz) or az!=bz:C=[[ax,ay,az-1]]
	if ax!=bx:C=list([(x,ay,az-1) for x in range(ax,bx+1)])
	if ay!=by:C=list([(ax,y,az-1) for y in range(ay,by+1)])
	return set([int(G[x,y,z]) for x,y,z in C if G[x,y,z]])
def above(rock):
	ax,ay,az,bx,by,bz=rock
	top=max(az,bz)
	if top+1>=len(G[0][0]):return set()
	if (ax==bx and ay==by and az==bz) or az!=bz:
		rab=int(G[ax,ay,top+1])
		if not rab:return set()
		return set([rab])
	if ax!=bx:C=list([(x,ay,az+1) for x in range(ax,bx+1)])
	if ay!=by:C=list([(ax,y,az+1) for y in range(ay,by+1)])
	# ~ print(C)
	return set([int(G[x,y,z]) for x,y,z in C if G[x,y,z]])
def safetorem(rock):
	ax,ay,az,bx,by,bz=rock
	rabove=above(rock)
	if not rabove:return True
	for ra in rabove:
		if len(under(Rocks[ra-1]))==1:return False
	return True
MEM={}
def makesfall(ir,fallen=set()):
	# ~ print("entry",ir,fallen)
	rock=Rocks[ir-1]
	rab=above(rock) #blocks above
	if not rab:
		# ~ print("none above")
		return set([ir])
	# ~ print("rab",rab)
	#rocks under rocks above
	SUPP=list([under(Rocks[x-1]) for x in rab])
	# ~ print("Supp",SUPP)
	
	#minus rocks fallen
	# ~ print("---"*indent,[len(list([x for x in supp if x-1 not in fallen])) for supp in SUPP])
	falls=[len(list([x for x in supp if x not in fallen|set([ir])]))==0 for supp in SUPP]
	# ~ print("falls",falls)
	newfallen=list([sr for sr,supp in zip(rab,falls) if supp])
	# ~ print("---"*indent,"new fallen",newfallen)
	nfndx=[x-1 for x in newfallen]
	nfndxset=set(nfndx)
	nfndxset=set(newfallen)
	# ~ print("nfndx",nfndx)
	
	v=set([ir])
	for supp in newfallen:
		for zz in makesfall(supp,fallen|nfndxset|set([ir])):
			v.add(zz)
			# ~ print("v",v,ir)
	return v
	
while True:
	G=fill()
	for ri,rock in enumerate(Rocks):
		if not canfall(rock):continue
		print(rock,ri,"falls")
		ax,ay,az,bx,by,bz=rock
		delta=canfall(rock)
		Rocks[ri]=(ax,ay,az-delta,bx,by,bz-delta)
		# ~ print(Rocks)
		break
	else:break
print(G)
DOR={}
class crock():
	def __init__(self,i,r):
		ax,ay,az,bx,by,bz=r
		self.r=r
		self.i=i
		self.ax=ax
		self.ay=ay
		self.az=az
		self.bx=bx
		self.by=by
		self.bz=bz
		self.above=set()
		self.under=set()
		self.status=True
		DOR[i]=self
	def toggle(self):
		self.status=not self.status
	def blows(self):
		if self.az==1:return False
		if not self.status:return False
		if sum([un.status for un in self.under]):return False
		self.status=False
		return True
		
		
print ([safetorem(rock) for rock in Rocks].count(True))
for ir,rock in enumerate(Rocks):crock(ir+1,rock)
for rock in DOR.values():
	AB=above(rock.r)
	UN=under(rock.r)
	print(rock.i,AB,UN)
	for ab in AB:
		rock.above.add(DOR[ab])
		DOR[ab].under.add(rock)
	for un in UN:
		rock.under.add(DOR[un])
		DOR[un].above.add(rock)
rock=DOR[7]
rock.toggle()
total=0
for rock in DOR.values():
	for r in DOR.values():r.status=True
	rock.toggle()
	while True:
		for r in DOR.values():
			if r==rock:continue
			if not r.blows():continue
			break
		else:break
	v=[r.status for r in DOR.values()].count(False)-1
	print (rock.i,v)
	total+=v
print (total)


