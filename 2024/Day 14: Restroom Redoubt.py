#!/usr/bin/env python3
#
sep="\n\n"
fn,part="d14.txt",1
data=open(fn).read()
import re
de=re.compile(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)")
class robot():
	def __init__(self,c,r,dc,dr):
		self.p=c+r*1j
		self.d=dc+dr*1j
map(int,(de.findall("p=0,-4 v=3,-3")))
data=open(fn).read().splitlines()
R=[]
for line in data:
	V=list(map(int,de.findall(line)[0]))
	R.append(robot(*V))
NC=101
NR=103
for r in R:	
	r.p+=100*r.d
	r.p=r.p.real%NC + r.p.imag%NR *1j
P=[r.p for r in R]
# ~ for r in range(NR):
	# ~ rt=[]
	# ~ for c in range(NC):
		# ~ c=P.count(c+r*1j)
		# ~ if c:rt.append(str(c))
		# ~ else:rt.append(".")
	# ~ print ("".join(rt))
sf=1
sf*=sum(1 if 0<=r.p.imag<NR//2 and 0<=r.p.real<NC//2 else 0 for r in R)
sf*=sum(1 if 0<=r.p.imag<NR//2 and NC//2<r.p.real<NC else 0 for r in R)
sf*=sum(1 if NR//2<r.p.imag<NR and 0<=r.p.real<NC//2 else 0 for r in R)
sf*=sum(1 if NR//2<r.p.imag<NR and NC//2<r.p.real<NC else 0 for r in R)
print(sf)
