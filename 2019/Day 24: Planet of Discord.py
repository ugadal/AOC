#!/usr/bin/env python
# -*- coding: utf-8 -*-
part=1
def repres(p,v):print(f"p{p}: {v}")
import re
import sys
import itertools as it
from functools import cache
import random
from intcoded23 import *
# ~ import uuid
# ~ import numpy as np
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
		G[pos]=s
NR=r+1
NC=c+1
print(NR,NC)
def rep():
	print()
	res=0
	bf=1
	for r in range(NR):
		t=[]
		for c in range(NC):
			pos=complex(c,r)
			t.append(G[pos])
			if G[pos]=="#":res+=bf
			bf*=2
		print ("".join(t))
	return res
rep()
def around(pos):
	yield pos-1j
	yield pos+1j
	yield pos+1
	yield pos-1
def livesaround(pos):
	return [G.get(tp,".") for tp in around(pos)].count("#")
def cs():
	r=0
	
seen=set()
while True:
	alive=[pos for pos,v in G.items() if v=="#"]
	NG={pos:"." if livesaround(pos)!=1 else "#" for pos in alive}
	deads=[pos for pos,v in G.items() if v=="."]
	NG=NG|{pos:"#" if 1<=livesaround(pos)<=2 else "." for pos in deads}
	G=NG
	res=rep()
	if res in seen:
		repres(1,res)
		exit()
	seen.add(res)
