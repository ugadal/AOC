#!/usr/bin/env python3
#
from functools import cache
fn,part="d11.txt",0
data=open(fn).readline().split()
@cache
def blink(v,bn):
	if bn==0:return 1
	if v=="0":return blink("1",bn-1)
	lv=len(v)
	if lv%2==0:return blink(str(int(v[:lv//2])),bn-1)+blink(str(int(v[lv//2:])),bn-1)
	return blink(str(int(v)*2024),bn-1)
print(sum(blink(x,75) for x in data))
print(blink.cache_info())
