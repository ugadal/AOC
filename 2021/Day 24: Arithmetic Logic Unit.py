#!/usr/bin/env python
# -*- coding: utf-8 -*-
part=0
def repres(p,v):print(f"p{p}: {v}")
import re
import sys
import itertools as it
from functools import cache
import random
# ~ import uuid
# ~ import numpy as np
cp=str(sys.argv[0])
dre=re.compile(r"^Day (\d+):")
day=dre.findall(cp)[0]
fn=f"d{day}.txt"
# ~ block=open(fn).read().split("\n\n\n")[part]
block=open(fn).read().split("\n\n")[part]
ops=[]
class reg():
	A={}
	def __init__(self,name):
		try:
			v=int(name)
			self.v=self.ori=v
		except:
			self.v=self.ori=0
		reg.A[name]=self
	def reset(self):
		self.v=self.ori
for line in block.splitlines():
	P=line.split()
	if line.startswith("inp"):
		tn=P[1]
		if tn in reg.A:tn=reg.A[tn]
		else:tn=reg(tn)
		ops.append(("inp",tn,None))
		continue
	ta,tb=P[1:]
	if ta in reg.A:ta=reg.A[ta]
	else:ta=reg(ta)
	if tb in reg.A:tb=reg.A[tb]
	else:tb=reg(tb)
	ops.append((P[0],ta,tb))
# ~ for op in ops:
	# ~ print(op)
# ~ for r in reg.A.items():print(r)
res=reg.A["z"]
def run(pool):
	# ~ P=[]
	tp=list(pool)
	for r in reg.A.values():r.reset()
	for op,ta,tb in ops:
		match op:
			case 'inp':ta.v=tp.pop(0)
			# ~ case 'inp':
				# ~ ta.v=random.randrange(1,10)
				# ~ P.append(ta.v)
			case 'add':ta.v+=tb.v
			case 'set':ta.v=tb.v
			case 'mul':ta.v*=tb.v
			case 'div':
				if tb.v==0:
					print("err div",pool)
					return False
				ta.v//=tb.v
			case 'mod':
				if ta.v<0 or tb.v<0:
					print("err mod")
					return False
				ta.v%=tb.v
			case 'eql':ta.v=1 if ta.v==tb.v else 0
			case 'dif':ta.v=1 if ta.v!=tb.v else 0
	print(res.v)
	return res.v==0
	# ~ else:
		# ~ print(P,"wrong",res.v)
		# ~ return False
for pool in it.product([9,8,7,6,5,4,3,2,1],repeat=14):
# ~ while True:
	print("\r",pool,end="")
	v=run(list(pool))
	# ~ print(v)
	if v:
		print(pool)
		input()
	break
def recoded(pool):
	x=y=z=w=0
	p=pool

	w=p[0]
	x=1
	y=z=w+12
	# ~									 z[a+12]

	w=p[1]
	z*=26
	z+=w+7		# z: (v1+12)*26+ v2+7
	# ~ 								z[a+12,b+7]
	
	w=v3=p[2]
	z*=26+w+1   #:z  ( (v1+12)*26+ v2+7 ) * 26
	# ~ 								z[a+12,b+7,c+1]
	
	w=v4=p[3]
	z*=26
	z+=w+2		#z  (( (v1+12)*26+ v2+7 ) * 26 +  v3+1) * 26 + v4+2
	# ~ 								z[a+12,b+7,c+1,d+2]
	
	w=v5=e=p[4]
	x=z%26  # v4+2
	# ~ 								x=d+2
	z=z//26     # (v1+12)*26+ v2+7 ) * 26 +  v3+1
	# ~ 								z[a+12,b+7,c+1]
	x-=5		# v4-3
	# ~ 								x=d-3
	x=1 if d-3 != e else 0   # x = v4-3!=v5
	# ~ on veut x=0 pour avoir y=1
	# ~ donc on veut e=d-3 supposons cela vrai			e=d-3; d>=4
	y=25*x+1		# y = 1 | 26						y=1
	z*=y			#									z[a+12,b+7,c+1]
	y=x*(w+4)
	z+=y
	
	w=v6=f=p[5]
	x=1
	y=w+15
	z=26*z + y   # y=w+15
	# ~ 							z[a+12,b+7,c+1,f+15]
	
	w=v7=g=p[6]
	x=1
	y=w+11
	z=26*z + y # y = w+11
	# ~ 							z[a+12,b+7,c+1,f+15,g+11]

	w=v8=h=p[7]
	x=z%26		#					x g+11
	z=z//26		# 					z[a+12,b+7,c+1,f+15]
	x-=13		# 					x g-2
	x=1 if x!=w else 0
	# ~ on veut x=0  g-2=h	#								h=g-2 ; g>=3
	y=25*x+1 #												y=1
	z*=y	#						z[a+12,b+7,c+1,f+15]
	y=x*(w+5)
	z+=y
	
	w=v9=i=p[8]
	x=z%26		#					x f+15
	z=z//26#						z[a+12,b+7,c+1]
	x-=16	#						x f-1
	x=1 if x!=w else 0
	# on veut f-1=i											i=f-1 ; f>=2
	y=25*x+1
	z*=y
	y=x*(w+3)
	z+=y#							z[a+12,b+7,c+1]
	
	w=v10=j=p[9]
	x=z%26	#						x=c+1
	z=z//26	#						z[a+12,b+7]
	x-=8	#						x=c-7
	x=1 if x!=w else 0
	# ~ on veut c-7=j										j=c-7 ; c>=8			
	y=25*x+1
	z*=y
	y=x*(w+9)
	z+=y
	
	w=v11=k=p[10]
	x=1
	y=w+2
	z=z*26+y	#					z[a+12,b+7,k+2]
	
	w=v12=l=p[11]
	x=z%26		#					x k+2
	z=z//26		#					z[a+12,b+7]
	x-=8		#					x k-6
	x=1 if x!=w else 0
	# ~ on veut  k-6=l										l=k-6;k>=7
	y=25*x+1
	z*=y
	y=x*(w+3)
	z+=y		#					z[a+12,b+7]
	
	w=v13=m=p[12]
	x=z%26		# 					x b+7
	z=z//26		#					z [a+12]
	x=1 if x!=w else 0
	# ~ on veut b+7=m										m=b+7 ;b<=2
	y=25*x+1
	z*=y
	y=x*(w+3)
	z+=y
	
	w=v14=n=p[13]
	x=z%26	#						x a+12
	z=z//26	# z []
	x-=4	#						x a+8
	x=1 if x!=w else 0
	# ~ on veut a+8=n										n=a+8; a=1
	y=25*x+1
	z*=y
	y=x*(w+11)
	z+=y
	return z
	
for pool in it.product([9,8,7,6,5,4,3,2,1],repeat=14):
	print("\r",pool,end="")
	v=recoded(pool)
	print(v,end="")
	if not v:
		print(pool)
		input()
	# ~ break
"""
A	1							1
B		<=2						2
C		>=8						9
D		>=4						9
E			D-3					6
F		>=2						9
G		>=3						9
H			G-2					7
I			F-1					8
J			C-7					2
K		>=7						9
L			K-6					3
M			B+7					9
N			A+8					9

12996997829399

A	1							1
B		<=2						1
C		>=8						8
D		>=4						4
E			D-3					1
F		>=2						2
G		>=3						3
H			G-2					1
I			F-1					1
J			C-7					1
K		>=7						7
L			K-6					1
M			B+7					8
N			A+8					9

11841231117189
"""
# ~ z[a+12]

