#!/usr/bin/env python3
#
from functools import cache
from collections import deque
sep="\n\n"
fn,part="d19.txt",0
parts=open(fn).read().split(sep)[part].split(', ')
wanted=open(fn).read().split(sep)[part+1].splitlines()
print( parts)
parts.sort()
parts.reverse()
print(wanted)
@cache
def possible(s):
	todo=deque([s])
	while todo:
		target=todo.popleft()
		# ~ print(target)
		if not target:return 1
		return sum(possible(target[len(p):]) for p in parts if target.startswith(p))
		# ~ for p in parts:
			# ~ if target.startswith(p):
				# ~ todo.append(target[len(p):])
				# ~ print(target,p, target[len(p):])
	return False
cc=0				
for s in wanted:
	print(s)
	if possible(s):cc+=1
print(cc)
