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
def allin(g):
	return all(a in b.partners for a,b in it.combinations(g,2))
z=3
# ~ Pool=set(Dpc.values())
Pool=list(Dpc.values())
PL=[]
while True:
	for p in Pool:
		for pi,pl in enumerate(PL):
			if allin(pl|set([p])):PL[pi]=pl|set([p])
		PL.append(set([p]))
	# ~ print([len(x) for x in PL])
	mx=max([len(x) for x in PL])
	print(mx)
	S=set()
	for pl in PL:
		if len(pl)==mx:
			N=[x.name for x in pl]
			N.sort()
			S.add(",".join(N))
	for s in S:print(s)
	input()
