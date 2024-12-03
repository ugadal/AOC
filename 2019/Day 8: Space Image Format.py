#!/usr/bin/env python
# -*- coding: utf-8 -*-
fn,part="d8.txt",0
pix=open(fn).readline().strip()
pos=0
maxz=float("inf")
while pos<len(pix)-150:
	cl=pix[pos:pos+150]
	nbz=cl.count("0")
	if nbz<maxz:
		maxz=nbz
		print(cl.count("1")*cl.count("2"))
	pos+=150
