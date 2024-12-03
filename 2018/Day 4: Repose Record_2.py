#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ~ #1 @ 37,526: 17x23
lines=open("d4.txt").read().split("\n\n")[1].splitlines()
lines.sort()
ST={}
G={}
for line in lines:
	parts=line.split()
	if parts[-1]=="shift":
		gid=int(parts[3][1:])
		tgm=G.get(gid,[0]*60)
		print("guard",gid,tgm)
		continue
	if parts[-1]=="asleep":
		bs=int(parts[1][:-1].split(":")[1])
		print("begins sleeping",bs)
		continue
	if parts[-1]=="up":
		es=int(parts[1][:-1].split(":")[1])
		print("ends sleeping",es)
		G[gid]=tgm
		for m in range (bs,es):tgm[m]+=1
		continue
print (G)
masm=max([max(z) for z in G.values()])
for gid,mm in G.items():
	if masm in mm:
		mmi=mm.index(masm)
		print (gid,mmi,gid*mmi)
