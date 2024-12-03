#!/usr/bin/env python
# -*- coding: utf-8 -*-
fn,part="d2.txt",0
V=list(map(int,open(fn).readline().split(",")))
V[1]=12
V[2]=2
pos=0
a,b,c,d=V[pos:pos+4]
print(a,b,c,d)
while True:
	match a:
		case 1:
			V[d]=V[b]+V[c]
		case 2:
			V[d]=V[b]*V[c]
		case 99:
			print(V[0])
			exit()
	pos+=4
	a,b,c,d=V[pos:pos+4]
