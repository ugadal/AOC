#!/usr/bin/env python
# -*- coding: utf-8 -*-
fn="d13.txt"
Parts=open(fn).read().split("\n\n")
res=0
for line in Parts[1].splitlines():
	t,d=map(int,line.split(": "))
	if t%(2*(d-1))==0:res+=t*d
print(res)
