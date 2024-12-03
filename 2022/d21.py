#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ~ import sympy
import sys
day=sys.argv[0].split(".")[0][1:]
exp=f"exp{day}.txt"
real=f"d{day}.txt"
S={}
D={}
V={}
# ~ for l in open(exp).read().splitlines():
for l in open(real).read().splitlines():
	k,f=l.split(": ")
	if k=="root":
		print (l)
		continue
	if k=="humn":continue
	if len(f.split())>1:D[k]=f
	else:V[k]=int(f)
V["humn"]=3423279932937
	  # ~ 3428077322232
# ~ print(V)
while D:
	rem=[]
	for k in D.keys():
		l,op,r=D[k].split()
		if l in V and r in V:
			# ~ print(l,op,r,V[l],V[r])
			V[k]=eval(f"{V[l]} {op} {V[r]}")
			rem.append(k)
	for k in rem:D.pop(k)
	if not rem:break
print(V["rnsd"],V["vlzj"])
print(V["rnsd"]==V["vlzj"])
print(V["rnsd"]-V["vlzj"])
for k in D.keys():
	print (k,D[k])
# ~ for k in V.keys():
	# ~ print (k,V[k])
"""
53428542700198.766 21718827469549.0
53428542700189.5   21718827469549.0
53428542700180.24  21718827469549.0
53428542700170.98  21718827469549.0
53428542700161.71  21718827469549.0















"""
