#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ~ #1 @ 37,526: 17x23
lines=open("d4.txt").read().split("\n\n")[1].splitlines()
lines.sort()
ST={}
for line in lines:
	parts=line.split()
	if parts[-1]=="shift":
		gid=int(parts[3][1:])
		print("guard",gid)
		continue
	if parts[-1]=="asleep":
		bs=int(parts[1][:-1].split(":")[1])
		print("begins sleeping",bs)
		continue
	if parts[-1]=="up":
		es=int(parts[1][:-1].split(":")[1])
		print("ends sleeping",es)
		ST[gid]=ST.get(gid,0)+es-bs
		continue
mt=max(ST.values())
mas=next(k for k,v in ST.items() if v==mt)
print ("most asleep",mas)
Mi=[0]*60
for line in lines:
	parts=line.split()
	if parts[-1]=="shift":
		gid=int(parts[3][1:])
		print("guard",gid)
		continue
	if gid!=mas:continue
	if parts[-1]=="asleep":
		bs=int(parts[1][:-1].split(":")[1])
		print("begins sleeping",bs)
		continue
	if parts[-1]=="up":
		es=int(parts[1][:-1].split(":")[1])
		print("ends sleeping",es)
		ST[gid]=ST.get(gid,0)+es-bs
		for m in range (bs,es):Mi[m]+=1
mm=max(Mi)
mm=next(p for p,k in enumerate(Mi) if k==mm)
print (mas,mm,mas*mm)
