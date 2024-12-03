#!/usr/bin/env python
# -*- coding: utf-8 -*-
fn,part="d7.txt",0
from collections import deque
from  intcode import computer
# ~ d=(3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,
# ~ 1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0)
# ~ d=(3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,3,0)
# ~ c=computer(d)
# ~ print(c.run(3))
# ~ print(c.run([1,0]))
# ~ print(c.run([0,6]))
# ~ print(c.run([4,65]))
# ~ print(c.run([3,652]))
# ~ print(c.run([2,6521]))

d=open(fn).readline().strip()
import itertools as it
v=list(range(5))
rec=float("-inf")
for p in it.permutations(v):
	Amps=[computer(d) for x in range(5)]
	prev=0
	for amp,code in zip(Amps,p):
		amp.inp.extend([code,prev])
		prev=next(amp.flow)
	rec=max(rec,prev)
print(rec)
