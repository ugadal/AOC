#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
T=json.loads(open("d12.txt").read().strip())
def contains(t):
	if t=="red":return 0
	if type(t)==list:
		return sum([contains(x) for x in t])
	if type(t)==dict:
		if list(t.values()).count("red"):return 0
		return sum([contains(x) for x in t.values()])
	if type(t)==int:return t
	if t.isdigit():return int(t)
	return 0
print(contains(T))
