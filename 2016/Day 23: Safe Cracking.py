#!/usr/bin/env python
# -*- coding: utf-8 -*-
D={}
I=open(0).read().splitlines()
nbi=len(I)
curr=0
"""
5: 
6:  8428
7 : 12748
8 : 48028
9 : 370558
10: 3636508
11: 39924508,
"""
D["a"]=12
T={}
while curr<nbi:
	# ~ print(curr,D,T)
	il=I[curr]	
	# ~ print(il,T.get(curr,False))
	match il.split():
		case ['tgl', *arg]:
			p=arg[0]
			if p.isdigit():a=int(p)
			else:a=D.get(p,0)
			toggled=T.get(curr,False)
			if toggled:D[p]=D.get(p,0)+1
			else:
				if a==0:T[curr]=True
				else:T[curr+a]=True
			curr+=1
		case ['cpy',*arg]:
			toggled=T.get(curr,False)			
			if not toggled:			
				a,b=arg
				try:a=int(a)
				except:a=D.get(a,0)
				D[b]=a
				curr+=1
			else:
				a,b=arg
				if a.isdigit():a=int(a)
				else:a=D.get(a,0)
				b=D.get(b,0)
				if a:curr+=b
				else:curr+=1				
		case ['jnz',*arg]:
			toggled=T.get(curr,False)
			if not toggled:
				a,b=arg
				if a.isdigit():a=int(a)
				else:a=D.get(a,0)
				# ~ print("a,b",a,b)
				try: b=int(b)
				except:b=D.get(b,0)
				# ~ print("a,b",a,b)
				if a:
					# ~ print("updating curr")
					curr+=b
					# ~ print(curr)
				else:curr+=1
			else: 
				a,b=arg
				if a.isdigit():a=int(a)
				else:a=D.get(a,0)
				if not b.isdigit():D[b]=a
				curr+=1
		case ['inc',var]:
			toggled=T.get(curr,False)
			if not toggled:	D[var]+=1
			else:D[var]-=1
			curr+=1
		case ['dec',var]:
			toggled=T.get(curr,False)
			if not toggled:	D[var]-=1
			else:D[var]+=1
			curr+=1
			
print(D)
