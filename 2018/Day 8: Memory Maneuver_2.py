#!/usr/bin/env python
# -*- coding: utf-8 -*-
fn="d8.txt"
inp=open(fn)
V=list(map(int,inp.readline().strip().split()))
V=list(map(int,inp.readline().strip().split()))
# ~ 2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2
# ~ A----------------------------------
    # ~ B----------- C-----------
                     # ~ D-----
meta=[]
pos=0
cch=0
class node():
	def __init__(self,pos,sons,md):
		global cch
		cch+=1
		self.name=f"#{cch}"
		self.beg=pos
		self.endpos=None
		self.md=md
		self.mdv=None
		self.Sons=[]
		self.sons=sons
		print (f"Created node {self.name} starting at {self.beg} expecting {self.sons} sons and {self.md} metadata")
	def end(self):
		print(f"in end function : {self.name} {self.endpos} {len(self.Sons)}")
		if self.endpos:
			print("returning from endpos",self.endpos)
			return self.endpos
		if not self.Sons:
			print("no sons currently returning beg+1",self.beg+1)
			return self.beg+1
		v=self.Sons[-1].end()
		print("last son ending in ",v)
		return v
	def full(self):
		if len(self.Sons)==self.sons:return True
		return False
	def rep(self):
		for k in dir(self):
			if k.startswith('__'):continue
			v=self.__getattribute__(k)
			if type(v)==type(self.rep):continue
			print(k,self.__getattribute__(k))

a,b=V[:2]
WL=[]
WL.append(node(0,a,b))
while True:
	cn=WL[-1]
	print(f"current node {cn.name}")
	cn.rep()
	if not cn.full():
		ns=cn.end()+1
		print("ns",ns)
		a,b=V[ns:ns+2]
		print("next vals",a,b)
		WL.append(node(ns,a,b))
		WL[-1].rep()
	else:
		print("node is full")
		if cn.sons==0:
			cn.endpos=cn.beg+1+cn.md
			cn.mdv=sum(V[cn.beg+2:cn.beg+2+cn.md])
		else:
			mds=cn.end()+1
			print(f"mds :{mds}")
			tt=0
			for v in V[mds:mds+cn.md]:
				print(f"v:{v}")
				if v>cn.sons:continue
				tt+=cn.Sons[v-1].mdv
			cn.mdv=tt
			cn.endpos=mds+cn.md-1
		cn.rep()
		WL.pop()
		WL[-1].Sons.append(cn)
		WL[-1].rep()
