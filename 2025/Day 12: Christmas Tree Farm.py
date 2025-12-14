#!/usr/bin/env python3
#
from malib import *
data=open(fn).read().split(sep+sep)[part]
B=data.split(sep)
Rules=B.pop()
def flip(G):
	return [ v[::-1] for v in G]
def transp(G):
	return list(map("".join,zip(*G)))
def rot(G):return flip(transp(G))
class block():
	F={}
	def __init__(self,D):
		bn=int(D[0].split(":")[0])
		self.bn=bn
		self.D=D[1:]
		self.allrot=[]
		for r in range(4):
			self.allrot.append("".join(self.D))
			self.D=rot(self.D)
		self.D=flip(self.D)
		for r in range(4):
			self.allrot.append("".join(self.D))
			self.D=rot(self.D)
		ts=set(self.allrot)
		if len(ts)<8:
			self.allrot=[]
			for r in ts:
				v=[]
				for b in (0,3,6):
					v.append(r[b:b+3])
				self.allrot.append(v)
		block.F[bn]=self
for b in B:block(b.splitlines())
def compbb(ba,bb):
	for ra,rb in zip(ba,bb):
		for ca,cb in zip(ra,rb):
			if ca==cb=="#":return False
	return True
def analyse(rule):
	dim,reqs=rule.split(": ")
	r,c=map(int,dim.split("x"))
	reqs=list(map(int,reqs.split()))
	G=[]
	for row in range(r):G.append("."*c)
	
for rule in Rules.splitlines():
	analyse(rule)
