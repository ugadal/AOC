#!/usr/bin/env python
# -*- coding: utf-8 -*-
I=open(0).read().strip().splitlines()
ok=0
for line in I:
	a,b,c=map(int,line.split())
	if a+b>c and a+c>b and b+c>a:ok+=1
print(ok)
