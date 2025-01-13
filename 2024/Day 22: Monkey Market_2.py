#!/usr/bin/env python3
#
# ~ from functools import cache
from collections import deque
from functools import cache
import itertools as it
sep="\n\n"
fn,part="d22.txt",0

def sng(i):
	while True:
		yield i-10*(i//10)
		i=i^(i<<6)
		i=i%16777216
		i=i^(i>>5)
		i=i%16777216
		i=i^(i<<11)
		i=i%16777216
		# ~ yield i-10*(i//10)
def nx(g,c):
	for x in range(c-1):next(g)
	return next(g)
z=sng(123)
t=0
M=map(int,open(fn).read().splitlines())
C={}
for x in M:
# ~ for x in [1,2,3,2024]:
	T={}
	g=sng(x)
	v=[next(g) for _ in range(2001)]
	dv=[b-a for a,b in zip(v,v[1:])]
	for a,b,c,d,x in zip(dv,dv[1:],dv[2:],dv[3:],v[4:]):
		if (a,b,c,d) in T:continue
		T[a,b,c,d]=x
	for k,v in T.items():
		C[k]=C.get(k,0)+v
print(max(C.values()))
