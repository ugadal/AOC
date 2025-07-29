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
	if res in seen:break
	seen.add(res)
repres(1,res)

G={}
for r,row in enumerate(block.splitlines()):
	for c,s in enumerate(row):
		pos=complex(c,r)
		G[0,pos]=s
def livearound2(l,pos):
	left=[(l,pos-1)]
	right=[(l,pos+1)]
	top=[(l,pos-1j)]
	bottom=[(l,pos+1j)]
	if pos.imag==0:top=[(l+1,2+1j)]
	if pos.imag==4:bottom=[(l+1,2+3j)]
	if pos.real==0:left=[(l+1,1+2j)]
	if pos.real==4:right=[(l+1,3+2j)]
	if pos==2+1j:
		bottom=[(l-1,c) for c in range(5)]
	if pos==1+2j:
		right=[(l-1,r*1j) for r in range(5)]
	if pos==2+3j:
		top=[(l-1,4j+c) for c in range(5)]
	if pos==3+2j:
		left=[(l-1,4+r*1j) for r in range(5)]
	P=left+right+top+bottom
	return[G.get(p,".") for p in P].count("#")
print (livearound2(0,4))
print (livearound2(0,3))
# ~ exit()
def rep2(l):
	print()
	# ~ res=0
	# ~ bf=1
	for r in range(NR):
		t=[]
		for c in range(NC):
			pos=complex(c,r)
			t.append(G.get((l,pos),"."))
			# ~ if G[(l,pos)]=="#":res+=bf
			# ~ bf*=2
		print ("".join(t))
	# ~ return res
mic=min(couche-1 for (couche,pos),v in G.items() if v=="#")
mac=max(couche+1 for (couche,pos),v in G.items() if v=="#")
print(mic,mac)
for couche in range (mic,mac+1):
	rep2(couche)
for rr in range(200):
	NG={}
	for couche in range(mic,mac+1):
		alive=[]
		deads=[]
		for r in range(NR):
			for c in range(NC):
				if c==r==2:continue
				pos=complex(c,r)
				if G.get((couche,pos),".")=="#":alive.append(pos)
				else:deads.append(pos)
		# ~ print(couche,alive)
		# ~ print(couche,deads)
		# ~ input()
		NG=NG|{(couche,pos):"." if livearound2(couche,pos)!=1 else "#" for pos in alive}
		NG=NG|{(couche,pos):"#" if 1<=livearound2(couche,pos)<=2 else "." for pos in deads}
		# ~ print(NG)
		# ~ input()
	G=NG
	mic=min(couche-1 for (couche,pos),v in G.items() if v=="#")
	mac=max(couche+1 for (couche,pos),v in G.items() if v=="#")
	print(mic,mac)
for couche in range (mic,mac+1):
	print(couche)
	rep2(couche)
res=sum(1 for k,v in G.items() if v=="#")
repres(2,res)
