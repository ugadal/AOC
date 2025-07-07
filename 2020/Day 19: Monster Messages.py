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
blocks=open(fn).read().split("\n\n\n")[part]
rules,data=blocks.split("\n\n")
# ~ using grammar
R={}
nok=0
tosub={}
for line in rules.splitlines():
	if line.startswith("8:"):line="8: 42 | 42 8"
	if line.startswith("11:"):line="11: 42 31 | 42 11 31"
	rid,rule=line.split(": ")
	print (f"working on {line} : rid {rid}, rule {rule}")
	if rule.startswith('"'):
		t=set()
		t.add(rid)
		R[rule[1:-1]]=t
		continue
	for p in rule.split(" | "):
		P=p.split()
		while len(P)>2:
			x=P.pop()
			y=P.pop()
			tr=f"{uuid.uuid1()}"
			P.append(tr)
			ky=f"{y} {x}"
			if ky not in R:R[ky]=set()
			R[ky].add(tr)
		if len(P)==2:
			ky=" ".join(P)
			if ky not in R:R[ky]=set()
			R[ky].add(rid)
		if len(P)==1:
			ky=P[0]
			if ky not in R:R[ky]=set()
			R[ky].add(rid)
			print("single target",ky,R[ky])
			tosub[ky]=R[ky]
			# ~ input()

# ~ 8: 42 | 42 8
# ~ 11: 42 31 | 42 11 31


for k in sorted(R.keys()):
	print(k,R[k])
for line in data.splitlines():
	G={}
	ll=len(line)
	for i,c in enumerate(line):
		G[i,i]=set()|R[c]
		if any(k in G[i,i] for k in tosub.keys()):
			ori=G[i,i]
			while True:
				new=set(ori)
				for k in ori:
					if k in R:
						new|=R[k]
				if new==ori:break
				ori=new
			G[i,i]=set(ori)
	for d in range(1,ll):
		for i in range(ll-d):
			j=i+d
			G[i,j]=set()
			for k in range(i,j):
				for a,b in it.product(G[i,k],G[k+1,j]):
					ky=f"{a} {b}"
					if ky in R:
						G[i,j]|=R[ky]
				new=set(G[i,j])
				for k in G[i,j]:
					if k in tosub:
						new|=R[k]
				G[i,j]=new
	# ~ print (G[0,ll-1])
	if '0' in G[0,ll-1]: 
		print(line,"ok")
		nok+=1
	else:print(line,"wrong")
print(nok)
