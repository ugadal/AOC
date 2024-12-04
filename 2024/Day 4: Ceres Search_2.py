#!/usr/bin/env python3
#
fn,part="d4.txt",1
data=open(fn).read().split("\n\n")[part].splitlines()
G={}
for r,line in enumerate(data):
	for c,s in enumerate(line):
		G[c+r*1j]=s
NR=r+1
NC=c+1

def valid(pos):
	lqc=[G.get(pos+d,"") for d in dirs]
	if lqc.count("M")!=2:return False
	if lqc.count("S")!=2:return False
	NW=G.get(pos-1-1j,"")
	SE=G.get(pos+1+1j,"")
	if NW==SE:return False
	if NW=="" or SE=="":return False
	return True
import itertools as it
res=0
dirs=[-1-1j,1-1j,-1+1j,1+1*1j]
for row in range(NR):
	for col in range(NC):
		pos=col+row*1j
		if G.get(pos,"")!="A":continue
		if valid(pos):res+=1
print(res)
