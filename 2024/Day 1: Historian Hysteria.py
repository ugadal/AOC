#!/usr/bin/env python3
#
fn="d1.txt"
G=[]
D=[]
for line in open(fn).read().splitlines():
	g,d=map(int,line.split())
	G.append(g)
	D.append(d)
G.sort()
D.sort()
r=sum(abs(d-g) for g,d in zip(G,D))
print(r)
ttl=0
for g in G:ttl+=g*D.count(g)
print(ttl)
print (len(set(G)))
print (len(set(D)))

