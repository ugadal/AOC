#!/usr/bin/env python
# -*- coding: utf-8 -*-
fn,part="d10.txt",3
sep="\n\n"
data=open(fn).read().split(sep)[part].splitlines()
R=[]
for r,line in enumerate(data):
	for c,s in enumerate(line):
		if s=="#":R.append((r,c))
print(len(R))
def pgcd(a,b):
	while b:a,b=b,a%b
	return abs(a)
record=0
for rock in R:
	D=set()
	for target in R:
		if rock==target:continue
		dr=target[0]-rock[0]
		dc=target[1]-rock[1]
		f=pgcd(dr,dc)
		dr/=f
		dc/=f
		D.add((dr,dc))
	visible=len(D)
	if visible>=record:
		record=visible
		print(visible,rock)
