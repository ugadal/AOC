#!/usr/bin/env python3
#
#  Day 1: Secret Entrance.py
sep="\n\n"
fn,part="d1.txt",1
data=open(fn).read().split(sep)[part]
res=50
count=0
for l in data.splitlines():
	v=int(l[1:])
	match l[0]:
		case 'L':res-=v
		case 'R':res+=v
	res=res%100
	if res==0:count+=1
print("p1 :",count)
oldres=res=50
count=0

for l in data.splitlines():
	v=int(l[1:])
	count+=v//100
	v=v%100
	match l[0]:
		case 'L':res-=v
		case 'R':res+=v
	if res==0:count+=1
	elif oldres and res!=res%100:count+=1
	res=res%100
	oldres=res
print("p2 :",count)
