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
print(Known)
todo= T.splitlines()
while todo:
	cl=todo.pop(0)
	a,op,b,unused,target=cl.split()
	print(len(todo),a,op,b,target)
	if op=="OR":
		# ~ input()
		if any([Known.get(a,False),Known.get(b,False)]):
			Known[target]=True
		else:todo.append(cl)
		continue
	if op=="AND":
		if a in Known and b in Known:
			Known[target]=Known[a] and Known[b]
			continue
		if a in Known:
			if Known[a]==False:
				Known[target]=False
				continue
		if b in Known:
			if Known[b]==False:
				Known[target]=False
				continue
		todo.append(cl)
		continue
	if op=="XOR":
		if target in Known:exit()
	if not all([a in Known,b in Known]):
		todo.append(cl)
		continue
	a=Known[a]
	b=Known[b]
	match op:
		case "XOR":
			if target in Known:
				input()
			Known[target]=a ^ b
	print(len(todo))
