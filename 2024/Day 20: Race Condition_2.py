#!/usr/bin/env python3
#
# ~ from functools import cache
from collections import deque
sep="\n\n"
fn,part="d20.txt",1
grid=open(fn).read().split(sep)[part].splitlines()
G={}
for r,row in enumerate(grid):
	for c,s in enumerate(row):
		G[complex(c,r)]=s
NR=r+1
NC=c+1
def draw():
	for row in range(NR):
		print( "".join( [ G.get(col+row*1j,"#") for col in range(NC) ] ) )
def around(p):
	yield p+1
	yield p+1j
	yield p-1
	yield p-1j
def aroundc(p):
	yield p+2
	yield p+2*1j
	yield p-2
	yield p-2*1j
def aroundr(p):
	for d in range(2,21):
		for dc in range(d+1):
			dr=d-dr
			yield p+complex(dc,dr),d
			yield p+complex(dc,-dr),d
			yield p+complex(-dc,dr),d
			yield p+complex(-dc,-dr),d
# ~ draw()
sp=next(p for p,v in G.items() if v=="S")
ep=next(p for p,v in G.items() if v=="E")
print(sp,ep)
G[sp]="."
G[ep]="."
rocks=[p for p,v in G.items() if v=="#"]
def walk(sp,std,cc,rec=float("inf")):
	V=set()
	todo=deque([(sp,0,cc)])
	while todo:
		cp,std,cc=todo.popleft()
		if (cp,cc) in V:continue
		if cp==ep:
			yield std
			continue
		for np in around(cp):
			if G.get(np,"#")=="#":continue
			todo.append((np,std+1,cc))
		if not cc:
			for np,d in aroundr(cp):
				if G.get(np,"#")==".":
					todo.append((np,std+d,(cp,np)))
		V.add((cp,cc))
	yield rec+1
		
nocheat=next(walk(sp,0,True))
print("using nocheat",nocheat)
count=0
for rock in rocks:
	G[rock]="."
	d=next(walk(sp,0,nocheat-100))
	if nocheat-d>=100:
		count+=1
		print("okpath gain:",count,nocheat-d)
	G[rock]="#"
print(count)
