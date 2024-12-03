#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ~ #1 @ 37,526: 17x23
G={}
for line in open("d3.txt").read().split("\n\n")[1].splitlines():
	bid,_,gpos,dim=line.split()
	bid=int(bid[1:])
	c,r=map(int,gpos[:-1].split(","))
	dc,dr=map(int,dim.split("x"))
	for row in range(r,r+dr):
		for col in range(c,c+dc):
			G[row,col]=G.get((row,col),0)+1
print(len([k for k in G.values() if k>1]))
