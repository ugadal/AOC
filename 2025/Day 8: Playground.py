#!/usr/bin/env python3
#
from malib import *
fn,part="d8.txt",1
data=open(fn).read().split(sep)[part]

JB=[tuple(map(int,l.split(","))) for l in data.splitlines()]

rec=inf
DP={}
for i,j in it.combinations(JB,2):
	d=dist(i,j)
	DP[i,j]=d
DL=sorted(DP.items(),key=lambda x:x[1])
C=[]
for (a,b),d in DL[:1000]:
	if any(a in c for c in C):
		ac=next(c for c in C if a in c)
	else:ac=False
	if any(b in c for c in C):
		bc=next(c for c in C if b in c)
	else:bc=False
	if ac and bc:
		if ac==bc:continue
		C.remove(ac)
		C.remove(bc)
		C.append(ac|bc)
		continue
	if ac:
		ac.add(b)
		continue
	if bc:
		bc.add(a)
		continue
	C.append(set([a,b]))
L=[len(c) for c in C]
L.sort()
res=reduce(L[-3:])
print("p1 :",res)

njb=len(JB)
C=[]
def checkconn(a,b,C):
	if len(C)==1:
		if len(C[0])==njb:
			print("p2 :",a[0]*b[0])
			exit()
for (a,b),d in DL:
	if any(a in c for c in C):
		ac=next(c for c in C if a in c)
	else:ac=False
	if any(b in c for c in C):
		bc=next(c for c in C if b in c)
	else:bc=False
	if ac and bc:
		if ac==bc:continue
		C.remove(ac)
		C.remove(bc)
		C.append(ac|bc)
		checkconn(a,b,C)
		continue
	if ac:
		ac.add(b)
		checkconn(a,b,C)
		continue
	if bc:
		bc.add(a)
		checkconn(a,b,C)
		continue
	C.append(set([a,b]))
