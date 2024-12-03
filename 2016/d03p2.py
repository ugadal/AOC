#!/usr/bin/env python
# -*- coding: utf-8 -*-
G=[list(map(int,line.split())) for line in open(0).read().strip().splitlines()]
G=list(zip(*G))
print (G[0][:10])
ok=0
T=[]
for row in G:T.extend(row)
while T:
	a=T.pop()
	b=T.pop()
	c=T.pop()
	if a+b>c and a+c>b and b+c>a:ok+=1
print(ok)
