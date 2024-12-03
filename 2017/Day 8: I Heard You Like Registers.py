#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Day 8
import re
Vars={}
rec=float("-inf")
ms=re.compile("^(\w+) (\w+) (-?\d+) if (\w+) (\S+) (-?\d+)$")
for line in open("d8.txt").read().splitlines():
	tar,op,arg,tv,comp,cv=ms.search(line).groups()
	arg=int(arg)
	tv=Vars.get(tv,0)
	t=eval(f"{tv}{comp}{cv}")
	if t:
		if op=="dec":arg=-arg
		cv=Vars.get(tar,0)
		Vars[tar]=cv+arg
		rec=max(rec,max(Vars.values()))
print("p1:",max(Vars.values()))
print("p2:",rec)
