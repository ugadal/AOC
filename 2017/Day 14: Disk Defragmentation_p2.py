#!/usr/bin/env python
# -*- coding: utf-8 -*-

ex="flqrgnkx"
ex="stpzcrnm"
def kh(s):
	LV=list(map(ord,( c for c in s)))
	LV.extend([17, 31, 73, 47, 23])
	L=list(range(256))
	pos=skip=0
	for _ in range(64):
		for v in LV:
			for d in range(v//2):
				L[(pos+d)%256],L[(pos+v-1-d)%256]=L[(pos+v-1-d)%256],L[(pos+d)%256]
			pos+=v+skip
			skip+=1
	V=0
	for a in range(16):
		hsx=L[16*a:16*a+16]
		v=hsx.pop()
		while hsx:v=v^hsx.pop()
		V=V*256+v
	return bin(V)
z=0
G=[]
for r in range(128):
	row=kh(ex+'-'+str(r))[2:]
	while len(row)<128:row="0"+row
	G.append(row)
print([len(row) for row in G])
G=[['#' if c=="1" else "." for c in row] for row in G]
isle=0
def anydot(G):
	for ir,row in enumerate(G):
		if row.count("#"):return (True,(ir,row.index("#")))
	return (False,(None,None))
ad,(r,c)=anydot(G)	
while ad:
	isle+=1
	todo=[(r,c)]
	while todo:
		nxtodo=[]
		for tr,tc in todo:
			G[tr][tc]=isle
			for dr,dc in ((-1,0),(1,0),(0,-1),(0,1)):
				nr=tr+dr
				nc=tc+dc
				if not 0<=nr<128:continue
				if not 0<=nc<128:continue
				if G[nr][nc]=="#":nxtodo.append((nr,nc))
		todo=list(nxtodo)
	ad,(r,c)=anydot(G)	
print(isle)
