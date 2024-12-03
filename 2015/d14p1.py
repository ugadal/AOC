#!/usr/bin/env python
# -*- coding: utf-8 -*-
am=2503
"""Vixen can fly 8 km/s for 8 seconds, but then must rest for 53 seconds."""
rec=0
for line in open("d14.txt").read().splitlines():
	E=line.split()
	sp,du,rt=[int(E[x]) for x in (3,6,13)]
	V=[sp]*du+[0]*rt
	while len(V)<am:V.extend(V)
	V=V[:am]
	dist=sum(V)
	if dist>rec:rec=dist
print(rec)
