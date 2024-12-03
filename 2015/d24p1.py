#!/usr/bin/env python
# -*- coding: utf-8 -*-
from copy import deepcopy as dc
import itertools as it
V=list(map(int,[line for line in open(0).readlines()]))
SV=set(V)
tt=sum(V)
pc=tt//3
no=len(V)
def qe(C):
	r=1
	for c in C:r*=c
	return r
def yta():
	for hm in range(1,no-2):
		f=False
		for comb in it.combinations(V,hm):
			if sum(comb)==pc:
				yield comb
				f=True
		if f:break
def canbesplit(L):
	for hm in range(len(L)-2):
		for comb in it.combinations(L,hm):
			return True
	return False
central=list(yta())
print (len(central))
rec=float('inf')
for c in central:
	# ~ print(c)
	R=list(SV-set(c))
	if canbesplit(R):
		q=qe(c)
		if q<=rec:
			rec=q
			print(c,qe(c))
	
