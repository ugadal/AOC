#!/usr/bin/env python3
#
# ~ from functools import cache
from collections import deque
from functools import cache
import itertools as it
sep="\n\n"
fn,part="d22.txt",0

def sng(i):
	while True:
		# ~ yield i
		i=i^(i<<6)
		i=i%16777216
		i=i^(i>>5)
		i=i%16777216
		i=i^(i<<11)
		i=i%16777216
		yield i
def nx(g,c):
	for x in range(c-1):next(g)
	return next(g)
z=sng(123)
t=0
M=map(int,open(fn).read().splitlines())
for x in M:
	g=sng(x)
	v=nx(g,2000)
	t+=v
print(t)
