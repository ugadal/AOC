#!/usr/bin/env python
# -*- coding: utf-8 -*-
fn,part="d14.txt",1
sep="\n\n"
data=open(fn).read().split(sep)[part]
rules={}
for l in data.splitlines():
	print(l)
	ing,res=l.split(" => ")
	print("ing:",ing,"// res:",res)
	q,t=res.split()
	P=ing.split(", ")
	print(P)
	I={}
	for p in P:
		print(p)
		x,y=p.split()
		I[y]=int(x)
	rules[t]=(int(q),I)
print(rules)
todo=[(1,"FUEL")]
ore=[]
while todo:
	qt,t=todo.pop(0)# 1 fuel
	if t=="ORE":
		ore.append(qt)
		continue
	td,rec=rules[t] #td:1   rec:{a:7 , e:1]
	print(td)
	print(rec)
	for x,y in rec.items():
		todo.append((qt*y/td,x))
	print(todo)
	print(ore)
	# ~ input()
print(ore)
