#!/usr/bin/env python
# -*- coding: utf-8 -*-
Boxes=open("d2.txt").read().splitlines()
import itertools as it
for a,b in it.combinations(Boxes,2):
	if [x==y for x,y in zip(a,b)].count(False)==1:
		print("".join([x for x,y in zip(a,b) if x==y]))
