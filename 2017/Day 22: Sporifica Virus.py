#!/usr/bin/env python
# -*- coding: utf-8 -*-
inf=open("d22.txt").read().split("\n\n")[1].splitlines()
G={}
for r,row in enumerate(inf):
	for c,sym in enumerate(row):
		if sym=="#":G[r,c]=True
nr=1+(r)//2
nc=(1+len(row))//2
cpos=nr-1,nc-1
dr,dc=-1,0 # UP
def pmp(G):
	tr=min([a for a,b in G.keys()])
	br=max([a for a,b in G.keys()])
	lc=min([b for a,b in G.keys()])
	rc=max([b for a,b in G.keys()])
	for r in range(tr,br+1):
		print("".join(["#" if (r,c) in G else "." for c in range(lc,rc+1)]))
	print("============")
pmp(G)
print(cpos,dr,dc,cpos in G)
pmp(G)
inf=0
for x in range (10000):
	if cpos in G:
		G.pop(cpos)
		dr,dc=dc,-dr
	else:
		G[cpos]=True
		dr,dc=-dc,dr
		inf+=1
	cpos=cpos[0]+dr,cpos[1]+dc
	print(cpos,dr,dc,cpos in G)
pmp(G)
print(f"Infection {inf}")
