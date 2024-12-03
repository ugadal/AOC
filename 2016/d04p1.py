#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
I=open(0).read().strip().splitlines()
# ~ nzydfxpc-rclop-qwzhpc-qtylyntyr-769[oshgk]
m=re.compile(r"(^\S+)-(\d+)\[(\w+)\]$")
l=re.compile("\w")
goal=0
for i in I:
	print(i)
	a,b,c=m.findall(i)[0]
	b=int(b)
	L=l.findall(a)
	d={s:L.count(s) for s in set(L)}
	mxc=max(d.values())
	R=[]
	while len(R)<5:
		T=[k for k in d if d[k]==mxc]
		R.extend(sorted(T))
		mxc-=1
	R="".join(R[:5])
	if R==c:goal+=b
print(goal)
