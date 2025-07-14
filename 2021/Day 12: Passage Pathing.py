#!/usr/bin/env python
# -*- coding: utf-8 -*-
part=3

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
pairs=[]
nodes=set()
for line in block.splitlines():
	a,b=line.split("-")
	pairs.append((a,b))
	nodes.add(a)
	nodes.add(b)
print(nodes)
class node():
	byn={}
	def __init__(self,n):
		node.byn[n]=self
		self.n=n
		self.small=False if n.isupper() else True
		self.link=set()
Nodes=[node(n) for n in nodes]
sn=node.byn["start"]
en=node.byn["end"]
for a,b in pairs:
	na=node.byn[a]
	nb=node.byn[b]
	na.link.add(nb)
	nb.link.add(na)
paths=0
todo=[[sn]]
while todo:
	cp=todo.pop(0)
	lp=cp[-1]
	if lp==en:
		paths+=1
		# ~ print([p.n for p in cp])
		continue
	for tar in lp.link:
		if tar.small and tar in cp:continue
		todo.append(cp+[tar])
		# ~ print (todo)
print("p1:",paths)
for n in Nodes:
	if sn in n.link:n.link.remove(sn)
paths=0
todo=[[sn]]
while todo:
	cp=todo.pop(0)
	lp=cp[-1]
	if lp==en:
		paths+=1
		# ~ print([p.n for p in cp])
		continue
	sv=set(no for no in cp if no.small)
	svt=any(cp.count(no)==2 for no in sv)
	for tar in lp.link:
		if tar.small and tar in cp and svt:continue
		todo.append(cp+[tar])
		# ~ print (todo)
print("p2:",paths)
