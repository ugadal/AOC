#!/usr/bin/env python
# -*- coding: utf-8 -*-
fn,part="d7.txt",0
from collections import deque
from  intcode import computer
d=open(fn).readline().strip()
# ~ d=(3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,
# ~ -5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,
# ~ 53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10)

import itertools as it
v=list(range(5,10))
rec=float("-inf")
for p in it.permutations(v):
# ~ for p in [[9,7,8,5,6]]:
	Amps=[computer(d) for x in range(5)]
	for amp,x in zip(Amps,p):amp.inp.append(x)
	prev=0
	while True:
		flag=False
		for amp,code in zip(Amps,p):
			amp.inp.append(prev)
			try:prev=next(amp.flow)
			except:
				flag=True
				break
		rec=max(rec,prev)
		# ~ if prev==rec:print(prev)
		if flag:break
print(rec)
