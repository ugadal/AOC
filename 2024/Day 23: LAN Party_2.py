#!/usr/bin/env python3
#
# ~ from functools import cache
from collections import deque
from functools import cache
import itertools as it
sep="\n\n"
fn,part="d23.txt",0
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
Pool=set(Dpc.values())
# ~ record=float("-Inf")
# ~ for a,b in it.combinations(Pool,2):
	# ~ if not a in b.partners:continue
	
	# ~ p=a.partners&b.partners
	# ~ NP=Pool
	# ~ for x in p:
		# ~ Pool=Pool&x.partners
	# ~ if Pool!=p:continue
	
	# ~ lp=len(p)
	# ~ if lp>record:
		# ~ record=lp
		# ~ N=[x.name for x in p]
		# ~ N.sort()
		# ~ print(a.name,b.name,lp,",".join(N))
# ~ exit()
# ~ Npool=set()
for n,g in enumerate(it.combinations(Pool,z)):
	if not any(x.good for x in g):continue
	if allin(g):
		# ~ print([x.name for x in g])
	# ~ Npool.add(g)
		t+=1
print(t)
# ~ print(len(Npool))
