#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ~ import sympy
import re
ap=re.compile("turn (\w+) (\d+),(\d+) through (\d+),(\d+)")
tog=re.compile("toggle (\d+),(\d+) through (\d+),(\d+)")
G=[[0 for col in range(1000)] for row in range(1000)]
on=1
off=-1
for line in open(0).read().splitlines():
	if ap.match(line):
		p,tr,tc,br,bc=map(eval,ap.search(line).groups())
		for r in range(tr,br+1):
			for c in range(tc,bc+1):
				G[r][c]=max(0,p+G[r][c])
	else:
		tr,tc,br,bc=map(eval,tog.search(line).groups())
		for r in range(tr,br+1):
			for c in range(tc,bc+1):
				G[r][c]=G[r][c]+2
count=0
for row in G:count+=sum(row)
print(count)
	
