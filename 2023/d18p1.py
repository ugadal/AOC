#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
fe="exp18.txt"
fr="d18.txt"
import re
fp=re.compile("^\.+#\.")
R=(0,1)
D=(1,0)
U=(-1,0)
L=(0,-1)
DD={}
for s,k in zip(list("RDUL"),(R,D,U,L)):	DD[s]=k
class grid():
	def __init__(self,fn):
		self.moves=[]
		for l in open(fn).read().splitlines():
			d,s,cc=l.split()
			self.moves.append((d,int(s)))
	def fill(self):
		S=[(0,0)]
		r=c=0
		for d,s in self.moves:
			dr,dc=DD[d]
			for _ in range(s):
				r+=dr
				c+=dc
				S.append((r,c))
		S.pop()
		self.S=S
	def glim(self):
		self.topr=min([a for a,b in self.S])
		self.botr=max([a for a,b in self.S])+1
		self.leftc=min([b for a,b in self.S])
		self.rightc=max([b for a,b in self.S])+1
		self.rowrange=range(self.topr,self.botr)
		self.colrange=range(self.leftc,self.rightc)
	def makemap(self):
		M=[]
		for r in self.rowrange:
			tl="".join(["#" if (r,c) in self.S else "." for c in self.colrange])
			M.append(tl)
		for l in M:print(l)
		self.M=M
		self.ML=[[c for c in row]for row in M]
	def findfp(self):
		for ri,row in enumerate(self.M):
			if fp.match(row):
				mo=fp.match(row)
				return ri,mo.span()[1]-1
	def flood(self):
		floodrow,floodcol=self.findfp()
		totreat=[(floodrow,floodcol)]
		while totreat:
			r,c=totreat.pop(0)
			if self.ML[r][c]=="#":continue
			self.ML[r][c]="#"
			for (dr,dc) in DD.values():
				if self.ML[r+dr][c+dc]==".":
					totreat.append((r+dr,c+dc))
		tt=0
		for row in self.ML:
			tt+=row.count("#")
		return tt
G=grid(fr)
G.fill()
# ~ print(G.S)
G.glim()
print(G.S[:5])
print(G.S[-5:])
print(G.rowrange,G.colrange)
print(len(G.S))
G.makemap()
print(G.findfp())
# ~ for l in (G.ML):print ("".join(l))
print(G.flood())
