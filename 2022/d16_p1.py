#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import itertools as it
from collections import deque
from tqdm import tqdm
day=sys.argv[0].split(".")[0][1:]
print(day)
CONN={}
FLOWS={}
toopen=[]
import re
exp=f"exp{day}.txt"
real=f"d{day}.txt"
s=re.compile(r"^Valve (\S+) has flow rate=(\d+); tunnels? leads? to valves? (.*)$")
lines=open(exp).read().strip().splitlines()
# ~ lines=open(real).read().strip().splitlines()
for line in lines:
	vn,flow,conn=s.match(line).groups()
	flow=int(flow)
	if conn.find(",")>=0:conn=conn.split(", ")
	else: conn=[conn]
	CONN[vn]=list(conn)
	if flow!=0:toopen.append(vn)
	FLOWS[vn]=flow
	# ~ print (vn,flow,conn)
toopen.sort()
V=CONN.keys()
MD={}
for x in V:
	for y in V:
		MD[x,y]=float("Inf")
		MD[y,x]=float("Inf")
	MD[x,x]=0
for x in CONN.keys():
	for y in CONN[x]:
		MD[x,y]=1
		MD[y,x]=1
for k in V:   # Floyd warshall not so slow
	for x in V:
		for y in V:
			h=min(MD[x,y],MD[x,k]+MD[k,y])
			MD[x,y]=h
			MD[y,x]=h
print("AA",[MD["AA",y] for y in toopen])
print()
# ~ for x in toopen:	print(x,[MD[x,y] for y in toopen])
# ~ for k in ['UW', 'TQ', 'EG', 'KR', 'EK', 'VW', 'FX']:toopen.remove(k)
# ~ for k in ['BB', 'JJ', 'DD', 'HH', 'EE', 'CC']:toopen.remove(k)
# ~ """1595"""
rec=0
lim=30
G=[{target:[] for target in toopen} for x in range(lim+1)]
for target in toopen:
	remt=lim-1-MD["AA",target]
	G[1+MD["AA",target]][target].append(([target],remt*FLOWS[target]))

for row in range(2,lim):
	for current,V in G[row].items():
		for opened,acc in V:
			if len(opened)==len(toopen):
				if acc>rec:
					rec=acc
					print("record 1 ",opened,rec)
			for target in toopen:
				if target in opened:continue
				ttm=MD[current,target]+1
				if row+ttm>=lim:
					if acc>rec:
						rec=acc
						print(f"record 2 {rec} {opened}")
					continue
				remt=30-row-ttm
				newval=(list(opened+[target]),acc+remt*FLOWS[target])
				try:G[row+ttm][target].append(newval)
				except:
					print(row,ttm,target,newval)
					exit()

