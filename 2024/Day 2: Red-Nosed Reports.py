#!/usr/bin/env python3
#
fn,part="d2.txt",1
data=open(fn).read().split("\n\n")[part].splitlines()
safe=0
def lat(L):
	yield L
	for p in range(len(L)):
		NL=list(L)
		NL.pop(p)
		yield NL
def valid(V):
	D=[b-a for a,b in zip(V,V[1:])]
	if any (da*db<=0 for da,db in zip(D,D[1:])):return False
	if all(1<=abs(d)<=3 for d in D):return True
	return False
for line in data:
	V=list(map(int,line.split()))
	D=[b-a for a,b in zip(V,V[1:])]
	if any (da*db<=0 for da,db in zip(D,D[1:])):continue
	if all(1<=abs(d)<=3 for d in D):safe+=1
print("part 1 :",safe)
safe=0
for line in data:
	V=list(map(int,line.split()))
	for L in lat(V):
		if valid(L):
			safe+=1
			break
print("part 2 :",safe)
