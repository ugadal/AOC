#!/usr/bin/env python
# -*- coding: utf-8 -*-
fn,part="d19.txt",0
from intcodegen import computer
pgm=open(fn).readline().strip()
# ~ pgm="2"+pgm[1:]
M={}
for row in range(50):
	for col in range(50):
		p=complex(col,row)
		c=computer(pgm)
		c.inp.extend([row,col])
		for v in c.flow:
			M[p]="#" if v else "."
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
		print("".join(R))
	print() 
draw(M)
print(list(M.values()).count("#"))
