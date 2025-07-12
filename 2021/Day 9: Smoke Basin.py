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
for r,line in enumerate(block.splitlines()):
	for c,s in enumerate(line):
		pos=complex(c,r)
		G[pos]=int(s)
R=r+1
C=c+1
def around(pos):
	for offs in (-1,1,1j,-1j):
		np=pos+offs
		if np in G:yield G[np]
res=0
for k,v in G.items():
	if all(x>v for x in around(k)):
		res+=v+1
print(res)
