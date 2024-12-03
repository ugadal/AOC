#!/usr/bin/env python
# -*- coding: utf-8 -*-
inf=open("d24.txt").read().split("\n\n")[1].splitlines()
# ~ 9/10
Comp=[]
for row in inf:
	a,b=map(int,row.split("/"))
	Comp.append((a,b))
cb=0
def rec(FL,cs=0,nv=0):
	global cb
	usable=[k for k,(a,b) in enumerate(Comp) if FL[k] and (a==nv or b==nv)]
	if not usable:
		if cs>=cb:
			cb=cs
			print("record",cb)
			return
	for k in usable:
		# ~ print(k,Comp[k])
		a,b=Comp[k]
		if a==nv:nnv=b
		else:nnv=a
		NFL=list(FL)
		NFL[k]=False
		rec(NFL,cs+a+b,nnv)
unused=[True for x in Comp]
rec(unused)
