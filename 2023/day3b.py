#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ~ 467..114..
# ~ ...*......
# ~ ..35..633.
# ~ ......#...
# ~ 617*......
# ~ .....+.58.
# ~ ..592.....
# ~ ......755.
# ~ ...$.*....
# ~ .664.598..
G=open(0).read().splitlines()
cs=set()
R=len(G)
C=len(G[0])
for r,row in enumerate(G):
	for c,ch in enumerate(row):
		if ch.isdigit() or ch==".":continue
		for cr in [r-1,r,r+1]:
			for cc in [c-1,c,c+1]:
				if cr<0 or cr>=R or cc<0 or cc>=C or not G[cr][cc].isdigit():continue
				while cc>0 and G[cr][cc-1].isdigit():cc-=1
				cs.add((cr,cc))
V=[]
for r,c in cs:
	s=""
	while c<C and G[r][c].isdigit():
		s+=G[r][c]
		c+=1
	V.append(int(s))
print(sum(V))
V=0
for r,row in enumerate(G):
	for c,ch in enumerate(row):
		if ch!="*":continue
		cs=set()
		for cr in [r-1,r,r+1]:
			for cc in [c-1,c,c+1]:
				if cr<0 or cr>=R or cc<0 or cc>=C or not G[cr][cc].isdigit():continue
				while cc>0 and G[cr][cc-1].isdigit():cc-=1
				cs.add((cr,cc))
		if(len(cs))!=2:continue
		ns=[]
		for cr,cc in cs:
			s=""
			while cc<C and G[cr][cc].isdigit():
				s+=G[cr][cc]
				cc+=1
			ns.append(int(s))
		V+=ns[0]*ns[1]
print (V)
	
