#!/usr/bin/env python3
#
from malib import *
from z3 import *
data=open(fn).read().split(sep)[part]
def mnmx(a,b):
	for v in range(a,b+1):
		if v==0 or v%2:yield v
def recsam(l,t,st=[]):
	needed=t-sum(st)
	if len(st)==l-1:
		if needed==0 or needed%2:
			yield st+[needed]
	else:
		for v in mnmx(0,needed):
			yield from recsam(l,t,st+[v])

res=0
for line in data.splitlines():
	parts=line.split()
	target=parts[0]
	buttons=parts[1:-1]
	goal=[True if c=="#" else False for c in target[1:-1]]
	buttons=[list(map(int,b[1:-1].split(",")))  for b in buttons ]
	press=1
	found=False
	while not found:
		for co in recsam(len(buttons),press):
			status=[False]*len(goal)
			for but,p in zip(buttons,co):
				if p:
					for v in but:
						status[v]=not status[v]
			if status==goal:
				res+=press
				found=True
				break
		else:
			press+=1
print("p1 :",res)

def recsam(l,t,st=[]):
	needed=t-sum(st)
	if len(st)==l-1:
		yield st+[needed]
	else:
		for v in range(0,needed+1):
			yield from recsam(l,t,st+[v])
def solve(B,goal):
	buttons=[set(b) for b in B]
	s=Optimize()
	bsyms=[Int(f"but{bi}") for bi,b in enumerate(buttons)]
	for bsym in bsyms:s.add(bsym>=0)
	for i,v in enumerate(goal):
		s.add(sum([bsym for but,bsym in zip(buttons,bsyms) if i in but])==v)
	s.minimize(sum(bsyms))
	s.check()
	res=s.model()
	return sum([res.eval(bsym).as_long() for bsym in bsyms])

res=0
for line in data.splitlines():
	parts=line.split()
	target=parts[-1]
	buttons=parts[1:-1]
	goal=list(map(int,target[1:-1].split(",")))
	buttons=[list(map(int,b[1:-1].split(",")))  for b in buttons ]
	res+=solve(buttons,goal)
print("p2 :",res)
