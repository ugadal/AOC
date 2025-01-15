#!/usr/bin/env python3
#
# ~ from functools import cache
from collections import deque
from functools import cache
import itertools as it
sep="\n\n"
fn,part="d25.txt",0
elems=open(fn).read().split(sep)
K=[]
L=[]
for block in elems:
	target=L if block.startswith("#") else K
	t="".join(block.splitlines())
	target.append(t)
res=0
for k,l in it.product(K,L):
	for a,b in zip(k,l):
		if a==b=="#":break
	else:
		print(k)
		print(l)
		res+=1
print(res)
