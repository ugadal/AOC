#!/usr/bin/env python
# -*- coding: utf-8 -*-
part=2

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
for r,row in enumerate(block.splitlines()):
	for c,s in enumerate(row):
		pos=complex(c,r)
		G[pos]=int(s)
R=r+1
C=c+1
POS=set(G.keys())
DP=[complex(r,i) for r,i in it.product([-1,1,0],[-1,1,0])][:-1]
def around(pos):
	for dp in DP:
		np=pos+dp
		if np in POS:yield np
def rep():
	print(step)
	for row in range(R):print ("".join(map(str,(G[complex(col,row)] for col in range(C)))))
	print()
step=0
flashes=0
while True:
	step+=1
	G={k:v+1 for k,v in G.items()}
	todo=set(k for k,v in G.items() if v>9)
	done=set()
	while todo:
		for f in todo:
			for n in around(f):G[n]+=1
			done.add(f)
		todo=set(k for k,v in G.items() if v>9)-done
	for n in done:G[n]=0
	flashes+=len(done)
	if step==100:print(f"p1: {flashes} flashes done after {step} steps...")
	if len(done)==R*C:
		print("p2:",step)
		break
