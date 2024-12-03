#!/usr/bin/env python
# -*- coding: utf-8 -*-
rules,mol=open("d19.txt").read().split("\n\n")
mol=mol.strip()
newmol=set()
for line in rules.splitlines():
	bef,aft=line.split(" => ")
	print(bef,aft)
	cp=-1
	for _ in range(mol.count(bef)):
		cp=mol.find(bef,cp+1)
		nm=mol[:cp]+mol[cp:].replace(bef,aft,1)
		newmol.add(nm)
		cp+=1
print(len(newmol))
