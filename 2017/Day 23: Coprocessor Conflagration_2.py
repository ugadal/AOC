#!/usr/bin/env python
# -*- coding: utf-8 -*-
from mylib import manager
inf=open("d23.txt").read().splitlines()
prgm=[]
for rule in inf:prgm.append(rule.split())
state={}
for c in list("abcdefgh"):state[c]=0
state["a"]=1
pos=0
cyc=0
ss="c"
oldb=(state["b"],state["c"])
while True:
	cyc+=1
	op,tar,z=prgm[pos]
	try:factor=int(z)
	except:factor=state[z]
	# ~ print("pre",pos,op,tar,z,factor,state)
	match op:
		case 'set':
			state[tar]=factor
			pos+=1
		case 'sub':
			state[tar]-=factor
			pos+=1
		case 'mul':
			# ~ cmul+=1
			state[tar]*=factor
			pos+=1
		case 'jnz':
			if tar in state:
				if state[tar]:pos+=factor
				else:pos+=1
			else:
				if int(tar):pos+=factor
				else:pos+=1
	if oldb!=(state["b"],state["c"]):print((state["b"],state["c"]),cyc)
	oldb=(state["b"],state["c"])
	print(cyc,(state["b"],state["c"]))
	# ~ input()
