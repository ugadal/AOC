#!/usr/bin/env python
# -*- coding: utf-8 -*-
part=1
import re
import sys
import itertools as it
from functools import cache

cp=str(sys.argv[0])
dre=re.compile(r"^Day (\d+):")
day=dre.findall(cp)[0]
fn=f"d{day}.txt"
blocks=open(fn).read().split("\n\n\n")[part]
rules,data=blocks.split("\n\n")
print(rules)
print(data)
R={}
for line in rules.splitlines():
	rid,rule=line.split(": ")
	R[rid]=rule
@cache
def decompose(x):
	print('entering on',x)
	if x.startswith('"'):
		print("returning simple from",x,[x[1:-1]])
		return [x[1:-1]]
	if x.count(" | "):
		P=[]
		for p in map(decompose,x.split(" | ")):
			P.extend(p)
		print(f"returning from or {x} {P}")
		return P
	if x.count(" "):
		P=map(decompose,x.split(" "))
		P=list(P)
		# ~ print(P)
		P=it.product(*P)
		# ~ P=list(P)
		# ~ print(P)
		P=["".join(p) for p in P]
		# ~ print(P)
		print(f"returning from and {x} : {P}")
		return P
	# ~ if R[x].startswith('"'):return [R[x][1:-1]]
	return decompose(R[x])
# ~ 3: 4 5 | 5 4
# ~ 4: "a"
# ~ 5: "b"
# ~ print(decompose("4 5 4"))
# ~ print(decompose("4 | 5"))
ok=decompose("0")
nok=0
for line in data.splitlines():
	if line in ok:
		print(line,"ok")
		nok+=1
	else:print(line,"wrong")
print(f"p1: {nok}")
