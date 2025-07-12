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
V=tuple(map(int,block.split(",")))
rec=float("+Inf")
for p in range(max(V)+1):
	r=sum(abs(x-p) for x in V)
	if r<rec:
		rec=r
print("p1:",rec)
rec=float("+Inf")
for p in range(max(V)+1):
	r=sum(abs(x-p)*(abs(x-p)+1)//2 for x in V)
	if r<rec:
		rec=r
print("p2:",rec)
