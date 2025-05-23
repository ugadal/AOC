#!/usr/bin/env python
# -*- coding: utf-8 -*-
fn,part="d3.txt",1
data=open(fn).read().split("\n\n")[part].splitlines()
G={}
for r,row in enumerate(data):
	for c,s in enumerate(row):
		pos=complex(c,r)
		G[pos]=s
R=r
C=c+1
sp=complex(0,0)
print(R,C)
res=1
for slope in [complex(1,1),complex(3,1),complex(5,1),complex(7,1),complex(1,2)]:
	trees=0
	sp=complex(0,0)
	while sp.imag<R:
		sp+=slope
		sp=complex(sp.real%C,sp.imag)
		if G[sp]=="#":trees+=1
	res*=trees
print(res)
