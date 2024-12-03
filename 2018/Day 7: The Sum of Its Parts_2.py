#!/usr/bin/env python
# -*- coding: utf-8 -*-
fn="d7.txt"
inp=open(fn).read().split("\n\n")[1].splitlines()
D={}
Status={}
ne=30
td=60
ct=0
oa=ord("A")-1
order=[]
for line in inp:
	a=line.split()[1]
	b=line.split()[7]
	if b in D:D[b].append(a)
	else:D[b]=[a]
	Status[a]="todo"
	Status[b]="todo"
NT={}
yettostart=[k for k,v in Status.items() if v=="todo"]
yettostart.sort()
startable=[k for k in yettostart if k in D and all(Status[z]=="done" for z in D[k])]
startable.extend((k for k in yettostart if k not in D))
startable.sort()
for targ in startable[:ne]:
	Status[targ]="busy"
	eta=ct+ord(targ)-oa+td
	if eta in NT:NT[eta].append(targ)
	else:NT[eta]=[targ]
while True:
	ct=nt=min([t for t in NT.keys()])
	targs=NT[nt]
	targs.sort()
	for targ in targs:
		Status[targ]="done"
		order.append(targ)
	NT.pop(nt)

	yettostart=[k for k,v in Status.items() if v=="todo"]
	yettostart.sort()
	if not yettostart:break
	startable=[k for k in yettostart if k in D and all(Status[z]=="done" for z in D[k])]
	startable.extend((k for k in yettostart if k not in D))
	startable.sort()
	currbusy=len(NT)
	for targ in startable[:ne-currbusy]:
		Status[targ]="busy"
		eta=ct+ord(targ)-oa+td
		if eta in NT:NT[eta].append(targ)
		else:NT[eta]=[targ]
	print(NT)
