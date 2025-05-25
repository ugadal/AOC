#!/usr/bin/env python
# -*- coding: utf-8 -*-
part=0
import re
import sys
cp=str(sys.argv[0])
dre=re.compile(r"^Day (\d+):")
day=dre.findall(cp)[0]
fn=f"d{day}.txt"
"""
mask = 1001X0X00110011X01X1000110100011000X
mem[5228] = 409649
mem[64037] = 474625
"""
R={}
memex=re.compile(r"mem\[(\d+)\] = (\d+)")
data=open(fn).read().split("\n\n")[part].splitlines()
for line in data:
	if line.startswith("mask"):
		m=line.split()[2]
		# ~ force one
		mor=m.replace("X","0")
		mor=int(mor,2)
		# ~ force zeroes
		mand=m.replace("X","1")
		mand=int(mand,2)
		continue
	add,val=map(int,memex.findall(line)[0])
	val=val|mor
	val=val&mand
	R[add]=val
print("p1:",sum(R.values()))
add=format(42,"b").zfill(36)
m="000000000000000000000000000000X1001X"
nm=""
for x,y in zip(m,add):
	match x:
		case "0":nm+=y
		case "1":nm+=x
		case "X":nm+=x
print(nm)
P=[""]
for c in nm:
	NP=[]
	match c:
		case "0":NP=[p+"0" for p in P]
		case "1":NP=[p+"1" for p in P]
		case "X":
			NP=[p+"0" for p in P]
			NP.extend([p+"1" for p in P])
	P=NP
for p in P:print(int(p,2))
