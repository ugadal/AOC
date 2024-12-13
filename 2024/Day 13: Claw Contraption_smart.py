#!/usr/bin/env python3
#
sep="\n\n"
fn,part="d13.txt",1
data=open(fn).read()
import re 
dig=re.compile(r"(\d+)")
def treat(a,b,c,d,e,f):
	c+=10000000000000 #part2
	f+=10000000000000 #part2
	y=(a*f-d*c)/(a*e-d*b)
	x=(c-b*y)/a
	if x.is_integer() and y.is_integer():return x,y
	return None,None
cost=0
for block in data.split(sep):
	a,d,b,e,c,f=map(int,dig.findall(block))
	x,y=treat(a,b,c,d,e,f)
	if x:cost+=3*x+y
print(int(cost))
