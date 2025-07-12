#!/usr/bin/env python
# -*- coding: utf-8 -*-
part=1
import re
import sys
import itertools as it
from functools import cache
import uuid
cp=str(sys.argv[0])
dre=re.compile(r"^Day (\d+):")
day=dre.findall(cp)[0]
fn=f"d{day}.txt"
# ~ block=open(fn).read().split("\n\n\n")[part]
block=open(fn).read().split("\n\n")[part]
dre=re.compile(r"\d+")
G={}
S=[]
for line in block.splitlines():
	a,b,c,d=map(int,dre.findall(line))
	if a==c:pos=[complex(a,row) for row  in range(min(b,d),max(b,d)+1)]
	elif b==d:pos=[complex(col,b) for col  in range(min(a,c),max(a,c)+1)]
	else:
		S.append(line)
		# ~ print(line,"skipped")
		continue
	# ~ print(line,pos)
	for p in pos:
		G[p]=G.get(p,0)+1
cp=[pos for pos,v in G.items() if v>1]
print("p1:",len(cp))
for line in S:
	a,b,c,d=map(int,dre.findall(line))
	v=c-a,d-b
	s=abs(max(v))
	dc,dr=tuple(x//s for x in v)
	c,r=a,b
	for x in range(s+1):
		pos=complex(c,r)
		G[pos]=G.get(pos,0)+1
		c+=dc
		r+=dr
cp=[pos for pos,v in G.items() if v>1]
print("p2:",len(cp))
