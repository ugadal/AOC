#!/usr/bin/env python
# -*- coding: utf-8 -*-
part=0
import re
import sys
cp=str(sys.argv[0])
dre=re.compile(r"^Day (\d+):")
day=dre.findall(cp)[0]
fn=f"d{day}.txt"
# ~ data=open(fn).read().splitlines()[:3]
data=open(fn).read().splitlines()[4:]
G={}
for r,row in enumerate(data):
	for c,s in enumerate(row):
		if s=="#":G[r,c,0]=True
R=r+1
C=c+1
def around(t):
	a,b,c=t
	V=[]
	for r in range(a-1,a+2):
		for co in range(b-1,b+2):
			for z in range(c-1,c+2):
				V.append((r,co,z))
	V.remove((a,b,c))
	for v in V:yield v
def ext(G):
	mir=min(k[0] for k,v in G.items() if v)
	mar=max(k[0] for k,v in G.items() if v)
	mic=min(k[1] for k,v in G.items() if v)
	mac=max(k[1] for k,v in G.items() if v)
	miz=min(k[2] for k,v in G.items() if v)
	maz=max(k[2] for k,v in G.items() if v)
	return (mir,mar,mic,mac,miz,maz)
for t in range(6):
	NG={}
	mir,mar,mic,mac,miz,maz=ext(G)
	for r in range(mir-1,mar+2):
		for c in range(mic-1,mac+2):
			for z in range(miz-1,maz+2):
				pos=(r,c,z)
				busy=[G.get(p,False) for p in around(pos)].count(True)
				if G.get(pos,False) and 2<=busy<=3:NG[pos]=True
				if not G.get(pos,False) and busy==3:NG[pos]=True
	G=NG
print("p1:",len(NG))
G={}
for r,row in enumerate(data):
	for c,s in enumerate(row):
		if s=="#":G[r,c,0,0]=True
R=r+1
C=c+1
def around(t):
	a,b,c,d=t
	V=[]
	for r in range(a-1,a+2):
		for co in range(b-1,b+2):
			for z in range(c-1,c+2):
				for w in range(d-1,d+2):
					V.append((r,co,z,w))
	V.remove(t)
	for v in V:yield v
def ext(G):
	mir=min(k[0] for k,v in G.items() if v)
	mar=max(k[0] for k,v in G.items() if v)
	mic=min(k[1] for k,v in G.items() if v)
	mac=max(k[1] for k,v in G.items() if v)
	miz=min(k[2] for k,v in G.items() if v)
	maz=max(k[2] for k,v in G.items() if v)
	miw=min(k[3] for k,v in G.items() if v)
	maw=max(k[3] for k,v in G.items() if v)
	return (mir,mar,mic,mac,miz,maz,miw,maw)
for t in range(6):
	NG={}
	mir,mar,mic,mac,miz,maz,miw,maw=ext(G)
	for r in range(mir-1,mar+2):
		for c in range(mic-1,mac+2):
			for z in range(miz-1,maz+2):
				for w in range(miw-1,maw+2):
					pos=(r,c,z,w)
					busy=[G.get(p,False) for p in around(pos)].count(True)
					if G.get(pos,False) and 2<=busy<=3:NG[pos]=True
					if not G.get(pos,False) and busy==3:NG[pos]=True
	G=NG
print("p2:",len(NG))
