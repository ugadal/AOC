#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ~ import sympy
floor=0
for i,c in enumerate(open(0).read().strip()):
	if c=="(":floor+=1
	else:floor-=1
	if floor==-1:
		print(i+1)
		exit()
print (floor)
