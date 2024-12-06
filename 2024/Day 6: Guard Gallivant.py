#!/usr/bin/env python3
#
sep="\n\n"
fn,part="d6.txt",1
data=open(fn).read().split("\n\n")[part].splitlines()
G={}
for r,line in enumerate(data):
	for c,s in enumerate(line):
		if s=="^":
			spos=c+r*1j
			s="."
		G[c+r*1j]=s
NR=r+1
NC=c+1
print(NR,NC,spos)
def walk():
	V=[spos]
	pos=spos
	d=-1j
	while True:
		npos=pos+d
		ns=G.get(npos,"-")
		match ns:
			case "#":
				d*=1j
				continue
			case "-":
				return V
			case ".":
				V.append(npos)
				pos=npos
res=walk()
s=set(res)
print(len(s))
