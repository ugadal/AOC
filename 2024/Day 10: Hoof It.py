#!/usr/bin/env python3
#
sep="\n\n"
fn,part="d10.txt",1
data=open(fn).read().split(sep)[part].splitlines()
G={}
def around(p):
	for d in [-1j,1,1j,-1]:	yield p+d
for row, line in enumerate(data):
	for col,v in enumerate(line):
		G[col+row*1j]=int(v)
zeroes=[k for k,v in G.items() if v==0]
def reachable(cp,cv=0):
	if cv==9:
		yield cp
	else:
		for t in [p for p in around(cp) if G.get(p,-1)==cv+1]:
			for v in reachable(t,cv+1):yield v
def countreached(sp):
	R=list(reachable(sp))
	return len(set(R))
r=sum(countreached(zero) for zero in zeroes)
print(r)
r=sum(len(list(reachable(zero))) for zero in zeroes)
print(r)
