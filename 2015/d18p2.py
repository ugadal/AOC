#!/usr/bin/env python
# -*- coding: utf-8 -*-
G=[[True if c=="#" else False for c in line] for line in open("d18.txt").read().splitlines()]
nr=len(G)
nc=len(G[0])
around=[(dr,dc) for dr in (-1,0,1)	for dc in (-1,0,1)]
around.remove((0,0))
G[0][0]=True
G[nr-1][0]=True
G[0][nc-1]=True
G[nr-1][nc-1]=True
for t in range(100):
	NG=[[None]*nc for _ in range(nr)]
	for r in range(nr):
		for c in range(nc):
			alivearound=[G[r+dr][c+dc] for dr,dc in around if 0<=r+dr<nr and 0<=c+dc<nc].count(True)
			if G[r][c]:
				if 2<=alivearound<=3:nxtv=True
				else:nxtv=False
			elif alivearound==3:nxtv=True
			else:nxtv=False
			NG[r][c]=nxtv
	G=[]
	for row in NG:G.append(list(row))
	G[0][0]=True
	G[nr-1][0]=True
	G[0][nc-1]=True
	G[nr-1][nc-1]=True
print(sum([row.count(True) for row in G]))
