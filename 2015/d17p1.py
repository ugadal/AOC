#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ~ Frosting: capacity 4, durability -2, flavor 0, texture 0, calories 5
import itertools as it
CS=list(map(int,open("d17.txt").read().splitlines()))
nbc=len(CS)
sol=0
for nbel in range(2,nbc+1):
	for comb in it.combinations(CS,nbel):
		if sum(comb)==150:sol+=1
	if sol:
		print(nbel)
		break
print(sol)
