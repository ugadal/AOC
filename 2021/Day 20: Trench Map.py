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
		# ~ if s==".":continue
		pos=complex(ic,ir)
		G[pos]=s
def getedge():
	mir=min(p.imag for p,v in G.items())
	mar=max(p.imag for p,v in G.items())
	mic=min(p.real for p,v in G.items())
	mac=max(p.real for p,v in G.items())
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
# ~ while True:
	NG={}
	mir,mar,mic,mac=getedge()
	# ~ input(f"{mir},{mar}  {mic},{mac}")
	for row in range(-200,200):
		for col in range(-200,200):
			pos=complex(col,row)
			t="".join("1" if G.get(z,".")=="#" else "0" for z in around(pos))
			pp=int(t,2)
			pp=pgm[pp]
			NG[pos]=pp
	G=NG
	# ~ draw()
	# ~ input()
r=[]
for k,v in G.items():
	if v==".":continue
	if not -180<k.imag<180:continue
	if not -180<k.real<180:continue
	r.append(k)

print("p1:",len(r))

# ~ print("p1:",list(NG.values()).count("#"))
