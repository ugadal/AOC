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
# ~ blocks=open(fn).read().split("\n\n\n")[part]
inp="389125467"
inp="459672813"
class cup():
	ring=[]
	byn={}
	def __init__(self,label):
		cup.ring.append(self)
		cup.byn[int(label)]=self
		self.l=None
		self.r=None
		self.n=label
		self.nn=int(label)
for c in inp:
	cup(c)
for a,b in zip(cup.ring,cup.ring[1:]+[cup.ring[0]]):
	a.r=b
	b.l=a
s=cup.byn[int(inp[0])]
# ~ print (s.l,s.r)
# ~ print (s.l.n,s.r.n)
cp=s
for r in range(100):
	pop=[cp.r,cp.r.r,cp.r.r.r]
	pv=[c.nn for c in pop]
	# ~ print(pv)
	cp.r=pop[-1].r
	cp.r.l=cp
	dest=cp.nn
	while dest-1:
		if dest-1 in pv:
			dest-=1
			continue
		dest-=1
		break
	else:
		dest=9
		while True:
			if dest in pv:
				dest-=1
				continue
			break
	ip=cup.byn[dest]
	ip.r,pop[0].l,ip.r.l,pop[-1].r=pop[0],ip,pop[-1],ip.r
	cp=cp.r
	# ~ print(ip.nn,cp.nn)
s=cup.byn[1]
r=[]
for x in range(8):
	s=s.r
	r.append(s.n)
print("p1 :","".join(r))
for c in range(10,1000001):cup(str(c))
for a,b in zip(cup.ring,cup.ring[1:]+[cup.ring[0]]):
	a.r=b
	b.l=a
cp=cup.byn[int(inp[0])]
for r in range(10000000):
	pop=[cp.r,cp.r.r,cp.r.r.r]
	pv=[c.nn for c in pop]
	# ~ print(pv)
	cp.r=pop[-1].r
	cp.r.l=cp
	dest=cp.nn
	while dest-1:
		if dest-1 in pv:
			dest-=1
			continue
		dest-=1
		break
	else:
		dest=1000000
		while True:
			if dest in pv:
				dest-=1
				continue
			break
	ip=cup.byn[dest]
	ip.r,pop[0].l,ip.r.l,pop[-1].r=pop[0],ip,pop[-1],ip.r
	cp=cp.r
	# ~ print(ip.nn,cp.nn)
s=cup.byn[1]
print("p2:",s.r.nn*s.r.r.nn)
