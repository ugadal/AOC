#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import sys
cp=str(sys.argv[0])
dre=re.compile(r"^Day (\d+):")
day=dre.findall(cp)[0]
fn,part=f"d{day}.txt",1
data=list(map(int,open(fn).read().split("\n\n")[part].splitlines()))
data.sort()
data.insert(0,0)
data.append(data[-1]+3)
delta=[b-a for a,b in zip(data,data[1:])]
print("p1:",delta.count(1)*delta.count(3))
print(data)
def count(L):
	match len(L):
		case 1:return 1
		case 2:return 1
		case 3:return 2 
		case 4:return 4 #keep 2, or remove 1 twice, or remove both
		case 5:return 7
R=1
pos=0
bg=0
while pos<len(data):
	if data[pos]==data[pos+1]-3:
		print ("break at pos:",pos)
		part=data[bg:pos+1]
		print ("find combos in ",part)
		n=pos-bg-1
		print("combo is",count(part))
		R*=count(part)
		print(R)
		bg=pos+1
		# ~ input()
	pos+=1
