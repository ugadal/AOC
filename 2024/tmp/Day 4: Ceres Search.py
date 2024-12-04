#!/usr/bin/env python
# -*- coding: utf-8 -*-
fn,part="d4.txt",0
G=open(fn).read().split("\n\n")[part].splitlines()
NR=len(G)
NC=len(G[0])
border="."*(NC+6)
NG=[border,border,border]
for line in G:NG.append("..."+line+"...")
for x in range(3):NG.append(border)
G=NG
def valid(pos,dirs):
	r,c=pos
	dr,dc=dirs
	for (a,b),s in zip([(r+k*dr,c+k*dc) for k in range(1,4)],"MAS"):
		if G[a][b]!=s:return False
	return True
for l in G:print(l)
import itertools as it
dirs=list(it.product((-1,1,0),repeat=2))[:-1]
res=0
for row in range(3,NR+3):
	for col in range(3,NC+3):
		if G[row][col]!="X":continue
		pos=(row,col)
		for d in dirs:
			if valid(pos,d):res+=1
print(res)
dirs=[a+b for a,b in it.product((-1,1,0),(-1j,1j,0))][:-1]
for d in dirs:print(d)
G={}
for r,line in enumerate(open(fn).read().split("\n\n")[part].splitlines()):
	for c,s in enumerate(line):
		G[c+r*1j]=s
NR,NC=r+1,c+1
print(NR,NC)
