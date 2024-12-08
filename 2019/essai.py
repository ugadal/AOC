#!/usr/bin/env python3
#
from math import atan2,pi
C=[(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
C=[(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]
class V():
	def __init__(self,coord):
		x,y=coord
		self.x,self.y=coord
		self.alpha=atan2(x,y)
		if self.alpha<0:self.alpha+=2*pi
	def __lt__(self,other):
		print(f"comparing{self} to {other}")
		if self.alpha-other.alpha<0:return True
		return False
		# ~ return other.alpha-self.alpha
	def __str__(self):
		return f"({self.x},{self.y})  : {self.alpha}"


LV=[V(t) for t in C]
# ~ LV.sort()
LV=sorted(LV)
for v in LV:print(v)

C=[(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,1)]
