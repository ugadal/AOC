#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ~ fn,part="d22.txt",0
from collections import deque
depth= 3198
tx,ty=12,757
# ~ depth=510
# ~ tx,ty=10,10
GEOI={}
GEOI[0,0]=0
GEOI[tx,ty]=0
EL={}
def geoindex(x,y):
	if (x,y) in GEOI:return GEOI[x,y]
	if y==0:
		v=16807*x
		GEOI[x,y]=v
		return v
	if x==0:
		v=48271*y
		GEOI[x,y]=v
		return v
	return erosion(x-1,y)[0]*erosion(x,y-1)[0]
def erosion(x,y):
	if (x,y) in EL:return EL[x,y]
	el=depth+geoindex(x,y)
	el%=20183
	EL[x,y]=el,el%3
	return el,el%3
	# ~ if el%3==0:return "rocky"
	# ~ if el%3==1:return "wet"
	# ~ if el%3==2:return "narrow"
# ~ print(erosion(0,0))
# ~ print(erosion(0,1))
# ~ print(erosion(1,0))
# ~ print(erosion(1,1))
# ~ print(erosion(tx,ty))
# ~ print(erosion(tx,ty))
res=0
for x in range(tx+1):
	for y in range(ty+1):
		res+=erosion(x,y)[1]
print(res)
"""
equipped=none 0, torch 1 climb 2
rocky 	= mod0 = climb,torch 	ok none False
wet 	= mod1 = climb,none 	ok torch False
narrow 	= mod2 = torch,none 	OK climb False
"""
Visited={}
spos,t=(0,0,1),0
dirs=[(1,0),(0,1),(0,-1),(-1,0)]
cx,cy,ce=spos
t=0
TOVISIT=deque()
TOVISIT.append((0,0,1,0))
record=inf=float("inf")
done=0
while TOVISIT:
	done+=1
	cx,cy,ce,t=TOVISIT.popleft()
	if not done%100000:print(len(TOVISIT),cx,cy,ce,t)
	if t>=Visited.get((cx,cy,ce),inf):continue
	ct=erosion(cx,cy)[1]
	if t>record:continue
	if cx==tx and cy==ty:
		v=t
		v+=0 if ce==1 else 7
		if v<record:
			record=v
			print("record",record)
		continue
	for dx,dy in dirs:
		if cx+dx<0 or cy+dy<0:continue
		nx,ny=cx+dx,cy+dy
		nt=erosion(nx,ny)[1]
		if ct==nt:#same ground type
			TOVISIT.append((nx,ny,ce,t+1))
		elif ce in set([0,1,2])-set([nt]):
			TOVISIT.append((nx,ny,ce,t+1))
		# ~ swap eq
		r=set([0,1,2])-set([ct])-set([ce])
		TOVISIT.append((cx,cy,r.pop(),t+7))
	Visited[cx,cy,ce]=t
print(record)
