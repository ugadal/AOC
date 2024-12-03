#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ~ import sympy
import sys
from random import shuffle as shf
day=sys.argv[0].split(".")[0][1:]
exp=f"exp{day}.txt"
real=f"d{day}.txt"
D={}
for line in open(0).read().splitlines():
	for i,c in enumerate(line):
		D[i,c]=D.get((i,c),0)+1
ll=i
s=""
t=""
for col in range(ll+1):
	if D[col,"0"]>D[col,"1"]:
		s+="0"
		t+="1"
	else:
		s+="1"
		t+="0"

gamma=int(s,2)
print (gamma)
epsilon=int(t,2)
print(epsilon)
print(gamma*epsilon)
