#!/usr/bin/env python
# -*- coding: utf-8 -*-
fn,part="d18.txt",4
import heapq as hq
data=open(fn).read().split("\n\n")[part]
print(data)
keys=list(map(chr,range(97,123)))
locks=list(map(chr,range(65,91)))
M={}
rk=[]
for r,row in enumerate(data.splitlines()):
	for c,s in enumerate(row):
		pos=complex(c,r)
		M[pos]=s
		if s=="@":sp=pos
		if s in keys:rk.append(s)
print(rk)
NR=r+1
NC=c+1
print(NR,NC,sp)

def around(p):
	yield p-1
	yield p+1
	yield p+1j
	yield p-1j
draw()
todo=[]
hq.heapify(todo)
hq.heappush(todo,(0,0,"",sp))
# ~ todo=[(sp,"",0)]
visited={}
tested=0
record=float("Inf")
while todo:
	steps,_,ks,pos=hq.heappop(todo)
	# ~ print(f"ks : {ks}  steps : {steps} pos : {pos}")
	if tested%100000==0:print("\r",len(todo),ks,end="                 ")
	if steps>record:continue
	if all(s in ks for s in rk):
		if steps<record:
			record=steps
			print("record",pos,steps-1,ks)
			continue
	if visited.get((pos,ks),float("Inf"))<steps:
		continue
	cs=M.get(pos,"#")
	if cs in keys and cs not in ks:
		# ~ print("adding key")
		ks+=cs
		ks=list(ks)
		ks.sort()
		ks="".join(ks)
	if cs in locks and cs.lower() not in ks:
		# ~ print("skipping 1")
		continue
	for np in around(pos):
		if M.get(np,"#")=="#":
			# ~ print("skipping2",np)
			continue
		tested+=1
		hq.heappush(todo,(steps+1,tested,ks,np))
		# ~ print("todo",todo)
	visited[pos,ks]=steps
	# ~ todo=set(newtodo)
	# ~ print(len(newtodo),len(todo),pos,ks,steps)
	# ~ if not todo:break
print (visited)
