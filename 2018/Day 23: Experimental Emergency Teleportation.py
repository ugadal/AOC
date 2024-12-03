#!/usr/bin/env python
# -*- coding: utf-8 -*-
fn,part="d23.txt",1
from random import choice
from random import randrange
from collections import deque
data=open(fn).read().split("\n\n")[part].splitlines()
def calcd(ba,bb):
	return abs(ba.x-bb.x)+abs(ba.y-bb.y)+abs(ba.z-bb.z)
D=[(-1,-1,-1),(-1,-1,0),(-1,0,-1),(0,-1,-1),(0,0,-1),(0,-1,0),(-1,0,0)]
class bot():
	def __init__(self,x,y,z,r):
		self.x=x
		self.y=y
		self.z=z
		self.r=r
		self.ir=0
		self.hd=0
	def irof(self,allbots):
		v=0
		for b in allbots:
			if calcd(self,b)<=b.r:v+=1
		self.ir=v
	def __str__(self):
		return f"bot at {self.x},{self.y},{self.z} radius {self.r}"
	def neighbors(self):
		N=[bot(self.x+dx,self.y+dy,self.z+dz,self.r) for dx,dy,dz in D]
		for n in N:n.hd=calcd(n,origin)
		return N
		
extr=[]
origin=bot(0,0,0,-1)
for line in data:
	a,b=line[5:].split(">, ")
	x,y,z=map(int,a.split(","))
	r=int(b.split("=")[1])
	extr.append((x,y,z,r))
Bots=[bot(x,y,z,r) for x,y,z,r in extr]
mr=max(b.r for b in Bots)
print(mr)
sb=next(b for b in Bots if b.r==mr)
print(sb)
inrange=0
for b in Bots:
	if calcd(sb,b)<=mr:inrange+=1
print("in range",inrange)
minx=min(b.x for b in Bots)
miny=min(b.y for b in Bots)
minz=min(b.z for b in Bots)
maxx=max(b.x for b in Bots)
maxy=max(b.y for b in Bots)
maxz=max(b.z for b in Bots)
rx=(minx,maxx+1)
ry=(miny,maxy+1)
rz=(minz,maxz+1)
print ("x:",minx,maxx,maxx-minx,rx)
print ("y:",miny,maxy,maxy-miny,ry)
print ("z:",minz,maxz,maxz-minz,rz)
         # ~ "pos=<10,10,10>, r=5"
spot=bot(0,0,0,-1)
print("spot:",spot)
for b in Bots:b.irof(Bots)
maxir=max(b.ir for b in Bots)
for b in [b for b in Bots if b.ir==maxir]:
	print(b,b.ir)
rec=-1
print(rec,spot)
while True:
	spot.x=randrange(*rx)
	spot.y=randrange(*ry)
	spot.z=randrange(*rz)
	spot.irof(Bots)
	if spot.ir>=rec:
		rec=spot.ir
		print(rec,spot,calcd(origin,spot))
# ~ 873 bot at 25919282,21565048,32174536 radius -1 79658866 random found
# ~ 873 bot at 25585752,21488509,32428867 radius -1 79503128
rec=873
spot=bot( 25091704,20994461,31934819,-1)
spot=bot( 25091702,20994458,31934817,-1)
print(spot,calcd(spot,origin))
# ~ N=spot.neighbors()
# ~ for n in N:n.irof(Bots)
# ~ for n in N:print(n,n.ir,n.hd)
while True:
	nspot=bot(spot.x-1,spot.y-1,spot.z-1,spot.r)
	nspot.irof(Bots)
	if nspot.ir<spot.ir:break
	spot=nspot
	print(spot,spot.ir,calcd(spot,origin))
N=spot.neighbors()
print("---")
for n in N:n.irof(Bots)
for n in N:print(n,n.ir,n.hd)
N=[n for n in N if n.ir>=spot.ir]
print("---")
for n in N:print(n,n.ir,n.hd)
for spot in N:
	print("=====")
	while True:
		nspot=bot(spot.x-1,spot.y-1,spot.z-1,spot.r)
		nspot.irof(Bots)
		if nspot.ir<spot.ir:break
		spot=nspot
		print(spot,spot.ir,calcd(spot,origin))
print(spot,spot.ir,calcd(spot,origin))
