#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ~ import sympy
floor=0
for c in open(0).read().strip():
	if c=="(":floor+=1
	else:floor-=1
print (floor)
