#!/usr/bin/env python
# -*- coding: utf-8 -*-
from mylib import manager
inf=open("d23.txt").read().splitlines()
prgm=[]
for rule in inf:prgm.append(rule.split())
state={}
for c in list("abcdefgh"):state[c]=0
pos=0
cmul=0
while True:
	op,tar,z=prgm[pos]
	try:factor=int(z)
	except:factor=state[z]
	print("pre",pos,op,tar,z,factor,state)
	match op:
		case 'set':
			state[tar]=factor
			pos+=1
		case 'sub':
			state[tar]-=factor
			pos+=1
		case 'mul':
			cmul+=1
			state[tar]*=factor
			pos+=1
		case 'jnz':
			if tar in state:
				if state[tar]:pos+=factor
				else:pos+=1
			else:
				if int(tar):pos+=factor
				else:pos+=1
	print("post",pos,op,tar,z,factor,state,cmul)
	# ~ input()
