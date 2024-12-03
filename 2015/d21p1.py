#!/usr/bin/env python
# -*- coding: utf-8 -*-
import itertools as it
shop="""Weapons:    Cost  Damage  Armor
Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0

Armor:      Cost  Damage  Armor
Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5

Rings:      Cost  Damage  Armor
Damage+1    25     1       0
Damage+2    50     2       0
Damage+3   100     3       0
Defense+1   20     0       1
Defense+2   40     0       2
Defense+3   80     0       3"""  #rewritten to get rid of space after "Defense"
w,a,r=shop.split("\n\n")
W=[]
A=[]
R=[]
for T,S in zip((W,A,R),(w,a,r)):
	for line in S.splitlines()[1:]:
		cos,dam,arm=map(int,line.split()[1:])
		T.append((cos,dam,arm))
bf=open("d21.txt")
Bhp=int(bf.readline().strip().split(": ")[1])
Bdam=int(bf.readline().strip().split(": ")[1])
Bar=int(bf.readline().strip().split(": ")[1])
print(Bhp,Bdam,Bar)
def combo():
	Rings=[(0,0,0)]+R
	for duo in it.combinations(R,2):
		ra,rb=duo
		Rings.append(tuple([x+y for x,y in zip(ra,rb)]))
	for w in W:
		for a in [(0,0,0)]+A:
			for r in Rings:
				yield tuple([x+y+z for x,y,z in zip(w,a,r)])
rec=float("inf")
for stuff in combo():
	# ~ print(stuff)
	BhpTmp=Bhp
	php=100
	pdam=stuff[1]
	parm=stuff[2]
	BdamE=max(1,pdam-Bar)
	PdamE=max(1,Bdam-parm)
	Vic=False
	BhpTmp-=BdamE
	while True:
		if BhpTmp>0:php-=PdamE
		else:
			Vic=True
			break
		if php>0:BhpTmp-=BdamE
		else:
			Vic=False
			break
	if Vic:
		cost=stuff[0]
		if cost<rec:
			rec=cost
			print(stuff)
	
	
