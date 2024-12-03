#!/usr/bin/env python
# -*- coding: utf-8 -*-
lim=29000000
# ~ R=[]
P=[2,3,5,7,11,13,17,19,21,23,29,31,37,41,43,47,53]
def dec(n):
	V=[]
	for pr in P:
		po=0
		while not n%pr:
			n//=pr
			po+=1
		V.append(po)
	return (V+[n])
g=0
def sd(n):
	g=0
	for m in range(1,n+1):
		if n%m==0:
			if n<=50*m:
				g+=m
	return g,11*g,11*g>lim


 # ~ ~ 665280 /2/2/2/2/2/2/3/3/3/5/7/11
x=705600
while True:
	onzaines,v,t=sd(x)
	if t:print (x,onzaines,v,dec(x))
	x-=2
	if not x%1000:print(x)
