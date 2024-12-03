#!/usr/bin/env python
# -*- coding: utf-8 -*-
exp="""498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9"""
X=[]
Y=[]
LINES=exp.splitlines()
LINES=open("d14.txt").read().splitlines()
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
Busy=set()
Sand=set()
for row in range(0,DR+3):
	G.append(["."]*(RC-LC+1))
def rep():
	lr=min([r for r,c in Busy|Sand])
	hr=max([r for r,c in Busy|Sand])
	lc=min([c for r,c in Busy|Sand])
	hc=max([c for r,c in Busy|Sand])
	for row in range(lr,hr+1):
		print ("".join(["#" if (row,c) in Busy else "o" if (row,c) in Sand else "." for c in range(lc,hc+1)]))
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
			Busy.add((y,x))
sand=0
rep()
# ~ exit()
while True:
	sand+=1
	print("sand",sand)
	r,c=0,500
	while True:
		# ~ if r==DR+2:break
		while (r+1,c) not in Busy|Sand and r<=DR:
			r+=1
		if r>DR:
			Sand.add((DR,c))
			rep()
			break
		if (r+1,c-1) not in Busy|Sand:
			r+=1
			c-=1
			continue
		if (r+1,c+1) not in Busy|Sand:
			r+=1
			c+=1
			continue
		if (r,c)==(0,500):
			print(sand)
			exit()
		Sand.add((r,c))
		break
	# ~ rep()
	# ~ input()
print(sand-1)
