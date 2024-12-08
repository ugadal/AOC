#!/usr/bin/env python3
#
sep="\n\n"
fn,part="d8.txt",3
data=open(fn).read().split(sep)[part].splitlines()
A={}
AN=set()
for r,line in enumerate(data):
	for c,s in enumerate(line):
		if s!=".":A[r,c]=s
NR,NC=r+1,c+1
AT=set(A.values())
print(AT)
AN=set()
for at in AT:
	for source,stype in A.items():
		if stype!=at:continue
		for target,ttype in A.items():
			if source==target:continue
			if ttype!=at:continue
			sr,sc=source
			tr,tc=target
			dr=tr-sr
			dc=tc-sc
			AN.add((2*sr-tr,2*sc-tc))
			AN.add((2*tr-sr,2*tc-sc))
IM=[]
for r,c in AN:
	if 0<=r<NR and 0<=c<NC:IM.append((r,c))
print(len(IM),IM)
			
