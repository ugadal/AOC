#!/usr/bin/env python3
r=0
for line in open(0).read().splitlines():
	E=list(map(int,line.split()))
	r+=max(E)-min(E)
print(r)
