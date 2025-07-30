#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
m=re.compile("^(\S+) = \((\S+), (\S+)\)")
def lorr(rule):
	while True:
		for c in rule:yield c
Problems=open(0).read().strip().split("\n\n")
print (len(Problems))
for p in Problems:
	print (p)
	print("*"*66)
rule=Problems[0].splitlines()[0]
print(rule)
D={}
for line in Problems[1].splitlines():
	k,g,d=m.search(line).groups()
	print(k,g,d)
	D[(k,"L")]=g
	D[(k,"R")]=d
starts=[a for a,b in D.keys()	if a.endswith("A") and b=="L"]
print(starts)
c=lorr(rule)
steps=0
while [k.endswith("Z") for k in starts].count(False):
	thisdir=next(c)
	steps+=1
	starts=[D[(k,thisdir)] for k in starts]
	# ~ print(steps,starts)
	
print(steps)
