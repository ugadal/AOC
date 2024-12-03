#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ~ import sympy
D=[]
santa=0+0*1j
robot=0+0*1j
D=[santa,robot]
a,b=santa,robot
for d in open(0).read().strip():
	match d:
		case '>':a+=1
		case '<':a-=1
		case '^':a+=1j
		case 'v':a-=1j
	D.append(a)
	a,b=b,a
print(len(D))
print(len(set(D)))
