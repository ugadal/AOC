#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ~ import sympy
import re
R=[]
char=[chr(i) for i in range(97,123)]
for a in char:
	for b in char:
		if b==a:continue
		R.append(re.compile(f"{a}{b}{b}{a}"))
res=0
inb=re.compile("\[(\w+)\]")
L=open(0).read().splitlines()
for l in L:
	n=re.sub(inb,"X",l)
	if any([p.search(n) for p in R]):
		if not any([p.search(ss) for ss in inb.findall(l) for p in R]):
			res+=1
print(res)
