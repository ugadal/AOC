#!/usr/bin/env python
# -*- coding: utf-8 -*-
fn,part="d1.txt",1
data=open(fn).read().split("\n\n")[part].splitlines()
data=list(map(int,data))
import itertools as it
for a,b in it.combinations(data,2):
	if a+b!=2020:continue
	print(a*b)
for a,b,c in it.combinations(data,3):
	if a+b+c!=2020:continue
	print(a*b*c)
	break
