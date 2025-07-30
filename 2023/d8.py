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
p="AAA"
c=lorr(rule)
steps=0
while p!="ZZZ":
	steps+=1
	p=D[(p,next(c))]
	print(p)
print(steps)
