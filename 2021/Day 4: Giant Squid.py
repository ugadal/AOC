#!/usr/bin/env python
# -*- coding: utf-8 -*-
part=1
import re
import sys
import itertools as it
from functools import cache
import uuid
cp=str(sys.argv[0])
dre=re.compile(r"^Day (\d+):")
day=dre.findall(cp)[0]
fn=f"d{day}.txt"
block=open(fn).read().split("\n\n\n")[part]
tirage,*grids=block.split("\n\n")
tirage=tirage.split(",")
B=[]
for board in grids:
	B.append([row.split() for row in board.splitlines()])
B=[[row.split() for row in board.splitlines()] for board in grids]
def valid (board,tir):
	for row in board:
		if all(v in tir for v in row):return True
	for row in zip(*board):
		if all(v in tir for v in row):return True
	return False
pos=5
while True:
	V=list(valid(board,tirage[:pos]) for board in B)
	if any(V):
		# ~ print(pos,tirage[pos-1],next(v for v in V if v))
		lv=tirage[pos-1]
		gr=next(v for v in V if v)
		break
	pos+=1
for board in B:
	if valid(board,tirage[:pos]):
		V=[]
		for row in board:
			V.extend(row)
		V=[v for v in V if v not in tirage[:pos]]
		ttl=sum(int(v) for v in V)
		break
print("p1:",int(lv)*ttl)
pos=len(tirage)
while all (valid(board,tirage[:pos]) for board in B):pos-=1
# ~ print(pos,tirage [pos])
lwb=next(b for i,b in enumerate(B) if not valid(b,tirage[:pos]))
# ~ print(lwb)
V=[]
for row in lwb:	V.extend(row)
V=[v for v in V if v not in tirage[:pos+1]]
ttl=sum(int(v) for v in V)
print("p2:",ttl*int(tirage[pos]))
