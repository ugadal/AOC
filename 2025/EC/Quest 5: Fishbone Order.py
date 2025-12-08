#!/usr/bin/env python3
#
from malib import *
fn="everybody_codes_e2025_q05_p1.txt"
V=list(map(int,open(fn).readline().split(":")[1].split(",")))
S=[('',V.pop(0),'')]
while V:
	v=V.pop(0)
	for i,(a,b,c) in enumerate(S):
		if not a and v<b:
			S[i]=(v,b,c)
			break
		if not c and v>b:
			S[i]=(a,b,v)
			break
	else:
		S.append(('',v,''))
res="".join([str(b) for a,b,c in S])
print(res)
def fb(l):
	sid,V=l.split(":")
	V=list(map(int,V.split(",")))
	S=[('',V.pop(0),'')]
	while V:
		v=V.pop(0)
		for i,(a,b,c) in enumerate(S):
			if not a and v<b:
				S[i]=(v,b,c)
				break
			if not c and v>b:
				S[i]=(a,b,v)
				break
		else:
			S.append(('',v,''))
	res="".join([str(b) for a,b,c in S])
	S=[int("".join(map(str,(a,b,c)))) for a,b,c in S]
	return int(sid),int(res),S
	
fn="everybody_codes_e2025_q05_p2.txt"
best=-inf
worst=inf
for l in open(fn):
	sid,v,S=fb(l)
	best=max(best,v)
	worst=min(worst,v)
print(best-worst)

fn="everybody_codes_e2025_q05_p3.txt"
D=open(fn).read()
SW=[fb(l) for l in D.splitlines()]

from functools import cmp_to_key
def ot(a,b):
	if a[1]<b[1]:return -1
	if a[1]>b[1]:return 1
	for i,j in zip (a[2],b[2]):
		if i<j:return -1
		if i>j:return 1
	if a[0]<b[0]:return -1
	return 1
	
SW=sorted(SW,key=cmp_to_key(ot))
SW.reverse()
res=sum(sid*(i+1) for i,(sid,_,_) in enumerate(SW))
print(res)
	
