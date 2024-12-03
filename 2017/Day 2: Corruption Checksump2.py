#!/usr/bin/env python3
import itertools as it
r=0
for line in open(0).read().splitlines():
	E=list(map(int,line.split()))
	for a,b in it.permutations(E,2):
		if a%b==0:
			r+=a//b
			break
print(r)
