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
# ~ target area: x=192..251, y=-89..-59
class val():
	def __init__(self,v):
		self.v=v
	def rep(self):return self.v
	def vis(self):yield self
	def visp(self):yield self
	def mag(self):return self.v
class pair():
	def __init__(self):
		self.a=None
		self.b=None
		self.pp=None
		self.par=None
	def rep(self):
		V=[]
		V.append(self.a if type(self.a)==int else self.a.rep())
		V.append(self.b if type(self.b)==int else self.b.rep())
		return V
	def mkdep(self,d=0):
		self.pp=d
		if type(self.a)==pair:
			self.a.par=self
			self.a.mkdep(d+1)
		if type(self.b)==pair:
			self.b.par=self
			self.b.mkdep(d+1)
	def vis(self):
		for v in self.a.vis():yield v
		for v in self.b.vis():yield v
	def visp(self):
		for v in self.a.visp():yield v
		for v in self.b.visp():yield v
		yield self
	def mag(self):
		return 3*self.a.mag()+2*self.b.mag()
s="[1,2]"
pre=re.compile(r"^\[.*\]$")
def smartsplit(s):
	cp=-1
	while True:
		nc=s.index(",",cp+1)
		lp=s[:nc]
		rp=s[nc+1:]
		if lp.count("[")==lp.count("]") and rp.count("[")==rp.count("]"):
			return lp,rp
		cp=nc
def ana(s):
	if s.isdigit():return val(int(s))
	if pre.match(s):
		a,b=smartsplit(s[1:-1])
		tp=pair()
		tp.a=ana(a)
		tp.b=ana(b)
		return tp
	else:return "?"
def simplify(tree):
	while True:
		ap=[p for p in tree.visp() if type(p)==pair]
		while any(p.pp==4 for p in ap):
			pb=next(p for p in ap if p.pp==4)
			lv,rv=pb.a,pb.b
			ov=[p for p in tree.vis()]
			if ov[0]==lv:pass
			else:
				for x,y in zip(ov,ov[1:]):
					if y==lv:break
				x.v+=y.v
			if ov[-1]==rv:pass
			else:
				for x,y in zip(ov,ov[1:]):
					if x==rv:break
				y.v+=x.v
			if pb.par.a==pb:pb.par.a=val(0)
			else:pb.par.b=val(0)
			tree.mkdep()
			ap=[p for p in tree.visp() if type(p)==pair]
		split=False
		if any(p.v>9 for p in tree.vis()):
			split=True
			pv=next(p for p in tree.vis() if p.v>9)
			na=pv.v//2
			nb=pv.v-na
			np=pair()
			np.a=val(na)
			np.b=val(nb)
			for pos in tree.visp():
				if type(pos)==val:continue
				if pos.a==pv:
					pos.a=np
					break
				if pos.b==pv:
					pos.b=np
					break
			tree.mkdep()
		if split:continue
		return tree
lines=open(fn).read().splitlines()
tree=ana(lines[0])
tree.mkdep()
print(tree.rep())
for l in lines[1:]:
	nb=ana(l)
	np=pair()
	np.a=tree
	np.b=nb
	np.mkdep()
	tree=simplify(np)
print(tree.rep())
print("p1:",tree.mag())
lines=open(fn).read().splitlines()
rec=0
for la,lb in it.permutations(lines,2):
	np=pair()
	np.a=ana(la)
	np.b=ana(lb)
	np.mkdep()
	np=simplify(np)
	rec=max(rec,np.mag())
print("p2:",rec)
