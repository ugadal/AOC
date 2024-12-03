#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from collections import deque
day=sys.argv[0].split(".")[0][1:]
print(day)

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
	if flow!=0:toopen.add(vn)
	FLOWS[vn]=flow
	print (vn,flow,conn)




exit()
CONN={}
toopen=set()
FLOWS={}
for line in lines:
	vn,flow,conn=s.match(line).groups()
	flow=int(flow)
	if conn.find(",")>=0:conn=conn.split(", ")
	else: conn=[conn]
	CONN[vn]=list(conn)
	if flow!=0:toopen.add(vn)
	FLOWS[vn]=flow
	print (vn,flow,conn)
# ~ OPENED=tuple(OPENED)
Q=deque()
NQ=deque()
Q.append((0,None,"AA",toopen,0,0))
nv=len(CONN)
rec=0
mt=30
for tt in range(mt+1):
	print(tt,len(Q))
	while Q:
		# ~ print (len(Q),Q[-1])
		z=Q.popleft()
		t,prev,vn,toopen,cf,acc=z
		if t==mt:
			if acc>rec:
				rec=acc
				print("*rec",rec)
				continue
		if len(toopen)==0:
			# ~ print(z)
			facc=acc+(mt-t)*cf
			if facc>rec:
				rec=facc
				print("*rec",rec)
			continue
		#open
		if vn in toopen:
			nf=cf+FLOWS[vn]
			NQ.append((t+1,None,vn,toopen-set(vn),nf,acc+cf))
		# ~ move
		for dst in CONN[vn]:
			if dst==prev:continue
			NQ.append((t+1,vn,dst,toopen,cf,acc+cf))
	# ~ print (len(Q),len(NQ),len(set(NQ)))
	# ~ Q=deque(set(NQ))
	Q=NQ
	# ~ for q in Q:print(q)
	# ~ Q=NQ
	NQ=deque()
	# ~ input(t)
	
