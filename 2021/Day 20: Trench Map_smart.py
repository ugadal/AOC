#!/usr/bin/env python
# -*- coding: utf-8 -*-
part=1

import re
import sys
import itertools as it
from functools import cache
import uuid
import numpy as np
cp=str(sys.argv[0])
dre=re.compile(r"^Day (\d+):")
day=dre.findall(cp)[0]
fn=f"d{day}.txt"
block=open(fn).read().split("\n\n\n")[part]
# ~ block=open(fn).read().split("\n\n")[part]
pgm,img=block.split("\n\n")
pgm="".join(pgm.splitlines())
# ~ pgm="#"+pgm[1:]
G={}
for ir,row in enumerate(img.splitlines()):
	for ic,s in enumerate(row):
		pos=complex(ic,ir)
		G[pos]=s
def getedge():
	mir=min(p.imag for p,v in G.items())
	mar=max(p.imag for p,v in G.items())
	mic=min(p.real for p,v in G.items())
	mac=max(p.real for p,v in G.items())
	return map(int,(mir,mar,mic,mac))
def draw():
	mir,mar,mic,mac=getedge()
	for row in range(mir-2,mar+3):
		R=[]
		for col in range(mic-2,mac+3):
			pos=complex(col,row)
			R.append("#" if G.get(pos,defa)=="#" else ".")
		print("".join(R))
	print()
	input()
def around(pos):
	yield pos-1-1j
	yield pos-1j
	yield pos+1-1j
	yield pos-1
	yield pos
	yield pos+1
	yield pos-1+1j
	yield pos+1j
	yield pos+1+1j
mir,mar,mic,mac=getedge()
defa="."
for enhance in range(50):
	print("\r",enhance,end="")
	NG={}
	for row in range(mir-1,mar+2):
		for col in range(mic-1,mac+2):
			pos=complex(col,row)
			t="".join("1" if G.get(z,defa)=="#" else "0" for z in around(pos))
			pp=int(t,2)
			pp=pgm[pp]
			NG[pos]=pp
	G=NG
	if enhance==1:
		r=[]
		for k,v in G.items():
			if v==".":continue
			r.append(k)
		print("\np1:",len(r))		
	defa="#" if defa=="." else "."
	mir-=1
	mar+=1
	mic-=1
	mac+=1
r=[]
for k,v in G.items():
	if v==".":continue
	r.append(k)
print("\np2:",len(r))

