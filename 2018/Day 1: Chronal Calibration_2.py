#!/usr/bin/env python
# -*- coding: utf-8 -*-
Ops=list(map(int,open("d1.txt").read().splitlines()))
visited=set()
freq=0
while True:
	cv=Ops.pop(0)
	freq+=cv
	if freq in visited:
		print(freq)
		exit()
	visited.add(freq)
	Ops.append(cv)
