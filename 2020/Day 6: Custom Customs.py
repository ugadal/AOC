#!/usr/bin/env python
# -*- coding: utf-8 -*-
fn,part="d6.txt",0
data=open(fn).read().split("\n\n")
res=0
for block in data:
	q=set()
	for line in block.splitlines():
		for iq in line:
			q.add(iq)
	res+=len(q)
print("p1:",res)
res=0
for block in data:
	q=[]
	p=0
	for line in block.splitlines():
		p+=1
		q.extend(list(line))
	for i in set(q):
		if q.count(i)==p:res+=1
print("p2:",res)
