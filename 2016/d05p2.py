#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ~ import sympy
import hashlib
kw="ugkcyxxp"
# ~ kw="abc"
z=0
H=['x']*8
valp=list("01234567")
while H.count("x"):
	v=kw+str(z)
	h=hashlib.md5(v.encode()).hexdigest()
	if h.startswith("00000"):
		if h[5] in valp and H[int(h[5])]=='x':
			H[int(h[5])]=h[6]
		print(z,v,hashlib.md5(v.encode()).hexdigest())
		# ~ H.append(hashlib.md5(v.encode()).hexdigest())
	z+=1
print ("".join(H))
