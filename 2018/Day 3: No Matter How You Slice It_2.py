#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ~ #1 @ 37,526: 17x23
G={}
bids=set()
for line in open("d3.txt").read().split("\n\n")[1].splitlines():
	bid,_,gpos,dim=line.split()
	bid=int(bid[1:])
	bids.add(bid)
	c,r=map(int,gpos[:-1].split(","))
	dc,dr=map(int,dim.split("x"))
	for row in range(r,r+dr):
		for col in range(c,c+dc):
			G[row,col]=G.get((row,col),[])
			G[row,col].append(bid)
			
mto=[k for k in G.values() if len(k)>1]
print(len(mto))
covered=set()
for k in mto:
	for b in k:
		covered.add(b)
print(bids-covered)
