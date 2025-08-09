#!/usr/bin/env python3
#
#  smms.py
import itertools as it
import random as rnd
nr=2
nc=5
G={(r,c):rnd.randrange(-9,10) for r in range(nr) for c in range(nc)}
def gc(v):
	p=list(range(v))
	for s in range(1,v+1):
		for c in it.combinations(p,s):yield c
rec=float("-inf")
sol=[]
for r in range(nr):
	print(" ".join(str(G[r,c]).rjust(4) for c in range(nc)))
for rr in gc(nr):
	for rc in gc(nc): 
		v=sum(G[r,c] for r in rr for c in rc)
		if v==rec:sol.append((rr,rc))
		if v>rec:
			rec=v
			sol=[(rr,rc)]
print(rec)
for s in sol:print(s)
for r in range(nr):
	wo=[]
	wi=[]
	a=b=0
	for c in range(nc):
		v=G[r,c]
		t=max(a,b)
		a,b=t,t+v
		wo.append(a)
		wi.append(b)
	print( " ".join(map(lambda x:str(x).rjust(4) ,wo)))
	print( " ".join(map(lambda x:str(x).rjust(4) ,wi)))
	print()
