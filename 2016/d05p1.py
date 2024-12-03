#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ~ import sympy
import hashlib
kw="ugkcyxxp"
# ~ kw="abc"
z=0
H=[]
while len(H)<8:
	v=kw+str(z)
	if hashlib.md5(v.encode()).hexdigest().startswith("00000"):
		print(z,v,hashlib.md5(v.encode()).hexdigest())
		H.append(hashlib.md5(v.encode()).hexdigest())
	z+=1

print("".join([h[5] for h in H]))
# ~ Your puzzle answer was d4cd2ee1
