#!/usr/bin/env python
# -*- coding: utf-8 -*-
fn,part="d14.txt",2
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
ore={}
while todo:
	qt,t=todo.pop(0)# 1 fuel
	td,rec=rules[t] #td:1   rec:{a:7 , e:1]
	print(td)
	print(rec)
	if "ORE" in rec:
		ore[t]=ore.get(t,0)+qt
		continue
	this={}
	while qt>0:
		for x,y in rec.items():
			this[x]=this.get(x,0)+y
		qt-=td
	print(this)
	for k,v in this.items():todo.append((v,k))
	print("todo",todo)
	# ~ print(ore)
	input()
print(ore)
tt=0
for k,needed in ore.items():
	print(k,needed)
	done,od=rules[k]
	print(done,od)
	while needed>0:
		tt+=od["ORE"]
		needed-=done
print(tt)
