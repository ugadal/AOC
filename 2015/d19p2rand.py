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

target=mol
part2=0
while target !="e":
	tmp=target
	for a,b in rules:
		if b not in target:continue
		target=target.replace(b,a,1)
		part2+=1
	if tmp==target:
		target=mol
		part2=0
		suffle(rules)
print(part2)
