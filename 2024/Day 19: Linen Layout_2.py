#!/usr/bin/env python3
#
from functools import cache
sep="\n\n"
fn,part="d19.txt",2
parts=open(fn).read().split(sep)[part].split(', ')
wanted=open(fn).read().split(sep)[part+1].splitlines()
@cache
def possible(target):
	if not target:return 1
	return sum(possible(target[len(p):]) for p in parts if target.startswith(p))
print ("part 1 :",sum(1 if possible(s) else 0 for s in wanted))
print ("part 2 :",sum(possible(s) for s in wanted))
