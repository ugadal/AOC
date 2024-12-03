#!/usr/bin/env python
# -*- coding: utf-8 -*-
fn,part="d20.txt",5
from  itertools import product
dirs={'N':-1j,'E':1,'S':1j,'W':-1}
class tree():
	def __init__(self,data,d=0):
		self.parts=[]
		self.value=None
		self.t=None
		print("  "*d,"creating tree : ",data)
		if data.count("("):
			pos=data.index("(")
			lvl=1
			ep=pos
			while lvl:
				ep+=1
				if data[ep]=="(":lvl+=1
				if data[ep]==")":lvl-=1
			self.parts.append(tree(data[:pos],d+1))
			self.parts.append(tree(data[pos+1:ep],d+1))
			self.parts.append(tree(data[ep+1:],d+1))
			self.t="P"
			return
		if data.count("|"):
			self.parts=[]
			for p in data.split("|"):
				self.parts.append(tree(p,d+1))
			self.t="L"
			return
		self.t="V"
		self.parts=[data]
	def rep(self):
		if self.t=="P":
			Z=[]
			for p in self.parts:
				Z.append(p.rep())
				print("z:",Z,len(Z))
			R=list(product(*Z))
			print("returning",R)
			return R
		if self.t=="L":
			R=[]
			for p in self.parts:
				R.extend(p.rep())
			print("returning L",R)
			return R
		if self.t=="V":return self.parts
z="^ENNWSWW(NEWS|)SSSEEN(WNSE|)EE(SWEN|)NNN$"
z="^WSSEESWWWNW(S|NENNEEEENN(ESSSSW(NWSW|SSEN)|WSWWN(E|WWS(E|SS))))$"
# ~ z="NNNNEEN"
z=open(fn).read().splitlines()[part]
# ~ x=tree(z)
# ~ print(x.parts)
# ~ for i,p in enumerate(x.rep()):
	# ~ print(i,p)
# ~ exit()
"""
J'ai triche mon arbre se contruit correctement
mais je ne parviens pas a finaliser,
j'ai utilise une solution bete et efficace trouvee sur reddit
"""
Positions = []
CurPosition = 0 + 0j
DistanceField = {}
DistanceField[0+0j]=0
for CurChar in z[1:-1]:
	if CurChar   == '(':
		Positions.append(CurPosition)
	elif CurChar == ')':
		CurPosition = Positions.pop()
	elif CurChar == '|':
		CurPosition = Positions[-1]
	elif CurChar in 'NESW':
		NewPosition = CurPosition + dirs[CurChar]
		DistanceField[NewPosition] = min(
			DistanceField.get(NewPosition,DistanceField[CurPosition]+1),
			DistanceField[CurPosition]+1
		)
		CurPosition = NewPosition

print("Part 1: " + str(max(DistanceField.values())))
print("Part 2: " + str(sum(map(lambda x: x >= 1000, DistanceField.values()))))
