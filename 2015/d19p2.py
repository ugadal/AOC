#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import deque
from random import shuffle
txtrules,mol=open("d19.txt").read().split("\n\n")
mol=mol.strip()
rules=[]
for line in txtrules.splitlines():
	bef,aft=line.split(" => ")
	rules.append((bef,aft))
Q=deque()
Q.append(("e",0))
Known=set()
it=0
lm=len(mol)
while Q:
	it+=1
	if (it%1000000)==0:print(it,Q[-1][1])
	q,step=Q.pop()
	if q in Known:continue
	if len(q)>lm:continue
	shuffle(rules)
	for bef,aft in rules:
		cp=-1
		for _ in range(q.count(bef)):
			cp=q.find(bef,cp+1)
			nm=q[:cp]+q[cp:].replace(bef,aft,1)
			if nm==mol:
				print(step+1)
				exit()
			Q.append((nm,step+1))
			cp+=1
	Known.add(q)
	
