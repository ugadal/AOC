#!/usr/bin/env python
# -*- coding: utf-8 -*-
from mylib import manager
D=manager(set)
for line in open("d12.txt").read().splitlines():
	l,rv =line.split(" <-> ")
	lo=D.get(l)
	for r in rv.split(", "):
		ro=D.get(r)
		lo.add(r)
		ro.add(l)
base=D.get("0")
while True:
	nb=set(base)
	for k in base:
		nb=nb|D.get(k)
	if nb==base:
		print("p1:",len(nb))
		break
	base=nb
# ~ p2
nbblock=0
while D.data:
	start=list(D.data.keys())[0]
	base=D.get(start)
	while True:
		nb=set(base)
		for k in base:nb=nb|D.get(k)
		if nb==base:
			for k in nb:D.data.pop(k)
			nbblock+=1
			break
		base=nb
print("p2:",nbblock)
