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

G={}
BP={}
for r,row in enumerate(block.splitlines()):
	for c,s in enumerate(row):
		pos=complex(c,r)
		G[pos]=int(s)
		BP[pos]=float("Inf")

pos=list(G.keys())
C+=1
R+=1

for rb in range(1,5):
	for p in pos:
		np=p+complex(rb*C,0)
		v=G[p]+rb
		v=v%9 if v>9 else v
		G[np]=v

pos=list(G.keys())
for db in range(1,5):
	for p in pos:
		np=p+complex(0,db*R)
		v=G[p]+db
		v=v%9 if v>9 else v
		G[np]=v

ec=max(p.real for p in G.keys())
er=max(p.imag for p in G.keys())
ep=complex(ec,er)
print(ep)
for p in G.keys():BP[p]=float("Inf")
BP[sp]=0
todo=set([sp])
while todo:
	cp=todo.pop()
	cw=BP[cp]
	for tar in around(cp):
		v=G[tar]
		nv=cw+v
		if nv<BP[tar]:
			BP[tar]=nv
			todo.add(tar)
print("p2:",BP[ep])











