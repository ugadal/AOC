#!/usr/bin/env python
# -*- coding: utf-8 -*-

ex="flqrgnkx"
ex="stpzcrnm"
def kh(s):
	LV=list(map(ord,( c for c in s)))
	LV.extend([17, 31, 73, 47, 23])
	L=list(range(256))
	pos=skip=0
	for _ in range(64):
		for v in LV:
			for d in range(v//2):
				L[(pos+d)%256],L[(pos+v-1-d)%256]=L[(pos+v-1-d)%256],L[(pos+d)%256]
			pos+=v+skip
			skip+=1
	# ~ print(L)
	res=""
	V=0
	for a in range(16):
		hsx=L[16*a:16*a+16]
		v=hsx.pop()
		while hsx:v=v^hsx.pop()
		V=V*256+v
		# ~ print(V,v,bin(v),hex(v))
		# ~ res+=hex(v)[-2:]
	return bin(V)
z=0
for r in range(128):
	z+=kh(ex+'-'+str(r))[2:].count('1')
print(z)
# ~ print(kh(ex+"-127"))
# ~ print(bin(0xa0c2017))
