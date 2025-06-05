#!/usr/bin/env python
# -*- coding: utf-8 -*-
part=0
import re
import sys
cp=str(sys.argv[0])
dre=re.compile(r"^Day (\d+):")
day=dre.findall(cp)[0]
fn=f"d{day}.txt"
blocks=open(fn).read().split("\n\n")
B={}
for block in blocks:
	bid=block.splitlines()[0].split()[1][:-1]
	print(bid)
	B[bid]=block.splitlines()[1:]
print(len(B))
lb=B[bid]
print(lb)
for row in lb:print(row)
print()
def flip(b):
	return[r[::-1] for r in b]
for row in flip(lb):print(row)
def transpose(b):
	# ~ R=zip(*b)
	return ["".join(row) for row in zip(*b)]
def rot(b):
	return(flip(transpose(b)))
print()	
for row in rot(lb):print(row)
def allrot(b):
	yield (b)
	yield (rot(b))
	yield (rot(rot(b)))
	yield (rot(rot(rot(b))))
	yield (flip(b))
	yield (flip(rot(b)))
	yield (flip(rot(rot(b))))
	yield (flip(rot(rot(rot(b)))))
def compare(x,y):return x[-1]==y[0]
def nmatch(x,y):
	return sum(1 if compare(x,z) else 0 for z in allrot(y))
for k,b in B.items():
	print(bid,k,nmatch(lb,b))
	print(bid,k,nmatch(rot(lb),b))
	print(bid,k,nmatch(rot(rot(lb)),b))
	print(bid,k,nmatch(rot(rot(rot(lb))),b))
# ~ for r in allrot(B["1871"]):
	# ~ for row in r:print(row)
	# ~ print()
def sidebyside(x,y):
	return	nmatch(x,y)+nmatch(rot(x),y)+nmatch(rot(rot(x)),y)+nmatch(rot(rot(rot(x))),y)
p1=1
for k,b in B.items():
	ok=0
	for t,c in B.items():
		if k==t:continue
		if sidebyside(b,c):ok+=1
	if ok==2:p1*=int(k)
print(p1)
