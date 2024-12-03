#!/usr/bin/env python
# -*- coding: utf-8 -*-
G={}
winds=list("<>^v")
WF=[]
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
start=(0,next(c for c in range(NC) if G[0,c]=="."))
end=(row,next(c for c in range(NC) if G[row,c]=="."))
for k,v in G.items():
	if v not in winds:continue
	WF.append(windgen(k,v))
walls=set([k for k,v in G.items() if v=="#"])
def nxt(pos):
	r,c=pos
	Avail=[]
	if 0<=c-1 :	Avail.append((r,c-1))
	if 0<=r-1 :	Avail.append((r-1,c))
	if r+1<=NR:	Avail.append((r+1,c))
	if c+1<=NC:	Avail.append((r,c+1))
	Avail.append(pos)		
	for x in Avail:yield x
def go(start,goal):
	Q=[(start)]
	z=0
	while True:
		nxtQ=[]
		z+=1
		while Q:
			q=Q.pop()
			t,pos=q
			for np in nxt(q):
				tpos=np
				if tpos==goal:
					currbest=z
					return z
				nxtQ.append(np)
		WPS=set([fun((cb+z)) for fun in WF])
		Q=set(nxtQ)-walls-WPS
		Q=list(Q)
cb=0
cb=go(start,end)
cb+=go(end,start)
cb+=go(start,end)
print(cb)
