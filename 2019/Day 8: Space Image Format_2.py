#!/usr/bin/env python
# -*- coding: utf-8 -*-
fn,part="d8.txt",0
pix=open(fn).readline().strip()
def job(r,c,line):
	dim=r*c
	pos=0
	maxz=float("inf")
	da=["2"]*dim
	print("".join(da))
	while pos<=len(line)-dim:
		cl=line[pos:pos+dim]
		# ~ print("pre","".join(da))
		# ~ print("pre","".join(cl))
		da=[b if a=="2" else a for a,b in zip(da,cl)]
		# ~ print("".join(da))
		pos+=dim
	pos=0
	for k in range(r):
		print("".join(da[pos:pos+c]))
		pos+=c
job(2,2,"0222112222120000")
job(6,25,pix)
"""
XXX  X  X XXXX XXX  XXX  
X  X X  X    X X  X X  X 
X  X X  X   X  XXX  X  X 
XXX  X  X  X   X  X XXX  
X X  X  X X    X  X X    
X  X  XX  XXXX XXX  X    
"""
