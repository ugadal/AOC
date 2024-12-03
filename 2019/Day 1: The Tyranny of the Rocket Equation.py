#!/usr/bin/env python
# -*- coding: utf-8 -*-
fn,part="d1.txt",0
data=open(fn).read().splitlines()
data=map(int,data)
data=map(lambda x: -2+x//3,data)
print(sum(data))
fuel=0
for module in open(fn).read().splitlines():
	module=int(module)
	fn=module//3-2
	fuel+=fn
	while fn>0:
		fn=fn//3-2
		if fn>0:fuel+=fn
print(fuel)
