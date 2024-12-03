#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ~ D={}
I=open("d25.txt").read().splitlines()
nbi=len(I)
curr=0
def go(v):
	D={}
	D["a"]=v
	curr=0
	while curr!=nbi:
		il=I[curr]	
		match il.split():
			case ['cpy',*arg]:
				a,b=arg
				if a.isdigit():a=int(a)
				else:a=D.get(a,0)
				D[b]=a
				curr+=1
			case ['jnz',*arg]:
				a,b=arg
				if a.isdigit():a=int(a)
				else:a=D.get(a,0)
				b=int(b)
				if a:curr+=b
				else:curr+=1
			case ['inc',var]:
				D[var]+=1
				curr+=1
			case ['dec',var]:
				D[var]-=1
				curr+=1
			case ['out',var]:
				yield D[var]
				curr+=1
seed=0			
while True:
	print(seed)
	z=go(seed)
	r=[]
	for _ in range(10):
		tr=next(z)
		if tr not in (0,1):break
		r.append(tr)
	if len(set(r))==2:
		print(seed,r)
		input()
	seed+=1
