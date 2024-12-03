#!/usr/bin/env python
# -*- coding: utf-8 -*-
fn="d8.txt"
inp=open(fn)
V=list(map(int,inp.readline().strip().split()))
V=list(map(int,inp.readline().strip().split()))
meta=[]
def treat(n,V):
	print(f"entered with {n} branches to find")
	print(f"data : {V[:12]} ... {V[-12:]}")
	a,b=V[:2]
	print(f"n {n} a {a} b {b}")
	if n==1:
		print("sum of metadata",sum(V[-b:]))
		meta.extend(V[-b:])
		if V[2:-b]:treat(a,V[2:-b])
	if n>1:
		if a==0:
			print("simple case")
			meta.extend(V[2:2+b])
			treat(n-1,V[2+b:])
		else:
			print("hard case")
			return
# ~ treat(1,V)
# ~ print(meta)
# ~ print(sum(meta))
pos=0
while True:
	while V[pos]:pos+=2
	print(pos)
	md=V[pos+1]
	meta.extend(V[pos+2:pos+2+md])
	print(meta)
	V=V[:pos]+V[pos+2+md:]
	print(V)
	pos-=2
	try:V[pos]-=1
	except:
		print(sum(meta))
		exit()
