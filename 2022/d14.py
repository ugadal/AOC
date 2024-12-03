#!/usr/bin/env python
# -*- coding: utf-8 -*-
exp="""498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9"""
X=[]
Y=[]
LINES=exp.splitlines()
# ~ LINES=open("d14.txt").read().splitlines()
for l in LINES:
	for t in l.split(" -> "):
		a,b=eval(t)
		X.append(a)
		Y.append(b)
print (min(X),max(X),min(Y),max(Y))
LC=min(X)-1
RC=max(X)+1
DR=max(Y)+1
G=[]
for row in range(0,DR+3):
	G.append(["."]*(RC-LC+1))
def rep():
	for i,l in enumerate(G):print(i,"".join(l))
rep()
for path in LINES:
	corners=path.split(" -> ")
	for a,b in zip(corners,corners[1:]):
		print(a,b)
		i,j=eval(a)
		k,l=eval(b)
		if i==k:
			if j>l:j,l=l,j
			lp=l-j
			XP=[i]*(lp+1)
			YP=list(range(j,l+1))
		else:
			if i>k:i,k=k,i
			lp=k-i
			XP=list(range(i,k+1))
			YP=[j]*(lp+1)
		print(i,j,k,l,lp)
		print (XP,YP)	
		for x,y in zip(XP,YP):
			G[y][x-LC]="#"
G[0][500-LC]="+"
rep()
sand=0
while True:
	sand+=1
	print("sand",sand)
	r,c=0,500
	while True:
		print(r,c)
		while G[r+1][c-LC]==".":
			r+=1
			print(r,c,DR)
			if r==DR+2:
				print (sand-1)
				exit()
		if G[r+1][c-LC-1]==".":
			r+=1
			c-=1
			continue
		if G[r+1][c-LC+1]==".":
			r+=1
			c+=1
			continue
		G[r][c-LC]="o"
		break
	rep()
	# ~ input()
print(sand-1)
