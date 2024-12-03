#!/usr/bin/env python
# -*- coding: utf-8 -*-
from copy import deepcopy as dc
import itertools as it
def rc(n):
	c=1
	while c*(c+1)/2<n:c+=1
	re=c*(c+1)//2
	print(f"{n} is in diag ending in column {c} with val {re}")
	print(f"{n} is in column {c-re+n} row {re-n+1}")
rc(16)
rc(8)
def gn(r,c):
	z=r+c-1
	re=z*(z+1)//2
	print(f"v in row 1 of diag {re}, v is {re-r+1}")
	return re-r+1
	
cyc=gn(2981,3075)
fc=20151125
for op in range(cyc-1):
	fc*=252533
	fc%=33554393
print(fc)
