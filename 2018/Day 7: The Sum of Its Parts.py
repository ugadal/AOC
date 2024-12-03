#!/usr/bin/env python
# -*- coding: utf-8 -*-
fn="d7.txt"
inp=open(fn).read().split("\n\n")[1].splitlines()
D={}
Status={}
for line in inp:
	a=line.split()[1]
	b=line.split()[7]
	if b in D:D[b].append(a)
	else:D[b]=[a]
	Status[a]=False
	Status[b]=False
for k,v in D.items():
	print(k,v)
yettostart=[k for k,v in Status.items() if not v]
yettostart.sort()
start=[k for k in Status.keys() if not k in D]
start.sort()
start=start[0]
Status[start]=True
order=[start]
while True:
	yettostart=[k for k,v in Status.items() if not v]
	if not yettostart:
		print("".join(order))
		break
	startable=[k for k in yettostart if k in D and all(Status[z] for z in D[k])]
	startable.extend((k for k in yettostart if k not in D))
	startable.sort()
	nv=startable[0]
	order.append(nv)
	Status[nv]=True
	
	
