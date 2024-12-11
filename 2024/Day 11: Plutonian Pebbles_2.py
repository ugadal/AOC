#!/usr/bin/env python3
#
from collections import deque
from functools import wraps
def memoize(func):
    cache = {}
    @wraps(func)
    def wrapper(*args):
        if args in cache:
            return cache[args]
        else:
            result = func(*args)
            cache[args] = result
            return result
    return wrapper

sep="\n\n"
fn,part="d11.txt",0
data=open(fn).readline().split()
@memoize
def blink(v,bn):
	if bn==1:
		if v=="0":return 1
		lv=len(v)
		if lv%2:return 1
		return 2
	else:
		if v=="0":return blink("1",bn-1)
		lv=len(v)
		if lv%2==0:return blink(str(int(v[:lv//2])),bn-1)+blink(str(int(v[lv//2:])),bn-1)
		return blink(str(int(v)*2024),bn-1)
print(blink("125",4))
print(blink("17",4))
print(sum(blink(x,75) for x in data))
