#!/usr/bin/env python
# -*- coding: utf-8 -*-
import hashlib
import re
from mylib import memoize
ha=list("0123456789abcdef")
DM=[]
ms="ngcjuoqr"
@memoize
def mkh(x):
	h=hashlib.md5((ms+str(x)).encode()).hexdigest()
	for _ in range(2016):h=hashlib.md5(h.encode()).hexdigest()
	return h
for c in ha:
	tm=re.compile(f"{c}{c}{c}")
	pm=re.compile(f"{c}{c}{c}{c}{c}")
	DM.append((tm,pm))

index=-1
valid=[]
while len(valid)!=64:
	index+=1
	th=mkh(index)
	pmr=[tm.search(th) for tm,pm in DM]
	if any(pmr):
		print(index,th)
		rlim=100
		for tm,pm in DM:
			r=tm.search(th)
			if r:
				if r.start()<rlim:
					rlim=r.start()
					nxtpm=pm
		if any([nxtpm.search(mkh(x)) for x in range(index+1,index+1001)]):
			print(index)
			valid.append(index)
print(valid[-1])
