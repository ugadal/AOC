#!/usr/bin/env python
# -*- coding: utf-8 -*-
part=0
import re
import sys
cp=str(sys.argv[0])
dre=re.compile(r"^Day (\d+):")
day=dre.findall(cp)[0]
fn=f"d{day}.txt"
rules,tick,near=open(fn).read().split("\n\n")
V=set()
for line in rules.splitlines():
	r=line.split(": ")[1].split(" or ")
	for p in r:
		a,b=list(map(int,p.split("-")))
		for v in range(a,b+1):V.add(v)
res=0
for line in near.splitlines()[1:]:
	for v in map(int,line.split(",")):
		if not v in V:res+=v

print("p1:",res)

VT=[]
for line in near.splitlines()[1:]:
	tv=list(map(int,line.split(",")))
	if all(v in V for v in tv):
		VT.append(tv)
print(VT)
R={}
for line in rules.splitlines():
	rn,r=line.split(": ")#[1].split(" or ")
	ts=R[rn]=set()
	for p in r.split(" or "):
		a,b=list(map(int,p.split("-")))
		for v in range(a,b+1):ts.add(v)
print(R)
RN=list(R.keys())
tl=len(VT[0])
PN={}
for rn in RN:
	print (rn)
	PN[rn]=set()
	for pos in range(tl):
		tv=[t[pos] for t in VT]
		if all(v in R[rn] for v in tv):
			print(pos,"ok for ",rn)
			PN[rn].add(pos)
print(PN)
todo=list(PN.keys())
done={}
while True:
	try:k=next(k for k in todo if len(PN[k])==1)
	except:break
	print(k)
	v=PN[k]
	done[k]=set(v)
	print(k,v)
	todo.remove(k)
	for k in todo:
		PN[k]-=v
	# ~ input()
print("todo",todo)
print(done)
vc=[done[k] for k in RN if k.startswith("departure")]
print(vc)
tick=tick.splitlines()[1]
tick=list(map(int,tick.split(",")))
print(tick)
val=[tick[p.pop()] for p in vc]
print(val)
r=1
for v in val:r*=v
print(r)
