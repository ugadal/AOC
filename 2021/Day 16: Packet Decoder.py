#!/usr/bin/env python
# -*- coding: utf-8 -*-
part=0

import re
import sys
import itertools as it
from functools import cache
import uuid
cp=str(sys.argv[0])
dre=re.compile(r"^Day (\d+):")
day=dre.findall(cp)[0]
fn=f"d{day}.txt"
# ~ block=open(fn).read().split("\n\n\n")[part]
# ~ block=open(fn).read().split("\n\n")[part]
def getbs(line):
	r=bin(int(line,16))[2:]
	while len(r)%4:r="0"+r
	# ~ print(r)
	return r
def operate(ptid,V):
	match ptid:
		case 0:v=sum(V)
		case 1:
			v=1
			for t in V:v*=t	
		case 2:v=min(V)
		case 3:v=max(V)
		case 5:v=1 if V[0]>V[1] else 0
		case 6:v=1 if V[0]<V[1] else 0
		case 7:v=1 if V[0]==V[1] else 0
	return v
def treat(r):
	global ttv
	pv,r=int(r[:3],2),r[3:]
	ptid,r=int(r[:3],2),r[3:]
	ttv+=pv
	if ptid==4:
		tex=""
		while True:
			a,b,r=r[0],r[1:5],r[5:]
			tex+=b
			if a=="0":break
		v=int(tex,2)
		return v,r
	else:
		ltid,r=r[0],r[1:]
		if ltid=="1":
			nsp,r=int(r[:11],2),r[11:]
			V=[]
			for sp in range(nsp):
				v,r=treat(r)
				V.append(v)
			v=operate(ptid,V)
			return v,r
		else:
			ttlb,r=int(r[:15],2),r[15:]
			tex,r=r[:ttlb],r[ttlb:]
			V=[]
			while tex:
				t,tex=treat(tex)
				V.append(t)
			v=operate(ptid,V)
			return v,r
ttv=0
for line in open(fn).read().splitlines()[7:]:
	print("p2:",treat(getbs(line)))
print("p1:",ttv)
