#!/usr/bin/env python3
#
sep="\n\n"
fn,part="d13.txt",1
data=open(fn).read()
# ~ from functools import cache
import re 
bp=re.compile(r"Button\s\S: X\+(\d+), Y\+(\d+)")
pp=re.compile(r"Prize:\sX=(\d+),\sY=(\d+)")
def treat(a,b,c,d,e,f):
	c+=10000000000000 #part2
	f+=10000000000000 #part2
	y=(a*f-d*c)/(a*e-d*b)
	x=(c-b*y)/a
	if x.is_integer() and y.is_integer():return x,y
	return None,None
cost=0
for block in data.split(sep):
	la,lb,lc=block.splitlines()
	a,d=bp.findall(la)[0]
	b,e=bp.findall(lb)[0]
	c,f=pp.findall(lc)[0]
	a,b,c,d,e,f=map(int,(a,b,c,d,e,f))
	x,y=treat(a,b,c,d,e,f)
	if x:cost+=3*x+y
print(int(cost))
