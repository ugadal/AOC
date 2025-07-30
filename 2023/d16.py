#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
from pandas import DataFrame as df
def rep(G):
	print("="*20)
	print(df(G))
	print("="*20)
T=open("d16.txt","rb").read()
parta=[]
partb=[]
target=parta
sub=[]
for x,y in zip(T,T[1:]):
	if x==y==10:
		target=partb
		continue
	if y==10:
		sub.append(x)
		target.append(sub)
		continue
	if x==10:
		sub=[]
		continue
	sub.append(x)
for l in parta:print(l)
