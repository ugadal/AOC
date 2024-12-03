#!/usr/bin/env python
# -*- coding: utf-8 -*-
lim=29000000
# ~ R=[]
hmx=3000000
H=[0]*(hmx+1)
elf=0
rec=float('inf')
while elf<=hmx:
	elf+=1
	am=11*elf
	pos=elf
	while pos<=elf*50 and pos<=hmx:
		H[pos]+=am
		if H[pos]>lim:
			if pos<rec:
				rec=pos
				print(pos,elf,H[pos])
		pos+=elf
	# ~ print(elf,H)
# ~ Your puzzle answer was 665280
# ~ print(H)
# ~ Your puzzle answer was 705600.

