#!/usr/bin/env python
# -*- coding: utf-8 -*-
fn,part="d3.txt",1
data=open(fn).read().split("\n\n")[part].splitlines()
G={}
for r,row in enumerate(data):
	for c,s in enumerate(row):
		pos=complex(c,r)
		G[pos]=s
R=r
C=c+1
sp=complex(0,0)
print(R,C)
trees=0
for r in range(R):
	print(sp,G[sp])
	sp+=complex(3,1)
	sp=complex(sp.real%C,sp.imag)
	if G[sp]=="#":trees+=1
print(trees)
# ~ import re
# ~ extract=re.compile(r"(\d+)-(\d+) (\S): (\S+)")
# ~ okp1=0
# ~ okp2=0
# ~ for line in data:
	# ~ mi,ma,s,pw=extract.findall(line)[0]
	# ~ mi=int(mi)
	# ~ ma=int(ma)
	# ~ c=pw.count(s)
	# ~ if c>=mi and c<=ma:okp1+=1
	# ~ if pw[mi-1]==s and pw[ma-1]!=s:okp2+=1
	# ~ elif pw[mi-1]!=s and pw[ma-1]==s:okp2+=1
# ~ print(okp1)
# ~ print(okp2)
