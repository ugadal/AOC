#!/usr/bin/env python
# -*- coding: utf-8 -*-
fn="d12.txt"
inp=open(fn).read().split("===\n")[1].splitlines()
start=inp[0].split(": ")[1]
print(start)
Rules={}
for rule in inp[2:]:
	k,r=rule.split(" => ")
	Rules[k]=r
leftadded=0
while not start.startswith("..."):
	start="."+start
	leftadded+=1
while not start.endswith("..."):
	start=start+"."
for ite in range(1,101):
	ns=start[:2]
	for pos in range(len(start)-4):
		k=start[pos:pos+5]
		# ~ if k in Rules:ns+="#"
		# ~ else:ns+="."
		ns+=Rules[k]
	start=ns
	while not start.startswith("..."):
		start="."+start
		leftadded+=1
	# ~ while start.startswith("...."):
		# ~ start=start[1:]
		# ~ leftadded-=1
	while not start.endswith("..."):
		start=start+"."
	print(ite,start,leftadded)
	print (sum(p-5 for p,s in enumerate(start) if s=="#"))
print (8898+81*(50000000000-100))
