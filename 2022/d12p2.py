#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tqdm import trange
from collections import deque
dirs={
	"U":(0,-1),
	"D":(0,1),
	"R":(1,0),
	"L":(-1,0)}
exp="""
Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""
inf=float("Inf")
# ~ G=[[ord (c) for c in row] for row in exp.splitlines()[1:]]
G=[[ord (c) for c in row] for row in open("d12.txt").read().splitlines()]
NR=len(G)
NC=len(G[0])
er,ec=next((ir,ic) for ir,row in enumerate(G) for ic,c in enumerate(row) if c==ord("E") )
sr,sc=next((ir,ic) for ir,row in enumerate(G) for ic,c in enumerate(row) if c==ord("S") )
print(er,ec)
print(sr,sc)
G[er][ec]=ord("z")
D=[[inf for c in range(NC)] for r in range(NR) ]
G[sr][sc]=ord("a")
D[er][ec]=0

# ~ BFS
seen={(er,ec)}
Q=[(er,ec)]
while Q:
	t=Q.pop(0)
	cr,cc=t
	if G[cr][cc]==ord("a"):
		print(D[cr][cc])
		exit()
	cv=G[cr][cc]
	cd=D[cr][cc]
	
	for dr,dc in dirs.values():
		nr=cr+dr
		nc=cc+dc
		if 0<=nr<NR and 0<=nc<NC and G[nr][nc]>=cv-1 and (nr,nc) not in seen:
			D[nr][nc]=min(D[nr][nc],cd+1)
			seen.add((nr,nc))
			Q.append((nr,nc))

# ~ dijkstra
# ~ seen=set()
# ~ Q=[(sr,sc)]
# ~ def bla(t):
	# ~ r,c=t
	# ~ return D[r][c]
# ~ while Q:
	# ~ Q=sorted(Q,key=bla)
	# ~ t=Q.pop(0)
	# ~ if t==(er,ec):
		# ~ print(t,D[er][ec])
		# ~ exit()
	# ~ cr,cc=t
	# ~ cv=G[cr][cc]
	# ~ cd=D[cr][cc]
	# ~ for dr,dc in dirs.values():
		# ~ nr=cr+dr
		# ~ nc=cc+dc
		# ~ if 0<=nr<NR and 0<=nc<NC and G[nr][nc]<=cv+1 and (nr,nc) not in seen:
			# ~ if (nr,nc) not in Q:Q.append((nr,nc))
			# ~ D[nr][nc]=min(D[nr][nc],cd+1)
	# ~ seen.add((cr,cc))
# ~ print (D[er][ec])
