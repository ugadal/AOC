#!/usr/bin/env python3
#
sep="\n\n"
fn,part="d6.txt",1
from progress.bar import Bar
data=open(fn).read().split(sep)[part].splitlines()
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
def loops(rock):
	d=-1j
	V=set()
	V.add((spos,d))
	pos=spos
	NG=dict(G)
	NG[rock]="#"
	while True:
		npos=pos+d
		ns=NG.get(npos,"-")
		match ns:
			case "#":
				d*=1j
				continue
			case "-":return False,V
			case ".":
				if (npos,d) in V:return True,V
				V.add((npos,d))
				pos=npos
res2=0
_,path=loops(-NC-NR*1j)
path=set([rock for rock,d in path])
bar=Bar("testing",max=len(path))
for rock in path:
	bar.next()
	if rock==spos:continue
	if loops(rock)[0]:res2+=1
bar.finish()
print(res2)
