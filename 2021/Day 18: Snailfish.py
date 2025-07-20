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
class pair():
	ap=[]
	def __init__(self):
		pair.ap.append(self)
		self.a=None
		self.b=None
		self.pp=None
		self.nat=None
		self.par=None
	def rep(self):
		# ~ print(self,"repping")
		V=[]
		V.append(self.a if type(self.a)==int else self.a.rep())
		V.append(self.b if type(self.b)==int else self.b.rep())
		return V
	def mkdep(self,d=0):
		self.pp=d
		if type(self.a)==pair:
			self.a.par=self
			self.a.nat="left"
			self.a.mkdep(d+1)
		if type(self.b)==pair:
			self.b.par=self
			self.b.nat="right"
			self.b.mkdep(d+1)
s="[1,2]"
pre=re.compile(r"^\[.*\]$")
def smartsplit(s):
	# ~ print("sm",s)
	cp=-1
	while True:
		nc=s.index(",",cp+1)
		# ~ print("nc",nc)
		lp=s[:nc]
		rp=s[nc+1:]
		if lp.count("[")==lp.count("]") and rp.count("[")==rp.count("]"):
			return lp,rp
		cp=nc
def ana(s):
	if s.isdigit():return int(s)
	if pre.match(s):
		a,b=smartsplit(s[1:-1])
		tp=pair()
		tp.a=ana(a)
		tp.b=ana(b)
		return tp
	else:return "?"
e="""[1,2]
[[1,2],3]
[9,[8,7]]
[[1,9],[8,5]]
[[[[1,2],[3,4]],[[5,6],[7,8]]],9]
[[[9,[3,8]],[[0,9],6]],[[[3,7],[4,9]],3]]
[[[[1,3],[5,3]],[[1,3],[8,7]]],[[[4,9],[6,9]],[[8,2],[7,3]]]]"""
for l in e.splitlines():
	pair.ap=[]
	x=ana(l)
	# ~ print([p.pp for p in pair.ap])
	x.mkdep()
	print(l,[p.pp for p in pair.ap])
l="[[[[[9,8],1],2],3],4]"
pair.ap=[]
x=ana(l)
# ~ print([p.pp for p in pair.ap])
x.mkdep()
print(l,[p.pp for p in pair.ap])
pb=next(p for p in pair.ap if p.pp==4)
print(pb)
print(pb.rep())
print(pb.par)
print(pb.par.rep())
# ~ exit()
l="[7,[6,[5,[4,[3,2]]]]]"
pair.ap=[]
x=ana(l)
# ~ print([p.pp for p in pair.ap])
x.mkdep()
print(l,[p.pp for p in pair.ap])
pb=next(p for p in pair.ap if p.pp==4)
print(pb)
print(pb.rep())
print(pb.par)
print(pb.par.rep())
exit()
l="[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]"
pair.ap=[]
x=ana(l)
# ~ print([p.pp for p in pair.ap])
x.mkdep()
print(l,[p.pp for p in pair.ap])
