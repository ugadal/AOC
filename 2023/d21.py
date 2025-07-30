#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
from copy import deepcopy as dcp
fe="exp21.txt"
fr="d21.txt"
offsets=[(1,0),(-1,0),(0,1),(0,-1)]
G=[[ch for ch in line] for line in open(fr).read().splitlines()]
NR=len(G)
NC=len(G[0])
for l in G:print(l)
sr=0
for r,row in enumerate(G):
	if row.count("S"):
		sr,sc=r,row.index("S")
		break
print(sr,sc)
G[sr][sc]=True
totreat=[(sr,sc)]
odd=True
# ~ for l in G:print(l)
for s in range(64):
	nxtbatch=[]
	odd=not odd
	for (r,c) in totreat:
		for (dr,dc) in offsets:
			if 0<=r+dr<NR and 0<=c+dc<NC:
				if G[r+dr][c+dc]==".":
					G[r+dr][c+dc]=odd
					nxtbatch.append((r+dr,c+dc))
	totreat=dcp(nxtbatch)
for l in G:print(l)		
ttl=0
for row in G:ttl+=row.count(True)
print(ttl)
