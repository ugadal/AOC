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
			self.v=v
		except:
			self.v=0
		reg.A[name]=self
for line in open(fn).read().splitlines():
	P=line.split()
	if line.startswith("inp"):
		tn=P[1]
		if tn in reg.A:tn=reg.A[tn]
		else:tn=reg(tn)
		ops.append(("inp",tn))
		continue
	ta,tb=P[1:]
	if ta in reg.A:ta=reg.A[ta]
	else:ta=reg(ta)
	if tb in reg.A:tb=reg.A[tb]
	else:tb=reg(tb)
	ops.append((P[0],ta,tb))
print(ops)
