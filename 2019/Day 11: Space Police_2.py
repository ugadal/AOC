#!/usr/bin/env python
# -*- coding: utf-8 -*-
fn,part="d11.txt",0
sep="\n\n"
data=open(fn).read().split(sep)[part].splitlines()[0]
from intcode_d9 import computer
icm=computer(data)
# ~ for res in icm.flow:print(res)
sp=0+0*1j
d=-1j
G={}
G[sp]=1
while True:
	curcolor=G.get(sp,0)
	icm.inp.append(curcolor)
	color=next(icm.flow)
	try:rotation=next(icm.flow)
	except:break
	print(color,rotation)
	G[sp]=color
	if rotation:d=d*1j
	else:d=d*-1j
	sp+=d
	print(len(G))
print(G)
minr=int(min(k.imag for k in G.keys()))
maxr=int(max(k.imag for k in G.keys()))
minc=int(min(k.real for k in G.keys()))
maxc=int(max(k.real for k in G.keys()))
print(minr,minc,maxr,maxc)
for row in range(minr,maxr+1):
	txt=[]
	for col in range(minc,maxc+1):txt.append("#" if G.get(col+row*1j,0) else " ")
	print("".join(txt))
