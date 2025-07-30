#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
t=0
# ~ for line in ex.splitlines():
for block in open("d13.txt").read().split("\n\n"):
	print (block)
	G=[[ch for ch in line] for line in block.splitlines()]
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
