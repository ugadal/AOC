#!/usr/bin/env python
# -*- coding: utf-8 -*-
D={}
I=open(0).read().splitlines()
nbi=len(I)
curr=0
D["c"]=1
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
			
print(D)
