#!/usr/bin/env python
# -*- coding: utf-8 -*-
part=0
def repres(p,v):print(f"p{p}: {v}")
import re
import sys
import itertools as it
from functools import cache
import random
# ~ import uuid
# ~ import numpy as np
cp=str(sys.argv[0])
dre=re.compile(r"^Day (\d+):")
day=dre.findall(cp)[0]
fn=f"d{day}.txt"
# ~ block=open(fn).read().split("\n\n\n")[part]
block=open(fn).read().split("\n\n")[part]
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
for line in block.splitlines():
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
	# ~ P=[]
	tp=list(pool)
	for r in reg.A.values():r.reset()
	for op,ta,tb in ops:
		match op:
			case 'inp':ta.v=tp.pop(0)
			# ~ case 'inp':
				# ~ ta.v=random.randrange(1,10)
				# ~ P.append(ta.v)
			case 'add':ta.v+=tb.v
			case 'set':ta.v=tb.v
			case 'mul':ta.v*=tb.v
			case 'div':
				if tb.v==0:
					print("err div",pool)
					return False
				ta.v//=tb.v
			case 'mod':
				if ta.v<0 or tb.v<0:
					print("err mod")
					return False
				ta.v%=tb.v
			case 'eql':ta.v=1 if ta.v==tb.v else 0
			case 'dif':ta.v=1 if ta.v!=tb.v else 0
	return res.v==0
	# ~ else:
		# ~ print(P,"wrong",res.v)
		# ~ return False
for pool in it.product([9,8,7,6,5,4,3,2,1],repeat=14):
# ~ while True:
	print("\r",pool,end="")
	v=run(list(pool))
	# ~ print(v)
	if v:
		print(v)
