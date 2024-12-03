#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ~ import sympy
import sys
import re
letters=[chr(c) for c in range(97,123)]
validletters=list("abcdefghjkmnpqrstuvwxyz")
tc=[re.compile(f"{a}{b}{c}") for a,b,c in zip(letters,letters[1:],letters[2:])]
iol=re.compile("i|o|l")
dup=[re.compile(f"{c}{c}") for c in letters]
def gen(s):
	P=[list(validletters) for c in s]
	for i,c in enumerate(s):
		while P[i][0]!=c:P[i].append(P[i].pop(0))
	lp=len(P)
	while True:
		P[-1].append(P[-1].pop(0))
		lp=len(P)
		for pos in range(lp-2,-1,-1):
			if P[pos+1][0]=="a":
				P[pos].append(P[pos].pop(0))
				if pos==0 and P[0][0]=='a':
					P.insert(0,list(validletters))
					lp+=1
			else:break
		yield "".join([p[0] for p in P])
def test(p):
	if not any([t.search(p) for t in tc ]):return False
	if sum([len(d.findall(p)) for d in dup])<2:return False
	return True
for p in gen(sys.argv[1]):
	if test(p):print(p)
