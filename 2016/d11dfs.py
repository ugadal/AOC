#!/usr/bin/env python
# -*- coding: utf-8 -*-
from copy import deepcopy as dc
import re
import itertools as it
from random import shuffle
EV={}
def mget(d,k):
	if k in d:return d[k]
	print(f"creating key {k}")
	v=2**(len(EV))
	d[k]=v
	return v
F=[]
gen=re.compile("a (\w+) generator")
chip=re.compile("a (\w+)-compatible microchip")
for floor,comp in enumerate(open(0).read().splitlines()):
	gval=sum([mget(EV,g) for g in gen.findall(comp)])
	cval=sum([mget(EV,g) for g in chip.findall(comp)])
	F.append([gval,cval])
# ~ print(EV)
ev=EV.values()
goal=2*sum(ev)
Valid=[]
elems=EV.values()
nbe=len(elems)
F=list(map(list,(zip(*F))))
def mkkey(e,sg,sc):
	nk=0
	for t in [e]+sg+sc:
		nk=(nk<<nbe)+t
	return nk
VD={}
def isvalid(e,sg,sc):
	nk=mkkey(e,sg,sc)
	if nk in VD:return VD[nk]
	# ~ if nk in VD:return False
	for g,c in zip(sg[1:],sc[1:]):
		if g and g&c!=c:
			VD[nk]=False
			return False
	VD[nk]=True
	return True
full=2**nbe-1
best=float('inf')
def prog(step,seen,etage,sg,sc,path):
	global best
	PS=[]
	# ~ print("entered",step,seen,etage,sg,sc)
	if step>=best or step>1000:return
	if sg[-1]+sc[-1]==2*full:
		print("ok",step,etage,path)
		best=step
		return
	tk=mkkey(etage,sg,sc)
	g,c=sg[etage],sc[etage]
	for nxtlvl in (etage+1,etage-1):
		if not 0<=nxtlvl<=3:continue
		cg=[elem for elem in ev if elem&g==elem]
		cc=[elem for elem in ev if elem&c==elem]
		
		# ~ takeone of each
		# ~ if etage==0 and cg and cc:
		if cg and cc:
			for a,b in it.product(cg,cc):
				NG=dc(sg)
				NC=dc(sc)
				NG[nxtlvl]+=a
				NG[etage]-=a
				NC[nxtlvl]+=b
				NC[etage]-=b
				nk=mkkey(nxtlvl,NG,NC)
				if nk in seen:continue
				if not isvalid(nxtlvl,NG,NC):continue
				PS.append((step+1,seen+[tk],nxtlvl,NG,NC,path+["b"]))
		# ~ taketwo g
		if len(cg)>=2:
			for a,b in it.combinations(cg,2):
				NG=dc(sg)
				NC=dc(sc)
				NG[nxtlvl]+=a+b
				NG[etage]-=a+b
				nk=mkkey(nxtlvl,NG,NC)
				if nk in seen:continue
				if not isvalid(nxtlvl,NG,NC):continue
				PS.append((step+1,seen+[tk],nxtlvl,NG,NC,path+["2g"]))
		# ~ taketwo c
		if len(cc)>=2:
			for a,b in it.combinations(cc,2):
				NG=dc(sg)
				NC=dc(sc)
				NC[nxtlvl]+=a+b
				NC[etage]-=a+b
				nk=mkkey(nxtlvl,NG,NC)
				if nk in seen:continue
				if not isvalid(nxtlvl,NG,NC):continue
				PS.append((step+1,seen+[tk],nxtlvl,NG,NC,path+["2c"]))
		# ~ takeone g
		for elem in cg:
			NG=dc(sg)
			NC=dc(sc)
			NG[nxtlvl]+=elem
			NG[etage]-=elem
			nk=mkkey(nxtlvl,NG,NC)
			if nk in seen:continue
			if not isvalid(nxtlvl,NG,NC):continue
			PS.append((step+1,seen+[tk],nxtlvl,NG,NC,path+["1g"]))
		# ~ takeone c
		for elem in cc:
			NG=dc(sg)
			NC=dc(sc)
			NC[nxtlvl]+=elem
			NC[etage]-=elem
			nk=mkkey(nxtlvl,NG,NC)
			if nk in seen:continue
			if not isvalid(nxtlvl,NG,NC):continue
			PS.append((step+1,seen+[tk],nxtlvl,NG,NC,path+["1c"]))
		shuffle(PS)
		for s in PS:
			prog(*s)
prog(0,[],0,F[0],F[1],[])
