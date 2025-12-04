#!/usr/bin/env python3
#
fn,part="d4.txt",1
sep="\n\n"
data=open(fn).read().split(sep)[part]
def readG(data):
	G={}
	for row,line in enumerate(data.splitlines()):
		for col,s in enumerate(line):
			pos=complex(col,row)
			G[pos]=s
	return G,row+1,col+1
G,R,C=readG(data)
def pmap(G):
	for row in range(R):
		print("".join([G[complex(col,row)] for col in range(C)]))
def around(pos):
	for dc in (-1,0,1):
		for dr in (-1j,0,1j):
			if dc+dr:yield pos+dc+dr
res=0
for row in range(R):
	for col in range(C):
		pos=complex(col,row)
		if G[pos]==".":continue
		a=[G.get(p,".") for p in around(pos)]
		if a.count("@")<4:res+=1
print("p1 :",res)
cyc=0
total=0
while True:
	pmap(G)
	cyc+=1
	torem=[]
	for row in range(R):
		for col in range(C):
			pos=complex(col,row)
			if G[pos]==".":continue
			a=[G.get(p,".") for p in around(pos)]
			if a.count("@")<4:torem.append(pos)
	print(f"{cyc} : {len(torem)}")
	for pos in torem:G[pos]="."
	if not torem:break
	total+=len(torem)
print("p2 :",total)
