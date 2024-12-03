#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import deque
from random import shuffle
from time import sleep
txtrules,mol=open("d19.txt").read().split("\n\n")
mol=mol.strip()
lm=len(mol)
rules=[]
for line in txtrules.splitlines():
	bef,aft=line.split(" => ")
	rules.append((bef,aft))
rec=float("inf")
K={}
# ~ iter=0
def dfs(s,step):
	# ~ global iter
	if s in K:return K[s]
	if len(s)>lm:return float("inf")
	# ~ iter+=1
	# ~ if iter%1000==0:print(s,step)
	cands=[]
	# ~ shuffle(rules)
	for bef,aft in rules:
		cp=-1
		for _ in range(s.count(bef)):
			cp=s.find(bef,cp+1)
			nm=s[:cp]+s[cp:].replace(bef,aft,1)
			if nm==mol:
				print(step+1)
				if step+1<rec:rec=step+1
				sleep(5)
				return step+1
			cands.append(nm)
			cp+=1
	v=min([dfs(cand,step+1) for cand in cands])
	K[s]=v
	return v
print(dfs("e",0))
