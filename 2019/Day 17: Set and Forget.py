#!/usr/bin/env python
# -*- coding: utf-8 -*-
fn,part="d17.txt",0
from intcodegen import computer
pgm=open(fn).readline().strip()
c=computer(pgm)
M={}
row=0
col=0
dirs={"^":-1j,"<":-1,"v":1j,">":1}
tl=-1j
tr=1j
for v in c.flow:
	if v==10:
		row+=1
		col=0
		continue
	pos=complex(col,row)
	M[pos]=chr(v)
	col+=1
	if chr(v) in "^<>v":
		sp=pos
		cd=dirs[chr(v)]
def draw(cp=0):
	mic=int(min(m.real for m in M))
	mxc=int(max(m.real for m in M))
	mir=int(min(m.imag for m in M))
	mxr=int(max(m.imag for m in M))
	S=complex(0,0)
	for r in range(mir,mxr+1):
		R=[]
		for c in range(mic,mxc+1):
			pos=complex(c,r)
			if pos==S:sym="S"
			elif pos==cp:sym="D"
			else:sym=M.get(pos,"?")
			R.append(sym)
		print("".join(R))
	print() 

draw()
print(sp,cd)
visited=[sp]
cp=sp
while True:
	while M.get(cp+cd,".")=="#":
		cp+=cd
		visited.append(cp)
	if M.get(cp+cd*tl,".")=="#":
		cd*=tl
		print("turned left")
		continue
	if M.get(cp+cd*tr,".")=="#":
		cd*=tr
		print("turned right")
		continue
	break
print(visited)
tt=0
for p in set(visited):
	if visited.count(p)>1:
		print(p)
		tt+=p.real*p.imag
print(tt)
