#!/usr/bin/env python
# -*- coding: utf-8 -*-
fn,part="d9.txt",0
data=open(fn).read().split("\n\n")[part].splitlines()
V=[int(x) for x in data]
import itertools as it
while len(V)>=26:
	Valid=[a+b for a,b in it.combinations(V[:25],2)]
	if V[25] not in Valid:
		print("p1:",V[25])
		target=V[25]
		break
	V.pop(0)
V=[int(x) for x in data]
NV=[a+b for a,b in zip(V,V[1:])]
off=2
while (target not in NV) and NV:
	NV=[a+b for a,b in zip(NV,V[off:])]
	off+=1
pos=NV.index(target)
part=V[pos:pos+off]
print("p2:",min(part)+max(part))
