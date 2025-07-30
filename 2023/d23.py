#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
from copy import deepcopy as dcp
from tqdm import tqdm
fe="exp23.txt"
fr="d23.txt"
Rocks=[]
N={}
class node():
	def __init__(self,r,c,symbol):
		self.r=r
		self.c=c
		self.out=set()
		self.visited=False
		N[(r,c)]=self
		self.symbol=symbol
		self.d=0
	def mkconn(self):
		match self.symbol:
			case "#":return
			case ">":
				self.out.add(N[(self.r,self.c+1)])
			case "<":
				self.out.add(N[(self.r,self.c-1)])
			case "^":
				self.out.add(N[(self.r-1,self.c)])
			case "v":
				if self.r==len(L)-1:return
				self.out.add(N[(self.r+1,self.c)])
			case ".":
				No=N[(self.r-1,self.c)]
				So=N[(self.r+1,self.c)]
				Ea=N[(self.r,self.c+1)]
				We=N[(self.r,self.c-1)]
				if No.symbol!="#":
					self.out.add(No)
					if No.symbol!="v":No.out.add(self)
				if So.symbol!="#":
					self.out.add(So)
					if So.symbol!="^":So.out.add(self)
				if Ea.symbol!="#":
					self.out.add(Ea)
					if Ea.symbol!="<":Ea.out.add(self)
				if We.symbol!="#":
					self.out.add(We)
					if We.symbol!=">":We.out.add(self)
L=open(fe).read().splitlines()
# ~ L=open(fr).read().splitlines()
for ri,row in enumerate(L):
	for co,symbol in enumerate(row):
		node(ri,co,symbol)
si=next(i for i,s in enumerate(L[0]) if s==".")		
startnode=N[(0,si)]
startnode.symbol="v"
ei=next(i for i,s in enumerate(L[-1]) if s==".")		
endnode=N[(len(L)-1,ei)]
endnode.symbol="v"
for node in tqdm(N.values()):node.mkconn()
UN=set([node for node in N.values() if not node.visited])
curr=startnode
while UN:
	for targ in curr.out&UN:targ.d=max(curr.d+1,targ.d)
	curr.visited=True
	UN.remove(curr)
	curr=max(UN,key=lambda s:s.d)
	# ~ print (curr.r,curr.c,curr.d)
	if curr==endnode:break
print (endnode.d)
