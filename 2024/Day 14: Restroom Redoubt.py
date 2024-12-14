#!/usr/bin/env python3
#
sep="\n\n"
fn,part="d14.txt",1
import re
de=re.compile(r"(-?\d+)")
class robot():
	def __init__(self,c,r,dc,dr):
		self.p=c+r*1j
		self.d=dc+dr*1j
data=open(fn).read().splitlines()
R=[]
for line in data:
	V=list(map(int,de.findall(line)))
	R.append(robot(*V))
NC=101
NR=103
t=0
while True:
	t+=1
	print(t)
	for r in R:	
		r.p+=r.d
		r.p=r.p.real%NC + r.p.imag%NR *1j
	P=set(r.p for r in R)
	if len(P)==len(R):
		for r in range(NR):
			rt=[]
			for c in range(NC):
				if c+r*1j in P:rt.append("X")
				else:rt.append(".")
			print ("".join(rt))
		input()
#part 1
sf=1
sf*=sum(1 if 0<=r.p.imag<NR//2 and 0<=r.p.real<NC//2 else 0 for r in R)
sf*=sum(1 if 0<=r.p.imag<NR//2 and NC//2<r.p.real<NC else 0 for r in R)
sf*=sum(1 if NR//2<r.p.imag<NR and 0<=r.p.real<NC//2 else 0 for r in R)
sf*=sum(1 if NR//2<r.p.imag<NR and NC//2<r.p.real<NC else 0 for r in R)
print(sf)
