#!/usr/bin/env python
# -*- coding: utf-8 -*-
B={}
R={}
V=[]
mxb=0
for line in open(0).read().splitlines():
	if line.startswith("value"):
		# ~ value 23 goes to bot 76
		_,v,_,_,_,b=line.split()
		v=int(v)
		b=int(b)
		V.append((v,b))
		if b>mxb:mxb=b
	# ~ bot 101 gives low to bot 46 and high to bot 111
	if line.startswith("bot "):
		E=line.split()
		bid=int(E[1])
		lot=int(E[6])
		hit=int(E[11])
		mxb=max(mxb,bid,lot,hit)
	R[bid]=(lot,hit)
print(mxb)
for x in range(mxb+1):B[x]=[]
for a,b in V:B[b].append(a)
# ~ print (B)
# ~ print("=====")
# ~ print ([(i,k) for i,k in B.items() if len(k)>=2])
# ~ print("=====")
gottwo=[i for i,k in B.items() if len(k)>=2]
print (gottwo)
while True:
	for k in gottwo:
		lot,hit=R[k]
		a,b=B[k]
		B[k]=[]
		if a>b:a,b=b,a
		if (a,b)==(17,61):
			print(k)
			exit()
		B[lot].append(a)
		B[hit].append(b)
	gottwo=[i for i,k in B.items() if len(k)>=2]
		
	
