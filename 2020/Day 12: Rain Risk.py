#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import sys
cp=str(sys.argv[0])
dre=re.compile(r"^Day (\d+):")
day=dre.findall(cp)[0]
fn,part=f"d{day}.txt",1
data=open(fn).read().split("\n\n")[part].splitlines()
pos=complex(0,0)
ext=re.compile(r"^(\S)(\d+)$")
def rot(cd,rl,ang):
	j=1j if rl=="R" else -1j
	for _ in range(ang//90):cd*=j
	return cd
d=complex(1,0)
for line in data:
	i,n=ext.findall(line)[0]
	n=int(n)
	match i:
		case "N":pos+=complex(0,-n)
		case "S":pos+=complex(0,n)
		case "E":pos+=complex(n,0)
		case "W":pos+=complex(-n,0)
		case "F":pos+=d*n
		case "L":d=rot(d,i,n)
		case "R":d=rot(d,i,n)
print("p1:",pos.real+pos.imag)
pos=complex(0,0)
wp=complex(10,-1)
for line in data:
	i,n=ext.findall(line)[0]
	n=int(n)
	match i:
		case "N":wp+=complex(0,-n)
		case "S":wp+=complex(0,n)
		case "E":wp+=complex(n,0)
		case "W":wp+=complex(-n,0)
		case "F":pos+=wp*n
		case "L":wp=rot(wp,i,n)
		case "R":wp=rot(wp,i,n)
print("p2:",abs(pos.real)+abs(pos.imag))
