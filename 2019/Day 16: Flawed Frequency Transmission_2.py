#!/usr/bin/env python
# -*- coding: utf-8 -*-
fn,part="d16.txt",0
sep="\n\n"
import math

def gen(r):
	V=[]
	for c in [0,1,0,-1]:V.extend([c]*(r+1))
	V.append(V.pop(0))
	# ~ def ig(r):
		# ~ I=[0,1,0,-1]
		# ~ while True:
			# ~ for c in I:
				# ~ for x in range(r):
					# ~ yield c
	# ~ mg=ig(r+1)
	# ~ next(mg)
	while True:
		for v in V:yield v
		# ~ yield next(mg)
def npnl(L):
	# ~ print("".join(map(str,map(abs,L))))
	return "".join(map(str,L))
def ld(x):	return int(str(x)[-1])
inp="03036732577212944063491565474664"
inp="02935109699940807407585447034323"
inp="03081770884921959731165446850517"
inp=open(fn).readline().strip()
z=list(map(int,list(inp)))
z=z*10000
pos=int("".join(inp[:7]))
print(pos)
p=z[pos:]
print(len(p))
for t in range(100):
	np=[p.pop()]
	for i in reversed(p):
		np.append(ld(np[-1]+i))
	np.reverse()
	p=np
	print(npnl(p[:8]))
	
