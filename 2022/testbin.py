#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
stobit={}
bittos={}
z=["a","b","c","d","e","f"]
for i,k in enumerate(z):
	stobit[k]=1<<i
	bittos[1<<i]=k
print(stobit)
print(bittos)
allin=2**len(z)-1
rem="a"
remn=allin^stobit[rem]
base=1
for bit in bin(remn)[:1:-1]:
	if int(bit):print(bittos[base])
	base=base<<1
print([2**i for i, v in enumerate(bin(remn)[:1:-1]) if int(v)])
