#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ~ import sympy
import hashlib
kw="yzbqklnj"
z=0
while True:
	v=kw+str(z)
	if hashlib.md5(v.encode()).hexdigest().startswith("000000"):
		print(z,v)
		exit()
	z+=1

