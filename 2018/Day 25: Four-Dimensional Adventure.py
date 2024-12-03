#!/usr/bin/env python
# -*- coding: utf-8 -*-
fn,part="d25.txt",3
parts=open(fn).read().split("\n\n")
data=parts[part]
Points=[]
Done=[]
def calcd(pa,pb):
	return sum(abs(x-y) for x,y in zip(pa,pb))
for line in data.splitlines():
	a,b,c,d=map(int,line.split(","))
	Points.append((a,b,c,d))
constel={}
cn=1
cc=[Points.pop()]
while Points:
	for p in Points:
		# ~ print(p)
		if p in cc:continue
		if any(calcd(p,aic)<=3 for aic in cc):
			print("adding ",p)
			cc.append(p)
			Points.remove(p)
			break
	else:
		print("no addition,=>next constel")
		constel[cn]=list(cc)
		cn+=1
		cc=[Points.pop()]
for k,v in constel.items():
	print(k,v)
print(cn,cc)
print(len(constel)+1)
