#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ~ import sympy
import re
ttl=0
ttc=0
re.compile(r'\\')
for l in open("d8.txt").read().splitlines():
	ttl+=len(l)
	ttc+=len(eval(l))
	print(len(l),len(eval(l)))
	
print(ttl,ttc,ttl-ttc)
