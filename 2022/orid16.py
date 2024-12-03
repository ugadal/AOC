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
lines=open(real).read().strip().splitlines()
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
# ~ for x in V:	print(x,[MD[x,y] for y in V])
for k in V:
	for x in V:
		for y in V:
			h=min(MD[x,y],MD[x,k]+MD[k,y])
			MD[x,y]=h
			MD[y,x]=h
# ~ for x in V:	print(x,[MD[x,y] for y in V])
# ~ print()
print("AA",[MD["AA",y] for y in toopen])
print()
for x in toopen:	print(x,[MD[x,y] for y in toopen])
rec=0
G=[{target:[] for target in toopen} for x in range(31)]
for target in toopen:
	G[1+MD["AA",target]][target].append(([target],0,FLOWS[target]))

for k in G[2].keys():
	print(k,G[2][k])
for row in range(2,30):
	for current,V in G[row].items():
		for opened,acc,cf in V:
			if len(opened)==len(toopen):
				sol=acc+cf*(30-row)
				if sol>rec:
					rec=sol
					print("record",opened,rec)
			# ~ print(current,opened,acc,cf)
			for target in toopen:
				if target in opened:continue
				ttm=MD[current,target]+1
				if row+ttm>=30:
					sol=acc+cf*(30-row)
					if sol>rec:
						rec=sol
						print(f"record {rec} {opened}")
					continue
				newval=(list(opened+[target]),acc+cf*ttm,cf+FLOWS[target])
				# ~ print(newval)
				try:G[row+ttm][target].append(newval)
				except:
					print(row,ttm,target,newval)
					exit()
	# ~ for ir,trow in enumerate(G[row:]):
		# ~ print(f"= {row+ir} ===============")
		# ~ for k in trow.keys():
			# ~ print("--------------")
			# ~ for v in trow[k]:
				# ~ print (v)
	# ~ input()


exit()







Known=set()
for p in tqdm(it.permutations(toopen)):
# ~ for p in it.permutations(toopen):
	# ~ print(p)
	acc=0
	t=MD["AA",p[0]]+1
	cf=FLOWS[p[0]]
	# ~ print(0,t,"AA",p[0],acc,cf)
	for ndx,(fr,to) in enumerate(zip(p,p[1:])):
		# ~ asas="".join(p)
		# ~ if any([asas.startswith(k) for k in Known]):continue
		ttm=MD[fr,to]+1
		# ~ print(t,t+ttm,fr,to,acc,cf)
		if t+ttm>=30:
			# ~ input(f"too late time path {p} {t} delta {ttm} prv {fr} to {to} curr index {ndx}")
			# ~ Known.add(asas[:1*(ndx+2)])
			break
		acc+=cf*ttm
		cf+=FLOWS[to]
		# ~ print(t,t+ttm,fr,to,acc,cf)
		t+=ttm
		# ~ input()
	if t<30:
		# ~ print("remn",t,t+ttm,fr,to,acc,cf)
		acc+=(30-t)*cf
	if acc>rec:
		rec=acc
		print(f"record: {rec} {p}")
		# ~ print(acc)
	# ~ input()
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
