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
while True:
	curcolor=G.get(sp,0)
	icm.inp.append(curcolor)
	color=next(icm.flow)
	rotation=next(icm.flow)
	print(color,rotation)
	G[sp]=color
	if rotation:d=d*1j
	else:d=d*-1j
	sp+=d
	print(len(G))
