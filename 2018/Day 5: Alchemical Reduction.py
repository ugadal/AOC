#!/usr/bin/env python
# -*- coding: utf-8 -*-
line=open("d5.txt").readline().strip()
line=open("d5.txt").readline().strip()
print(f"original length {len(line)}")
pos=0
while pos!=len(line)-1:
	a=line[pos]
	b=line[pos+1]
	if a!=b and a.upper()==b.upper():
		print ("hit",pos,a,b)
		line=line[:pos]+line[pos+2:]
		pos-=2
	pos+=1
	pos=max(pos,0)
print(f"final length {len(line)}")
