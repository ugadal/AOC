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
for x in range(10):
	z=""
	for a,b in zip(st,st[1:]):
		z+=a+R[a+b]
	z+=b
	st=z
mx=float("-inf")
mn=-mx
for c in set(R.values()):
	v=z.count(c)
	mx=max(mx,v)
	mn=min(mn,v)
print("p1:",mx-mn)
# ~ p2
st,rules=block.split("\n\n")
em=set(R.values())
IC={a+b: 0 for a,b in it.product(em,repeat=2)}
# ~ print(IC)
for a,b in zip(st,st[1:]):IC[a+b]+=1
for x in range(40):
	NC={a+b: 0 for a,b in it.product(em,repeat=2)}
	for k,v in IC.items():
		if not v:continue
		a,b=k
		t=R[k]
		NC[a+t]+=v
		NC[t+b]+=v
	IC=NC
	# ~ print(x,1+sum(IC.values()))
seen={x:0 for x in em}
for (a,b),v in IC.items():
	seen[a]+=v
	seen[b]+=v
# ~ print(seen)
print("p2:",1+(max(seen.values())-min(seen.values()))//2)
# ~ this might seem strange
# ~ ab -> ax xb -> ay yx xz zb
# ~ as string
# ~ ab -> axb -> ayxzb  each symbol seen once
# ~ but in dimers count a and b seen once, xyz seen twice, first and last symbol lacking one
