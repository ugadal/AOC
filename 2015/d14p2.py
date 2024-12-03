#!/usr/bin/env python
# -*- coding: utf-8 -*-
am=2503
"""Vixen can fly 8 km/s for 8 seconds, but then must rest for 53 seconds."""
rec=0
VV=[]
for line in open("d14.txt").read().splitlines():
	E=line.split()
	sp,du,rt=[int(E[x]) for x in (3,6,13)]
	V=[sp]*du+[0]*rt
	while len(V)<am:V.extend(V)
	V=V[:am]
	VV.append(V)
P=[0 for v in VV]
for k in range(2503):
	dist=[sum(v[:k+1]) for v in VV]
	md=max(dist)
	for x,v in enumerate(dist):
		if v==md:P[x]+=1 
print(P,max(P))	
