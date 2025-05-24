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
for d,v in enumerate(data[1].split(",")):
	if v=="x":continue
	print(d,v,int(v)+d)
print
"""

7,13,x,x,59,x,31,19
	x%7 and x+1%13 == 0 
	x=77 recur=169 7*13
	
	x % 7 and x+1 % 13  x+4 % 59  == 0 
	x=?  recur = 9971

< 13-(x+1%13) <59-

"""
t=p=5713406
while True:
	if t%29 or (t+23)%37 or (t+29)%433 or(t+42)%13 or (t+43)%17:
		t+=1
		continue
	print(t,t-p)
	p=t
	input()
	t+=6039917
