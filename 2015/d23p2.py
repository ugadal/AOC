#!/usr/bin/env python
# -*- coding: utf-8 -*-
from copy import deepcopy as dc
import itertools as it
bf=open("d23.txt")
D={}
D["a"]=1
D["b"]=0
I=bf.read().splitlines()
cp=0
while True:
	inst=I[cp]
	match inst.split():
		case ['hlf',*arg]:
			k=arg[0]
			D[k]//=2
			cp+=1
			print(inst,arg,D,cp)
		case ['tpl',*arg]:
			k=arg[0]
			D[k]*=3
			cp+=1
			print(inst,arg,D,cp)
		case ['inc',*arg]:
			k=arg[0]
			D[k]+=1
			cp+=1
			print(inst,arg,D,cp)			
		case ['jmp',*arg]:
			cp=eval(f"{cp}{arg[0]}")
			print(inst,arg,D,cp)
		case ['jie',*arg]:
			k=arg[0][0]
			off=arg[1]
			if D[k]%2==0:cp=eval(f"{cp}{off}")
			else:cp+=1
			print(inst,arg,D,cp)
		case ['jio',*arg]:
			k=arg[0][0]
			off=arg[1]
			if D[k]==1:cp=eval(f"{cp}{off}")
			else:cp+=1
			print(inst,arg,D,cp)
			
