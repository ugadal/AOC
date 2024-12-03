#!/usr/bin/env python
# -*- coding: utf-8 -*-
fn,part="d2.txt",0
OV=list(map(int,open(fn).readline().split(",")))
def check(x,y):
	V=list(OV)
	V[1]=x
	V[2]=y
	pos=0
	a,b,c,d=V[pos:pos+4]
	while True:
		match a:
			case 1:
				V[d]=V[b]+V[c]
			case 2:
				V[d]=V[b]*V[c]
			case 99:
				return V[0]
		pos+=4
		a,b,c,d=V[pos:pos+4]
for x in range(100):
	for y in range(100):
		r=check(x,y)
		if r==19690720:
			print(100*x+y)
			exit()
