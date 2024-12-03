#!/usr/bin/env python
# -*- coding: utf-8 -*-
fn="d13.txt"
Parts=open(fn).read().split("\n\n")
RULES=[]
for line in Parts[1].splitlines():
	t,d=map(int,line.split(": "))
	RULES.append((t,2*(d-1)))

delay=-1
while True:
	res=True
	delay+=1
	# ~ print(delay)
	for t,d in RULES:
		if (t+delay)%d==0:
			res=False
			break
	if res:break
print(delay)
