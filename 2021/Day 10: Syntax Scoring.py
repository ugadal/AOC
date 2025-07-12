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
SC={")": 3,"]": 57,"}": 1197,">": 25137}

res=0
incomplete=[]
for s in block.splitlines():
	# ~ print(s)
	while True:
		ori=s
		s=s.replace("()","")
		s=s.replace("[]","")
		s=s.replace("<>","")
		s=s.replace("{}","")
		if s==ori:break
	if all(s.count(x)==0 for x in ")]>}"):
		incomplete.append(s)
		continue
	# ~ print(s)
	loc=min(s.index(x) for x in ")]>}" if s.count(x))
	res+=SC[s[loc]]
print("p1;",res)
SC={"(": 1,"[": 2,"{": 3,"<": 4}
res=[]
for line in incomplete:
	ttl=0
	for k in reversed(line):
		ttl*=5
		ttl+=SC[k]
	res.append(ttl)

res.sort()
p=len(res)//2
print("p2:",res[p])
	
