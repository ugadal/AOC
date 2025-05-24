#!/usr/bin/env python
# -*- coding: utf-8 -*-
part=1
import re
import sys
cp=str(sys.argv[0])
dre=re.compile(r"^Day (\d+):")
day=dre.findall(cp)[0]
fn=f"d{day}.txt"
data=open(fn).read().split("\n\n")[part].splitlines()
st=int(data[0])
def z(st,x):return x-st%x
rec=float("inf")
for v in data[1].split(","):
	if v=="x":continue
	r=z(st,int(v))
	if r<rec:
		rec=r
		t=int(v)
print("p1:",t*rec)
V=[]
for d,v in enumerate(data[1].split(",")):
	if v=="x":continue
	print(d,v)
	V.append((d,int(v)))
print("===")
base,inc=V.pop(0)
t=inc
print(t)
while V:
	off,mod=V.pop(0)
	while True:
		if (t+off)%mod:
			t+=inc
			continue
		break
	base=t
	inc*=mod
	print(f"base: {base} inc: {inc}    ...")
