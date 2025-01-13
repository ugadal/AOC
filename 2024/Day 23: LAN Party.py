#!/usr/bin/env python3
#
# ~ from functools import cache
from collections import deque
from functools import cache
import itertools as it
sep="\n\n"
fn,part="d23.txt",1
pcnames=set()
Dpc={}
class pc():
	def __init__(self,name):
		self.name=name
		self.partners=set()
		self.good=True if name.startswith("t") else False
for l in open(fn).read().split(sep)[part].splitlines():
	a,b=l.split("-")
	pcnames.add(a)
	pcnames.add(b)
	if not a in Dpc:Dpc[a]=pc(a)
	if not b in Dpc:Dpc[b]=pc(b)
	Dpc[a].partners.add(Dpc[b])
	Dpc[b].partners.add(Dpc[a])
print(len(pcnames))
t=0
for n,(a,b,c) in enumerate(it.combinations(Dpc.values(),3)):
	# ~ print(n,any((a.good,b.good,c.good)))
	# ~ any 
	if not any((a.good,b.good,c.good)):continue
	if not b in a.partners:continue
	if not c in a.partners:continue
	if not c in b.partners:continue
	print(n,"ok")
	t+=1
print(t)
