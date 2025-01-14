#!/usr/bin/env python3
#
# ~ from functools import cache
from collections import deque
from functools import cache
import itertools as it
sep="\n\n"
fn,part="d24.txt",0
K,T=open(fn).read().split(sep)
Known={}
for l in K.splitlines():
	k,v=l.split(": ")
	Known[k]=True if int(v) else False
# ~ print(Known)
todo= T.splitlines()
while todo:
	cl=todo.pop(0)
	a,op,b,unused,target=cl.split()
	# ~ print(len(todo),a,op,b,target)
	if not (a in Known and b in Known):
		# ~ print(a,a in Known,b,b in Known,"skipping")
		todo.append(cl)
		continue
	# ~ print(a,a in Known,b,b in Known,"going on")
	a=Known[a]
	b=Known[b]
	# ~ print(a,op,b)
	# ~ input()
	match op:
		case 'OR':
			Known[target]=a or b
		case 'AND':
			Known[target]=a and b
		case 'XOR':
			Known[target]=a ^ b
nz=[k for k in Known.keys() if k.startswith("z") ]
nz.sort()
nz.reverse()
bs="".join(["1" if Known[k] else "0" for k in nz])
print(int(bs,2))
