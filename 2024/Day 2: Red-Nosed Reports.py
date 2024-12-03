#!/usr/bin/env python3
#
fn,part="d2.txt",1
data=open(fn).read().split("\n\n")[part].splitlines()
safe=0
for line in data:
	V=list(map(int,line.split()))
	print(V)
	D=[b-a for a,b in zip(V,V[1:])]
	print(D)
	if any (da*db<=0 for da,db in zip(D,D[1:])):continue
	if all(1<=abs(d)<=3 for d in D):safe+=1
print(safe)
