#!/usr/bin/env python
# -*- coding: utf-8 -*-
fn="d6.txt"
inp=open(fn).read().split("\n\n")[1].splitlines()
G={}
ch=ord("A")-1
for line in inp:
	ch+=1
	c,r=map(int,line.split(","))
	G[r,c]=chr(ch)
print (G)
tr=min([r for r,c in G.keys()])
br=max([r for r,c in G.keys()])
lc=min([c for r,c in G.keys()])
rc=max([c for r,c in G.keys()])
print (tr,br,lc,rc)
M=[]
for r in range(tr-1,br+2):
	rt=[]
	for c in range(lc-1,rc+2):
		sd=sum([abs(r-pr)+abs(c-pc) for pr,pc in G.keys()])
		if sd<10000:rt.append("#")
		else:rt.append(".")
	M.append("".join(rt))
for r in M:print(r)
M="".join(M)
print(M.count("#"))
