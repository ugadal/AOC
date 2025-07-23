#!/usr/bin/env python
# -*- coding: utf-8 -*-
part=0

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
		# ~ if s==".":continue
		pos=complex(ic,ir)
		G[pos]=s
def getedge():
	mir=min(p.imag for p,v in G.items() if v=="#")
	mar=max(p.imag for p,v in G.items() if v=="#")
	mic=min(p.real for p,v in G.items() if v=="#")
	mac=max(p.real for p,v in G.items() if v=="#")
	return map(int,(mir,mar,mic,mac))
def draw():
	print(len(G))
	# ~ for k,v in G.items():print(k,v)
	mir,mar,mic,mac=getedge()
	print(*getedge())
	for row in range(mir,mar+1):
		R=[]
		for col in range(mic,mac+1):
			pos=complex(col,row)
			R.append("#" if G.get(pos,".")=="#" else ".")
		print("".join(R))
	print()
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
draw()
for enhance in range(2):
	NG={}
	mir,mar,mic,mac=getedge()
	# ~ input(f"{mir},{mar}  {mic},{mac}")
	for row in range(mir-1,mar+2):
		for col in range(mic-1,mac+2):
			pos=complex(col,row)
			t="".join("1" if G.get(z,".")=="#" else "0" for z in around(pos))
			pp=int(t,2)
			pp=pgm[pp]
			NG[pos]=pp
	G=NG
	draw()
print("p1:",list(NG.values()).count("#"))
