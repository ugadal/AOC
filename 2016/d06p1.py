#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ~ import sympy
L=open(0).read().splitlines()
print(L[:3])
R=[]
for C in zip(*L):
	char=sorted(set(C))
	print(char)
	cou=[C.count(c) for c in char]
	mv=max(cou)
	R.append(next((c for c in char if C.count(c)==mv)))
print ("".join(R))
