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
# ~ block=open(fn).read().split("\n\n\n")[part]
block=open(fn).read().split("\n\n")[part]
BT={v:0 for v in range(9)}
V=tuple(map(int,block.split(",")))
V=[V.count(x) for x in range(9)]
for x in range(80):
	z=V.pop(0)
	V=V+[z]
	V[6]+=z
print("p1:",sum(V))
for x in range(256-80):
	z=V.pop(0)
	V=V+[z]
	V[6]+=z
print("p2:",sum(V))
