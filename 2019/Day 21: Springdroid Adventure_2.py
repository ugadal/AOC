#!/usr/bin/env python
# -*- coding: utf-8 -*-
fn,part="d21.txt",0
from functools import cache
from intcodegen import computer
import itertools as it
pgm=open(fn).readline().strip()
pc=list(it.product(("AND","OR","NOT"),("A","B","C","D","E","F","G","H","I","T","J"),("T\n","J\n")))
# ~ for p in pc:print(" ".join(p))
pc=[" ".join(p) for p in pc]
# ~ pc.remove("NOT D J\n")
for r in range(4,16):
	print("\n",r)
	for x,p in enumerate(it.product(pc,repeat=r)):
		print(x,end="\r")
		# ~ if x<2625000:continue
		c=computer(pgm)
		c.inp.extend([*map(ord,"".join(p))])
		c.inp.extend([*map(ord,"RUN\n")])
		res=list(c.flow)
		if res[34:40]!=list(map(ord,"Didn't")):
			print ()
			print (p)
			print (res)
			exit()
M={}
for row in range(47):
	for col in range(150):
		p=complex(col,row)
		c=computer(pgm)
		c.inp.extend([row,col])
		for v in c.flow:
			M[p]="#" if v else "."
@cache
def check(r,c):
	C=computer(pgm)
	C.inp.extend([r,c])
	return next(C.flow)
@cache
def getlc(row):
	if row<=5:return 8
	b=getlc(row-1)
	while not check(row,b):b+=1
	return b
@cache
def getrc(row):
	if row<=5:return 8
	b=getrc(row-1)+5
	while not check(row,b):b-=1
	return b

def draw(M):
	mic=int(min(m.real for m in M))
	mxc=int(max(m.real for m in M))
	mir=int(min(m.imag for m in M))
	mxr=int(max(m.imag for m in M))
	for r in range(mir,mxr+1):
		R=[]
		for c in range(mic,mxc+1):
			pos=complex(c,r)
			sym=M.get(pos,"?")
			# ~ if pos==S:sym="S"
			# ~ elif pos==cp:sym="D"
			# ~ else:sym=M.get(pos,"?")
			R.append(sym)
		print("".join(R),r,getlc(r),getrc(r))
	print() 
draw(M)
print(list(M.values()).count("#"))
# ~ r=105
d=100
r=d+5
while True:
	r+=1
	bl=getlc(r)
	tr=getrc(r-d+1)
	print(r,bl,tr)
	if tr-bl>=d-1:
		print(bl*10000+r-d+1)
		print((r-d+1)*10000+bl)
		break
# ~ < 13370986
# ~ < 13280979
# ~ M={}
# ~ for row in range(r-d,r+2):
	# ~ for col in range(bl-1,tr+2):
		# ~ p=complex(col,row)
		# ~ M[p]="#" if check(row,col) else "."
# ~ draw(M)
