#!/usr/bin/env python
# -*- coding: utf-8 -*-
fn,part="d4.txt",0
data=open(fn).read().split("\n\n")[part].splitlines()
G={}
for r,line in enumerate(data):
	for c,s in enumerate(line):
		G[c+r*1j]=s
NR,NC=r+1,c+1
print(NR,NC)
def valid(pos,d):
	for p,s in zip((pos+k*d for k in range(1,4)),"MAS"):
		if G.get(p,"")!=s:return False
	return True

import itertools as it
dirs=[a+b for a,b in it.product((-1,1,0),(-1j,1j,0))][:-1]
res=0
for row in range(NR):
	for col in range(NC):
		pos=col+row*1j
		if G.get(pos,"")!="X":continue
		for d in dirs:
			if valid(pos,d):res+=1
print(res)
# ~ print(0+0*1j==0)
# ~ z={}
# ~ z[0]="zero"
# ~ z[0+0*1j]="zeroc"
# ~ print(z)
