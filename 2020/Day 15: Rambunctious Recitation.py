#!/usr/bin/env python
# -*- coding: utf-8 -*-
part=1
import re
import sys
cp=str(sys.argv[0])
dre=re.compile(r"^Day (\d+):")
day=dre.findall(cp)[0]
fn=f"d{day}.txt"
data=list(map(int,open(fn).read().splitlines()[part].split(",")))
print(data)
while len(data)!=2020:
	lw=data[-1]
	if data.count(lw)==1:
		data.append(0)
		continue
	# ~ print(data)
	# ~ input()
	data.reverse()
	pos=data.index(lw,1)
	data.reverse()
	data.append(pos)
print("p1;",data[-1:])
data=list(map(int,open(fn).read().splitlines()[part].split(",")))
R={}
# ~ 0,3,6
# ~ 0 3 6 0 3 3 1 0
for p,v in enumerate(data):
	R[v]=(-1,p)
	lw=v
	lp=p
print(R)
while p<30000000:
	p+=1
	res=lw
	if lw not in R:
		R[lw]=(-1,p-1)
	a,b=R[lw]
	if a==-1: #first sight
		c,d=R[0]
		R[0]=(d,p)
		lw=0
		# ~ print(R)
		# ~ input()
		continue
	lw=b-a
	if lw not in R:
		R[lw]=(-1,-1)
	c,d=R[lw]
	R[lw]=(d,p)
print(res)
	# ~ print(R)
	# ~ input()
	# ~ a,b=R[lw]
	# ~ lw=b-a
	# ~ if lw in R:
	# ~ if lw=p-1
	# ~ R[lw]=(b,p)
		# ~ print("in:",lw,p,R)
		# ~ input()
		# ~ continue
	# ~ lw=0
	# ~ R[0]=(R[0][-1],p)
	# ~ print("out:",lw,p,R)
	# ~ input()
