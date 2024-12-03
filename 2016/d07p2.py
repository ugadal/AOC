#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ~ import sympy
import re
char=[chr(i) for i in range(97,123)]
R=[]
GL=[]
for a in char:
	for b in char:
		if b==a:continue
		aba=re.compile(f"{a}{b}{a}")
		bab=re.compile(f"{b}{a}{b}")
		R.append((aba,bab))
res=0
inb=re.compile("\[(\w+)\]")
L=open(0).read().splitlines()
for l in L:
	n=re.sub(inb,"XXXX",l)
	for aba,bab in R:
		if not aba.search(n):continue
		if any([bab.search(ss) for ss in inb.findall(l)]):
			GL.append(l)
			print(l,aba,bab)
			break
print(len(GL))
print(len(set(GL)))

