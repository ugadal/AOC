#!/usr/bin/env python
# -*- coding: utf-8 -*-
fn,part="d18.txt",4
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
todo=[(sp,"",0)]
visited={}
while True:
	newtodo=[]
	for pos,ks,steps in todo:
		# ~ print(pos,ks,steps)
		if all(s in ks for s in rk):
			print(pos,steps-1,ks)
			exit()
		if visited.get((pos,ks),float("Inf"))<steps:continue
		# ~ input()
		cs=M.get(pos,"#")
		if cs in keys and cs not in ks:
			ks+=cs
			ks=list(ks)
			ks.sort()
			ks="".join(ks)
		if cs in locks and cs.lower() not in ks:continue
		for np in around(pos):
			if M.get(np,"#")=="#":continue
			newtodo.append((np,ks,steps+1))
		visited[pos,ks]=steps
	todo=set(newtodo)
	print(len(newtodo),len(todo),pos,ks,steps)
	if not todo:break
print (visited)
