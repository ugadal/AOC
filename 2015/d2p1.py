#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ~ import sympy
Area=0
ribbon=0
for line in open(0).read().strip().splitlines():
	w,l,h=map(int,(line.split("x")))
	comb=[w*l,w*h,l*h]
	extra=min(comb)
	sides=[w,l,h]
	sides.sort()
	ribbon+=2*sum(sides[:2])+w*l*h
	Area+=2*sum(comb)+extra

print (Area)
print (ribbon)
