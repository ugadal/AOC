#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import sys
cp=str(sys.argv[0])
dre=re.compile(r"^Day (\d+):")
day=dre.findall(cp)[0]
fn,part=f"d{day}.txt",1
data=open(fn).read().split("\n\n")[part].splitlines()
G={}
for r,row in enumerate(data):
	for c,s in enumerate(row):
		pos=complex(c,r)
		G[pos]=s
R=r+1
C=c+1
def around(pos):
	yield pos+1
	yield pos+1+1j
	yield pos+1-1j
	yield pos-1
	yield pos-1+1j
	yield pos-1-1j
	yield pos+1j
	yield pos-1j
def surround(pos):
	return [G.get(nx,".") for nx in around(pos)]
def draw():
	for row in range(R):
		print("".join(G[complex(col,row)] for col in range(C)))
	print()
# ~ draw()
while True:
	NG=dict(G)
	for r in range(R):
		for c in range(C):
			pos=complex(c,r)
			cs=G[pos]
			if cs==".":continue
			if cs=="L" and surround(pos).count("#")==0:
				NG[pos]="#"
				continue
			if cs=="#" and surround(pos).count("#")>=4:
				NG[pos]="L"
	if G==NG:
		print("p1:",list(NG.values()).count("#"))
		exit()
	G=NG
	# ~ draw()
	# ~ input()
