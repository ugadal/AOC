#!/usr/bin/env python
# -*- coding: utf-8 -*-
fn="d18.txt"
part=1
G={}
for row,line in enumerate(open(fn).read().split("\n\n")[part].splitlines()):
	for col,sym in enumerate(line):
		G[col+row*1j]=sym
nr,nc=row,col
for row in [-1,nr+1]:
	for col in range(-1,nc+2):G[col+row*1j]="%"
for col in [-1,nc+1]:
	for row in range(-1,nr+2):G[col+row*1j]="%"
around=[-1-1j,-1j,1-1j,-1+0j,1+0j,-1+1j,+1j,1+1j]
def draw():
	for row in range(-1,nr+2):
		tr=[]
		for col in range(-1,nc+2):
			tr.append(G[col+row*1j])
		print("".join(tr))
# ~ draw()
t=0
while t <=1000000000:
	t+=1
	newG={}
	for p,v in G.items():
		if v=="%":
			newG[p]=v
			continue
		A=[G[p+d] for d in around]
		symb=v
		match v:
			case ".":
				if A.count("|")>=3:symb="|"
			case "|":
				if A.count("#")>=3:symb="#"
			case "#":
				if A.count("#")==0 or A.count("|")==0 :symb="."
		newG[p]=symb
	G=dict(newG)
	# ~ draw()
	V=list(G.values())
	res=V.count("|")*V.count("#")
	print(t,res)
	if res==200466:
		while t<1000000000-28:t+=28
