#!/usr/bin/env python
# -*- coding: utf-8 -*-

L=list(range(256))
pos=skip=0

# ~ p1

for v in map(int,open("d10.txt").readline().strip().split(",")):
	for d in range(v//2):
		L[(pos+d)%256],L[(pos+v-1-d)%256]=L[(pos+v-1-d)%256],L[(pos+d)%256]
	pos+=v+skip
	skip+=1
print(L[0]*L[1])

# ~ p2

LV=list(map(ord,( c for c in open("d10.txt").readline().strip())))
LV.extend([17, 31, 73, 47, 23])
L=list(range(256))
pos=skip=0
for _ in range(64):
	for v in LV:
		for d in range(v//2):
			L[(pos+d)%256],L[(pos+v-1-d)%256]=L[(pos+v-1-d)%256],L[(pos+d)%256]
		pos+=v+skip
		skip+=1

res=""

for a in range(16):
	hsx=L[16*a:16*a+16]
	v=hsx.pop()
	while hsx:v=v^hsx.pop()
	res+=hex(v)[-2:]

print(res)
