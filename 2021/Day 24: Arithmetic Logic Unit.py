#!/usr/bin/env python
# -*- coding: utf-8 -*-
part=0
def repres(p,v):print(f"p{p}: {v}")
import re
import sys
import itertools as it
from functools import cache
# ~ import uuid
# ~ import numpy as np
cp=str(sys.argv[0])
dre=re.compile(r"^Day (\d+):")
day=dre.findall(cp)[0]
fn=f"d{day}.txt"
# ~ block=open(fn).read().split("\n\n\n")[part]
# ~ block=open(fn).read().split("\n\n")[part]
ops=[]
class reg():
	A={}
	def __init__(self,name):
		try:
			v=int(name)
			self.v=self.ori=v
		except:
			self.v=self.ori=0
		reg.A[name]=self
	def reset(self):
		self.v=self.ori
for line in open(fn).read().splitlines():
	P=line.split()
	if line.startswith("inp"):
		tn=P[1]
		if tn in reg.A:tn=reg.A[tn]
		else:tn=reg(tn)
		ops.append(("inp",tn,None))
		continue
	ta,tb=P[1:]
	if ta in reg.A:ta=reg.A[ta]
	else:ta=reg(ta)
	if tb in reg.A:tb=reg.A[tb]
	else:tb=reg(tb)
	ops.append((P[0],ta,tb))
# ~ for op in ops:
	# ~ print(op)
# ~ for r in reg.A.items():print(r)
res=reg.A["z"]
def run(pool):
	for r in reg.A.values():r.reset()
	for op,ta,tb in ops:
		match op:
			case 'inp':ta.v=pool.pop(0)
			case 'add':ta.v+=tb.v
			case 'mul':ta.v*=tb.v
			case 'div':ta.v//=tb.v
			case 'mod':ta.v%=tb.v
			case 'eql':ta.v=1 if ta.v==tb.v else 0
	return res.v==0
for pool in it.product([9,8,7,6,5,4,3,2,1],repeat=14):
	print(pool)
	v=run(list(pool))
	# ~ print(v)
	if v:break
