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
	ap=[]
	def __init__(self):
		pair.ap.append(self)
		self.num=len(pair.ap)
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
	def vis(self):
		for v in self.a.vis():yield v
		for v in self.b.vis():yield v
		# ~ yield self
	def visp(self):
		for v in self.a.visp():yield v
		for v in self.b.visp():yield v
		yield self
	def mag(self):
		return 3*self.a.mag()+2*self.b.mag()
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
		# ~ print(len(ap))
		while any(p.pp==4 for p in ap):
			# ~ print("explodes")
			pb=next(p for p in ap if p.pp==4)
			# ~ print(pb.num)
			lv,rv=pb.a,pb.b
			# ~ for p in tree.vis():print(p,p.v)
			ov=[p for p in tree.vis()]
			if ov[0]==lv:pass
			else:
				for x,y in zip(ov,ov[1:]):
					if y==lv:break
				# ~ print(x.v,y.v)
				x.v+=y.v
			if ov[-1]==rv:pass
			else:
				for x,y in zip(ov,ov[1:]):
					if x==rv:break
				# ~ print(x.v,y.v)
				y.v+=x.v
			if pb.par.a==pb:pb.par.a=val(0)
			else:pb.par.b=val(0)
			# ~ pair.ap.remove(pb)
			# ~ for p in tree.vis():print(p,p.v)
			tree.mkdep()
			ap=[p for p in tree.visp() if type(p)==pair]
			# ~ print(tree.rep())
		
		split=False
		if any(p.v>9 for p in tree.vis()):
			split=True
			# ~ print("splits")
			pv=next(p for p in tree.vis() if p.v>9)
			# ~ print(pv,pv.v)
			# ~ input()
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
		# ~ print(tree.rep())
		return tree
# ~ l="[[[[[9,8],1],2],3],4]"
# ~ l="[7,[6,[5,[4,[3,2]]]]]"
# ~ l="[[6,[5,[4,[3,2]]]],1]"
# ~ l="[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]"
# ~ l="[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]"
# ~ pair.ap=[]
# ~ tree=ana(l)
# ~ tree.mkdep()
# ~ res=simplify(tree)
# ~ print(res.rep())
lines="""[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]
[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]
[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]
[[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]
[7,[5,[[3,8],[1,4]]]]
[[2,[2,2]],[8,[8,1]]]
[2,9]
[1,[[[9,3],9],[[9,0],[0,7]]]]
[[[5,[7,4]],7],1]
[[[[4,2],2],6],[8,7]]""".splitlines()
lines="""[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
[[[5,[2,8]],4],[5,[[9,9],0]]]
[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
[[[[5,4],[7,7]],8],[[8,3],8]]
[[9,3],[[9,9],[6,[4,9]]]]
[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]""".splitlines()
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
	# ~ print(np.rep())
	# ~ input()
	tree=simplify(np)
print(tree.rep())
print("p1:",tree.mag())
lines="""[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
[[[5,[2,8]],4],[5,[[9,9],0]]]
[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
[[[[5,4],[7,7]],8],[[8,3],8]]
[[9,3],[[9,9],[6,[4,9]]]]
[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]""".splitlines()
lines=open(fn).read().splitlines()
rec=0
for la,lb in it.combinations(lines,2):
	np=pair()
	np.a=ana(la)
	np.b=ana(lb)
	np.mkdep()
	np=simplify(np)
	rec=max(rec,np.mag())
	np=pair()
	np.a=ana(lb)
	np.b=ana(la)
	np.mkdep()
	np=simplify(np)
	rec=max(rec,np.mag())
print("p2:",rec)
