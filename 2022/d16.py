#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import itertools as it
from collections import deque
# ~ from tqdm import tqdm
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
allin=2**(len(toopen))-1
stb={}
bts={}
for i,k in enumerate(toopen):
	stb[k]=1<<i
	bts[1<<i]=k
ndx={valve:1<<toopen.index(valve) for valve in toopen}
cache = {}
def dfs(time, valve, bitmask):
    if (time, valve, bitmask) in cache:return cache[(time, valve, bitmask)]
    maxval = 0
    for neighbor in toopen:
        bit = ndx[neighbor]
        if bitmask & bit: continue
        remtime = time - MD[valve,neighbor] - 1
        if remtime <= 0:continue
        maxval = max(maxval, dfs(remtime, neighbor, bitmask | bit) + FLOWS[neighbor] * remtime)
    cache[(time, valve, bitmask)] = maxval
    return maxval
print(dfs(30, "AA", 0))
def TA(A,B):
	# ~ print(A,B)
	if (A,B) in cache:return cache[A,B]
	if (B,A) in cache:return cache[B,A]
	ta,va,bma=A
	tb,vb,bmb=B
	remn=[bts[2**i] for i, v in enumerate(bin(allin^bma^bmb)[:1:-1]) if int(v)]
	# ~ print(remn)
	mv=0
	for na in remn:
		remta=ta-MD[va,na]-1
		if remta>0:	mv=max(mv,remta*FLOWS[na]+TA((remta,na,bma|ndx[na]),B))
		remtb=tb-MD[vb,na]-1
		if remtb>0:	mv=max(mv,remtb*FLOWS[na]+TA(A,(remtb,na,bmb|ndx[na])))
	cache[A,B]=mv
	return mv
print(TA((26,"AA",0),(26,"AA",0)))
# ~ print(len(cache))
exit()
while Q:
	Aa,Ab=Q.pop(0)
	Visited=Aa[0]|Ab[0]
	REM=[targ for targ in toopen if ndx[targ]&Visited==0]
	# ~ print(Aa,Ab,REM)
	# ~ exit()
	if len(REM)==0:
		sol=Aa[3]+Ab[3]
		check(sol)
		continue
	if len(REM)==1:
		targ=REM[0]
		tndx=ndx[targ]
		ttm=MD[Aa[1],targ]+1
		if Aa[2]+ttm>=lim:check(Aa[3]+Ab[3])
		else:
			remt=lim-Aa[2]-ttm
			newa=(Aa[0]|ndx[targ],targ,Aa[2]+ttm,Aa[3]+FLOWS[targ]*remt)
			Q.append((newa,Ab))
		
		ttm=MD[Ab[1],targ]+1
		if Ab[2]+ttm>=lim:check(Aa[3]+Ab[3])
		else:
			remt=lim-Ab[2]-ttm
			newb=(Ab[0]|ndx[targ],targ,Ab[2]+ttm,Ab[3]+FLOWS[targ]*remt)
			Q.append((Aa,newb))
		continue
	for targa,targb in it.combinations(REM,2):
		for _ in range(2):
			ttma=MD[Aa[1],targa]+1
			ttmb=MD[Ab[1],targb]+1
			if Aa[2]+ttma<lim and Ab[2]+ttmb<lim:
				remta=lim-Aa[2]-ttma
				remtb=lim-Ab[2]-ttmb
				newa=(Aa[0]|ndx[targa],targa,Aa[2]+ttma,Aa[3]+FLOWS[targa]*remta)
				newb=(Ab[0]|ndx[targb],targb,Ab[2]+ttmb,Ab[3]+FLOWS[targb]*remtb)
				Q.append((newa,newb))
			else:check(Aa[3]+Ab[3])
			# ~ if Aa[2]+ttma<lim and Ab[2]+ttmb>=lim:
				# ~ remta=lim-Aa[2]-ttma
				# ~ newa=(Aa[0]|ndx[targa],targa,Aa[2]+ttma,Aa[3]+FLOWS[targa]*remta)
				# ~ Q.append((newa,Ab))
			# ~ if Aa[2]+ttma>=lim and Ab[2]+ttmb<lim:
				# ~ remtb=lim-Ab[2]-ttmb
				# ~ newb=(Ab[0]|ndx[targb],targb,Ab[2]+ttmb,Ab[3]+FLOWS[targb]*remtb)
				# ~ Q.append((Aa,newb))
			targa,targb=targb,targa
print(rec)
exit()
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

