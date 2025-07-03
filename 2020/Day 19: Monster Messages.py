#!/usr/bin/env python
# -*- coding: utf-8 -*-
part=2
import re
import sys
import itertools as it
from functools import cache

cp=str(sys.argv[0])
dre=re.compile(r"^Day (\d+):")
day=dre.findall(cp)[0]
fn=f"d{day}.txt"
blocks=open(fn).read().split("\n\n\n")[part]
rules,data=blocks.split("\n\n")
print(rules)
print(data)
R={}
for line in rules.splitlines():
	rid,rule=line.split(": ")
	R[rid]=rule
@cache
def decompose(x):
	print('entering on',x)
	if x.startswith('"'):
		return [x[1:-1]]
	if x.count(" | "):
		P=[]
		for p in map(decompose,x.split(" | ")):
			P.extend(p)
		return P
	if x.count(" "):
		P=map(decompose,x.split(" "))
		P=list(P)
		P=it.product(*P)
		P=["".join(p) for p in P]
		return P
	return decompose(R[x])
ok=decompose("0")
nok=0
for line in data.splitlines():
	if line in ok:
		print(line,"ok")
		nok+=1
	else:print(line,"wrong")
print(f"p1: {nok}")
