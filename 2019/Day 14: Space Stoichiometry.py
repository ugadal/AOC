#!/usr/bin/env python
# -*- coding: utf-8 -*-
fn,part="d14.txt",6
sep="\n\n"
import math
data=open(fn).read().split(sep)[part]
rules={}
for l in data.splitlines():
	# ~ print(l)
	ing,res=l.split(" => ")
	# ~ print("ing:",ing,"// res:",res)
	q,t=res.split()
	P=ing.split(", ")
	# ~ print(P)
	I={}
	for p in P:
		# ~ print(p)
		x,y=p.split()
		I[y]=int(x)
	rules[t]=(int(q),I)
# ~ print(rules)
def nxtodo():
	return next(k for k,v in todo.items() if v>0 and k!="ORE")
todo={"FUEL":1}
ore={}
done={}
used={}
while True:
	try:target=nxtodo()
	except:break
	needed=todo[target]-done.get(target,0)+used.get(target,0)
	# ~ print("needed",needed,"of",target)
	doneonce,parts=rules[target]
	# ~ print("pack:",doneonce,", recipe:",parts)
	runs=math.ceil(needed/doneonce)
	# ~ print("runs required",runs)
	done[target]=done.get(target,0)+runs*doneonce
	used[target]=used.get(target,0)+todo[target]
	# ~ print("done",done)
	# ~ print("used",used)
	for k,v in parts.items():
		todo[k]=todo.get(k,0)+v*runs
	todo[target]=0
	# ~ print("todo",todo)
print(todo["ORE"])
