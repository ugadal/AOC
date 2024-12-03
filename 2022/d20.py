#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
day=sys.argv[0].split(".")[0][1:]
print(day)
import re
real=f"d{day}.txt"
data=[int(x) for x in open(real).read().strip().splitlines()]
class cell():
	def __init__(self,x):
		self.v=x
		self.r=None
		self.l=None
C=[cell(x) for x in data]
for a,b in zip(C,C[1:]):
	a.r=b
	b.l=a
C[-1].r=C[0]
C[0].l=C[-1]
l=len(data)
for c in C:
	if c.v%(l-1)==0:continue
	t=c
	for x in range(c.v%(l-1)):t=t.r
	c.l.r, c.r.l =c.r , c.l
	t.r.l = c
	c.r = t.r
	t.r=c
	c.l=t
	current=C[0]
c=C[0]
while c.v:c=c.r
ttl=0
for _ in range(3):
	for t in range(1000):c=c.r
	ttl+=c.v
print(ttl)
