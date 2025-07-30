#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
fn="/root/day3.txt"
df=open(fn)
total=0
a=df.readline().strip()
b=df.readline().strip()
c=df.readline().strip()
while a:
	i=list(set(a)&set(b)&set(c))[0]
	if i>="a":total+=ord(i)-96
	else:total+=ord(i)-38
	a=df.readline().strip()
	b=df.readline().strip()
	c=df.readline().strip()	
print (total)
