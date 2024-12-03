#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ~ import sympy
import re

ap=re.compile("turn (\w+) (\d+),(\d+) through (\d+),(\d+)")
tog=re.compile("toggle (\d+),(\d+) through (\d+),(\d+)")
G=[[False for col in range(1000)] for row in range(1000)]
on=True
off=False
for line in open(0).read().splitlines():
	if ap.match(line):
		p,tr,tc,br,bc=ap.search(line).groups()
		tr,tc,br,bc=map(int,(tr,tc,br,bc))
		v=eval(p)
		for r in range(tr,br+1):
			for c in range(tc,bc+1):
				G[r][c]=v
	else:
		tr,tc,br,bc=tog.search(line).groups()
		tr,tc,br,bc=map(int,(tr,tc,br,bc))
		for r in range(tr,br+1):
			for c in range(tc,bc+1):
				G[r][c]=not G[r][c]
count=0
for row in G:count+=row.count(True)
print(count)
	
