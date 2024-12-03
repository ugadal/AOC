#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ~ import sympy
import sys
from random import shuffle as shf
day=sys.argv[0].split(".")[0][1:]
exp=f"exp{day}.txt"
real=f"d{day}.txt"
G={}
winds=list("<>^v")
WF=[]
def pgcd(a,b):
	while b:a,b=b,a%b
	return a
def windgen(pos,s):
	if s=="<":d=(0,-1)
	if s==">":d=(0,1)
	if s=="^":d=(-1,0)
	if s=="v":d=(1,0)
	r,c=pos
	dr,dc=d
	def fun(t):
		nr=(r+t*dr)%(NR-1) or NR-1
		nc=(c+t*dc)%(NC-1) or NC-1
		return (nr,nc)
	return fun
	
for row,line in enumerate(open(0).read().splitlines()):
	for col,c in enumerate(line):
		G[row,col]=c
NR=row
NC=col
print(NR,NC)
modtime=int((NR-1)*(NC-1)/pgcd(NR-1,NC-1))
print (modtime)
start=(0,next(c for c in range(NC) if G[0,c]=="."))
end=(row,next(c for c in range(NC) if G[row,c]=="."))
print (start,end)
assert [fun(0) for fun in WF]==[fun(modtime) for fun in WF]
assert [fun(1) for fun in WF]==[fun(modtime+1) for fun in WF]
for k,v in G.items():
	if v not in winds:continue
	WF.append(windgen(k,v))
K={}
walls=set([k for k,v in G.items() if v=="#"])
def nxt(t,pos):
	WP=[fun((cb+t+1)) for fun in WF]
	r,c=pos
	Avail=[]
	if 0<=c-1 and G[r,c-1]!="#" and (r,c-1) not in WP:
		Avail.append((t+1,(r,c-1)))
	if 0<=r-1 and G[r-1,c]!="#" and (r-1,c) not in WP:
		Avail.append((t+1,(r-1,c)))
	if pos not in WP:Avail.append((t+1,pos))		
	if r+1<=NR and G[r+1,c]!="#" and (r+1,c) not in WP:
		Avail.append((t+1,(r+1,c)))
	if c+1<=NC and G[r,c+1]!="#" and (r,c+1) not in WP:
		Avail.append((t+1,(r,c+1)))
	if not Avail and pos not in WP:Avail.append((t+1,pos))		
	for x in Avail:yield x
# ~ Q=[(0,start)]
def hamd(a,b):
	ax,ay=a
	bx,by=b
	return abs(ax-bx)+abs(ay-by)
# ~ currbest=float("Inf")
p=10000
# ~ z=0
def go(start,goal):
	Q=[(0,start)]
	z=0
	while True:
		nxtQ=set()
		z+=1
		while Q:
			q=Q.pop()
			t,pos=q
			for np in nxt(t,pos):
				tt,tpos=np
				if tpos==goal:
					currbest=tt
					print (f"curr {currbest}")
					return tt
				nxtQ.add(np)
		Q=list(nxtQ)
		print (z,len(Q))
cb=0
cb=go(start,end)
# ~ exit()
cb+=go(end,start)
cb+=go(start,end)
print(cb)
