#!/usr/bin/env python
# -*- coding: utf-8 -*-
part=0
import re
import sys
import itertools as it
from functools import cache
import uuid
cp=str(sys.argv[0])
dre=re.compile(r"^Day (\d+):")
day=dre.findall(cp)[0]
fn=f"d{day}.txt"
blocks=open(fn).read().split("\n\n\n")[part]
pa,pb=blocks.split("\n\n")
pa=list(map(int,(line for line in pa.splitlines()[1:])))
pb=list(map(int,(line for line in pb.splitlines()[1:])))

while pa and pb:
	a=pa.pop(0)
	b=pb.pop(0)
	if a>b:
		pa.append(a)
		pa.append(b)
	else:
		pb.append(b)
		pb.append(a)
w=pa if pa else pb
w.reverse()
print("p1:",sum((i+1)*v for i,v in enumerate(w)))
pa=list(map(int,(line for line in pa.splitlines()[1:])))
pb=list(map(int,(line for line in pb.splitlines()[1:])))
def game(A,B):
	if not A:return "b",B
	if not B:return "a",A
	if A[0]>len[A] and B[0]>len(B):
		hold=A[0],B[0]
		winner,deck=game(A[1:],B[1:])
		
