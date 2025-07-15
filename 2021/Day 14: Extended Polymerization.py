#!/usr/bin/env python
# -*- coding: utf-8 -*-
part=1

import re
import sys
import itertools as it
from functools import cache
import uuid
cp=str(sys.argv[0])
dre=re.compile(r"^Day (\d+):")
day=dre.findall(cp)[0]
fn=f"d{day}.txt"
block=open(fn).read().split("\n\n\n")[part]
# ~ block=open(fn).read().split("\n\n")[part]
st,rules=block.split("\n\n")
print(st)
R={}
for rule in rules.splitlines():
	a,b=rule.split(" -> ")
	R[a]=b
print(R)
for x in range(10):
	z=""
	for a,b in zip(st,st[1:]):
		z+=a+R[a+b]
	z+=b
	# ~ print(z)
	st=z
mx=float("-inf")
mn=-mx
for c in set(R.values()):
	v=z.count(c)
	mx=max(mx,v)
	mn=min(mn,v)
	print(c,v,mn,mx)
print(mx-mn)
