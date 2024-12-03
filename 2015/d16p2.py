#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ~ Frosting: capacity 4, durability -2, flavor 0, texture 0, calories 5
import itertools as it
import re
dig=re.compile("^Sue (\d+): (\w+): (\d+), (\w+): (\d+), (\w+): (\d+)$")
Aunts={}
# ~ Sue 1: children: 1, cars: 8, vizslas: 7
# ~ Sue 13: akitas: 10, pomeranians: 0, vizslas: 2
for line in open("d16.txt").read().splitlines():
	E=list(dig.search(line).groups())
	auntnum=E.pop(0)
	d={}
	while E:
		k=E.pop(0)
		v=int(E.pop(0))
		d[k]=v
	Aunts[auntnum]=d
# ~ for k,v in Aunts.items():print(k,v)
infos="""children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1"""
for info in infos.splitlines():
	k,v=info.split(": ")
	v=int(v)
	torem=[]
	for ak in Aunts.keys():
		if k in Aunts[ak]:
			if k in ["cats","trees"]:
				if Aunts[ak][k]<=v:torem.append(ak)
			elif k in ["pomeranians","goldfish"]:
				if Aunts[ak][k]>=v:torem.append(ak)
			elif Aunts[ak][k]!=v:torem.append(ak)
				
	for ak in torem:Aunts.pop(ak)
print(Aunts)
