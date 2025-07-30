#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
t=0
exp="""#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#"""
from copy import deepcopy as dc
import pandas as pd
def rep(G):
	print (pd.DataFrame(G))
def compute(D):
	v=0
	for a,_ in D["rows"]:v+=100*(a+1)
	for a,_ in D["columns"]:v+=a+1
	return v
def comparemir(New,Orig):
	newlines={}
	for k in New.keys():
		newlines[k]=[]
	for k in New.keys():
		if any([r not in Orig[k] for r in New[k]]):
			newlines[k].extend([r for r in New[k] if r not in Orig[k] ])
			return True,newlines
	return False,newlines
def fixit(G,a,b,col):
	# ~ print(a,b,col)
	Z=dc(G)
	# ~ print(f"rows {len(Z)},cols {len(Z[0])}")
	if col:Z=[list(line) for line in zip(*Z)]
	pos=[x==y for x,y in zip(Z[a],Z[b])].index(False)
	# ~ print("pos a",pos)
	if Z[a][pos]=="." :Z[a][pos]="#" 
	else:Z[a][pos]="." 
	if col:Z=[list(line) for line in zip(*Z)]
	ZZ=dc(G)
	if col:ZZ=[list(line) for line in zip(*ZZ)]
	pos=[x==y for x,y in zip(ZZ[a],ZZ[b])].index(False)
	# ~ print("pos b",pos)
	if ZZ[b][pos]=="." :ZZ[b][pos]="#" 
	else:ZZ[b][pos]="." 
	if col:ZZ=[list(line) for line in zip(*ZZ)]
	return Z,ZZ
def getlines(G):
	R={}
	for direc in ("rows","columns"):
		R[direc]=[]
		for i,(a,b) in enumerate(zip(G,G[1:])):
			if a==b:
				A=G[:i+1]
				B=G[i+1:2*i+2]
				A.reverse()
				if all(x==y for x,y in zip(A,B)):
					R[direc].append((i,i+1))
		G=list(zip(*G))
	return(R)
	
def findpossmud(block):
	G=[[ch for ch in line] for line in block.splitlines()]
	ORIG=dc(G)
	rep(ORIG)
	original=getlines(G)
	print("original",original,compute(original))
	for direc in ("rows","columns"):
	# ~ for direc in ["rows"]:
		for ia,a in enumerate(G):
			for ib,b in enumerate(G[ia+1:]):
				if [x==y for x,y in zip(a,b)].count(False)==1:
					print(f"possible smudge between {direc} {ia} {ia+ib+1}")
					fixeda,fixedb=fixit(ORIG,ia,ia+ib+1,direc=="columns")
					newmir=getlines(fixeda)
					if newmir==original:print("no changes",newmir)
					else : 
						print("Changed!!",newmir,compute(newmir))
						test,rdic=comparemir(newmir,original)
						if test:
							print("ok",rdic,compute(rdic))
							return compute(rdic)
					newmir=getlines(fixedb)
					if newmir==original:print("no changes",newmir)
					else : 
						print("Changed!!",newmir,compute(newmir))
						test,rdic=comparemir(newmir,original)
						if test:
							print("ok",rdic,compute(rdic))
							return compute(rdic)


		G=list(zip(*G))
z=0
# ~ for block in exp.split("\n\n"):
for block in open("d13.txt").read().split("\n\n"):
	# ~ print (block)
	findpossmud(block)
	z+=findpossmud(block)
print(z)
exit()
	
def getlines(G):
	# ~ G=[[ch for ch in line] for line in block.splitlines()]
	# ~ print(G)
	v=0
	for i,(a,b) in enumerate(zip(G,G[1:])):
		if a==b:
			A=G[:i+1]
			B=G[i+1:2*i+2]
			A.reverse()
			for l in A:print("A",l)
			print()
			for l in B:print("B",l)
			print()
			print("h",i,list((x==y for x,y in zip(A,B))))
			if all(x==y for x,y in zip(A,B)):
				v+=100*(i+1)
				print("horizontal",i)
	G=list(zip(*G))
	# ~ print(G)
	for i,(a,b) in enumerate(zip(G,G[1:])):
		if a==b:
			A=G[:i+1]
			B=G[i+1:2*i+2]
			A.reverse()
			for l in A:print("A",l)
			print()
			for l in B:print("B",l)
			print()
			print("v",i,list((x==y for x,y in zip(A,B))))
			if all(x==y for x,y in zip(A,B)):
				v+=i+1
				print("vertical",i)
	t+=v
	print(v,t)
	# ~ input()
print(t)
