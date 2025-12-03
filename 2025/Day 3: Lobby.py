#!/usr/bin/env python3
#
fn,part="d3.txt",1
sep="\n\n"
data=open(fn).read().split(sep)[part]
def ana(l):
	V=list(l)
	V=list(map(int,V))
	mx=0
	for pos,v in enumerate(V[:-1]):
		for w in V[pos+1:]:
			mx=max(mx,10*v+w)
	return mx
res=0
for bank in data.splitlines():
	res+=ana(bank)
print("p1 :",res)

def ana(V):
	sub=list(V)
	res=[]
	keep=11
	while keep:
		mx=max(sub[:-keep])
		pos=next(p for p,v in enumerate(sub) if v==mx)
		res.append(mx)
		sub=sub[pos+1:]
		keep-=1
	p=0
	res.append(max(sub))
	for v in res:p=10*p+v
	return p
res=0
for bank in data.splitlines():
	V=list(bank)
	V=list(map(int,V))
	v=ana(V)
	res+=v
print("p2 :",res)
