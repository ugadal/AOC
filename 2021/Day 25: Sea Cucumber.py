#!/usr/bin/env python
# -*- coding: utf-8 -*-
part=1
def repres(p,v):print(f"p{p}: {v}")
import re
import sys
import itertools as it
from functools import cache
import random
# ~ import uuid
# ~ import numpy as np
cp=str(sys.argv[0])
dre=re.compile(r"^Day (\d+):")
day=dre.findall(cp)[0]
fn=f"d{day}.txt"
# ~ block=open(fn).read().split("\n\n\n")[part]
block=open(fn).read().split("\n\n")[part]
G={}
for ir,row in enumerate(block.splitlines()):
	for ic,s in enumerate(row):
		pos=complex(ic,ir)
		G[pos]=s
R=ir+1
C=ic+1
def rep():
	print()
	for row in range(R):
		t=[]
		for col in range(C):
			pos=complex(col,row)
			t.append(G[pos])
		print("".join(t))
	print()
input()
rep()
def cmr(pos):
	c=(1+pos.real)%C
	r=pos.imag
	np=complex(c,r)
	if G[np]==".":return np
	return pos
def cmd(pos):
	c=pos.real
	r=(1+pos.imag)%R
	np=complex(c,r)
	if G[np]==".":return np
	return pos
steps=0
while True:
	steps+=1
	E=[(k,cmr(k)) for k,v in G.items() if v==">"]
	moved=any(p!=np for p,np in E)
	for p,np in E:
		G[p]="."
		G[np]=">"
	D=[(k,cmd(k)) for k,v in G.items() if v=="v"]
	moved=moved or any(p!=np for p,np in D)
	for p,np in D:
		G[p]="."
		G[np]="v"
	if not moved:break
	rep()
print(moved,steps)
