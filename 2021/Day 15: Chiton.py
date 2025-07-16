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
G={}
BP={}
for r,row in enumerate(block.splitlines()):
	for c,s in enumerate(row):
		pos=complex(c,r)
		G[pos]=int(s)
		BP[pos]=float("Inf")
R=r
C=c
sp=complex(0,0)
BP[sp]=0
todo=set([sp])
def around(p):
	for dp in (-1,1,1j,-1j):
		np=p+dp
		if np in G:yield np
while todo:
	cp=todo.pop()
	cw=BP[cp]
	for tar in around(cp):
		v=G[tar]
		if cw+v<BP[tar]:
			BP[tar]=cw+v
			todo.add(tar)
ep=complex(C,R)
print("p1:",BP[ep])
