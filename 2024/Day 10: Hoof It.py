#!/usr/bin/env python3
#
sep="\n\n"
fn,part="d10.txt",1
data=open(fn).read().split(sep)[part].splitlines()
# ~ the sum of the scores of all trailheads is 36
G={}
D=[-1j,1,1j,-1]
for row, line in enumerate(data):
	for col,v in enumerate(line):
		G[col+row*1j]=int(v)
zeroes=[k for k,v in G.items() if v==0]
def reachable(cp,cv=0):
	# ~ print(" "*cv,f"entered pos {cp} v {cv}")
	if cv==9:
		yield cp
	else:
		for t in [cp+d for d in D if G.get(cp+d,-1)==cv+1]:
			for v in reachable(t,cv+1):yield v
def countreached(sp):
	R=list(reachable(sp))
	print(R)
	return len(set(R))
r=sum(countreached(zero) for zero in zeroes)
print(r)
# ~ print(zeroes[0])
# ~ for v in reachable(zeroes[0]):print(v)
# ~ R=list(reachable(zeroes[0]))
# ~ print(R)
# ~ print(len(set(R)))
