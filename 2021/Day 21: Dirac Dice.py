#!/usr/bin/env python
# -*- coding: utf-8 -*-
part=1

import re
import sys
import itertools as it
from functools import cache
import uuid
import numpy as np
cp=str(sys.argv[0])
dre=re.compile(r"^Day (\d+):")
day=dre.findall(cp)[0]
fn=f"d{day}.txt"
# ~ block=open(fn).read().split("\n\n\n")[part]
# ~ block=open(fn).read().split("\n\n")[part]
a,b,c=0,1,2
pa,pb=4,8
pa,pb=9,6
sa=sb=0
rolls=3
pa-=1
pb-=1
while True:
	pa=(pa+a+b+c+3)%10
	sa+=pa+1
	if sa>=1000:
		print("a wins")
		break
	rolls+=3
	a=(a+3)%100
	b=(b+3)%100
	c=(c+3)%100
	pb=(pb+a+b+c+3)%10
	sb+=pb+1
	if sb>=1000:
		print("b wins")
		break
	rolls+=3
	a=(a+3)%100
	b=(b+3)%100
	c=(c+3)%100
	# ~ exit()
print(sa,sb,rolls)
print("p1:",rolls*min(sa,sb))
pa,pb=4,8
pa,pb=9,6
oc=[x + y + z for x in [1, 2, 3] for y in [1, 2, 3] for z in [1, 2, 3]]
@cache
def rec(pa,pb,sa,sb):
	print(pa,pb,sa,sb)
	# ~ input()
	if sa>=21:return (1,0)
	sc=[0,0]
	for d in oc:
		npa=pa+d
		npa=(npa-1)%10+1
		nsa=sa+npa
		if nsa>=21:sc[0]+=1
		else:
			wb,wa=rec(pb,npa,sb,nsa)
			sc[1]+=wb
			sc[0]+=wa
	return sc
# ~ r=rec(4,8,0,0)
# ~ print(r,max(r))
r=rec(9,6,0,0)
print(r,max(r))
