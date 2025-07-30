#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
from copy import deepcopy as dcp
fe="exp21.txt"
fr="d21.txt"
G=[[ch for ch in line] for line in open(fr).read().splitlines()]
NR=len(G)
NC=len(G[0])
sr=0
for r,row in enumerate(G):
	if row.count("S"):
		sr,sc=r,row.index("S")
		break
print(sr,sc)
G[sr][sc]="."
# ~ global DG
DG={}
totreat=[]
nxt=[]
def myget(x,y):
	if (x,y) in DG:return DG[x,y]
	else:return grid(x,y)
def tog():
	while True:
		yield "0"
		yield "1"
class grid(object):
	def __init__(self,x,y):
		# ~ print(f"creating grid {x},{y} at step {step}")
		self.x=x
		self.y=y
		self.G=[]
		self.full=False
		for row in G:self.G.append(dcp(row))
		DG[(x,y)]=self
		# ~ print(DG.keys())
		# ~ print(DG.values())
		self.cz=0
		self.co=0
	def __str__(s):return f"grid {s.x},{s.y}"
	def toggle(s,r,c,status):
		if s.G[r][c]==".":
			s.G[r][c]=status
			s.cou()
			return True #toggled
		return False
	def rep(s):
		print(s,f"even: {s.cz}, odd: {s.co}")
		# ~ for row in s.G:print("".join(row))
	def cou(s):
		if not s.full:
			s.cz=sum([row.count("0") for row in s.G])
			s.co=sum([row.count("1") for row in s.G])
			if s.cz+s.co==7457+7520:
				s.full=True
				# ~ print (f"{s} filled at step {step} {s.cz} {s.co}")
	def prop(s,r,c):
		# ~ North
		if r==0:
			northG=myget(s.x,s.y+1)
			if northG.toggle(NR-1,c,curr):nxt.append((northG,NR-1,c))
		else:
			if s.toggle(r-1,c,curr):nxt.append((s,r-1,c))
			# ~ print("after north",nxt)
		# ~ South
		if r==NR-1:
			southG=myget(s.x,s.y-1)
			if southG.toggle(0,c,curr):nxt.append((southG,0,c))
		else:
			if s.toggle(r+1,c,curr):nxt.append((s,r+1,c))
		# ~ East
		if c==NC-1:
			eastG=myget(s.x+1,s.y)
			if eastG.toggle(r,0,curr):nxt.append((eastG,r,0))
		else:
			if s.toggle(r,c+1,curr):nxt.append((s,r,c+1))
		# ~ West
		if c==0:
			westG=myget(s.x-1,s.y)
			if westG.toggle(r,NC-1,curr):nxt.append((westG,r,NC-1))
		else:
			if s.toggle(r,c-1,curr):nxt.append((s,r,c-1))
					
step=0		
tgstat=tog()
curr=next(tgstat)
sg=grid(0,0)
sg.toggle(sr,sc,curr)
sg.rep()
curr=next(tgstat)
sg.prop(sr,sc)
while True:
	step+=1
	totreat=nxt
	nxt=[]
	curr=next(tgstat)
	while totreat:
		g,r,c=totreat.pop(0)
		g.prop(r,c)
	if (step-65)%262==0:
		obs=list([(g.cz,g.co) for g in DG.values()])
		TOG=set(obs)
		for tog in TOG:
			# ~ print(f"{step} {tog}, {obs.count(tog)}")
			print(f"{tog}, {obs.count(tog)}")
		input()
	
for g in DG.values():g.rep()
