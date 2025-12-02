#!/usr/bin/env python3
#
fn="everybody_codes_e2025_q04_p1.txt"
V=open(fn).readlines()
a=int(V[0])
b=int(V[-1])
print("p1 :",int(2025*a/b))
fn="everybody_codes_e2025_q04_p2.txt"
V=open(fn).readlines()
a=int(V[0])
b=int(V[-1])
v=10000000000000*b/a
print("p2 :",int(v)+1)

fn="everybody_codes_e2025_q04_p3.txt"
V=list(open(fn).readlines())
v=100*int(V.pop(0))
for l in V[:-1]:
	a,b=l.split("|")
	v*=int(b)/int(a)
v/=int(V[-1])
print("p3 :",int(v))
	
