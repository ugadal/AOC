#!/usr/bin/env python3
#
# ~ from malib import *
fn="everybody_codes_e2025_q06_p1.txt"
d=open(fn).readline()
res=0
for pos in (p for p,c in enumerate(d) if c=="A"):
	res+=d[pos+1:].count("a")
print(res)
fn="everybody_codes_e2025_q06_p2.txt"
d=open(fn).readline()
res=0
for pos,c in ((p,c) for p,c in enumerate(d) if c.isupper()):
	res+=d[pos+1:].count(c.lower())
print(res)
fn="everybody_codes_e2025_q06_p3.txt"
d=open(fn).readline()
def ana(l):
	res=0
	rl=len(l)+1
	for pos,c in enumerate(l):
		if c.isupper():continue
		res+=l[max(0,pos-1000):min(pos+1001,rl)].count(c.upper())
	return res
v=ana(d)
ww=ana(d+d)
print(v+999*(ww-v))
# ~ 1665131219
