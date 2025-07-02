#!/usr/bin/env python
# -*- coding: utf-8 -*-
part=0
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
	if x.startswith('"'):return [x[1:-1]]
	if x.count(" | "):
		return list(it.product(*map(decompose,x.split(" | "))))
	if x.count(" "):
		return "".join(*it.product(*map(decompose,x.split(" "))))
	if R[x].startswith('"'):return [R[x][1:-1]]
	return decompose(R[x])
print(decompose("4 | 5"))
print(decompose("4 5 | 5 4 | 4 4 4"))
