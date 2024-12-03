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
		dmap={sym:abs(r-pr)+abs(c-pc) for (pr,pc),sym in G.items()}
		# ~ print(r,c,dmap)
		tag=min(dmap.values())
		if list(dmap.values()).count(tag)>1:sym="."
		else:sym=next(k for k in dmap.keys() if dmap[k]==tag)
		rt.append(sym)
	M.append("".join(rt))
for r in M:print(r)
torep=set(list(M[0]))
torep=torep | set([l[0] for l in M])
torep=torep | set([l[-1] for l in M])
torep=torep | set(list(M[-1]))
torep.remove(".")
print(torep)
NM=[]
for m in M:
	for s in torep:	m=m.replace(s,".")
	NM.append(m)
for r in NM:print(r)
S="".join(NM)
symbs=set(list(S))
symbs.remove(".")
print(max(S.count(s) for s in symbs))
