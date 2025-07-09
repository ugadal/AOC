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
sys.setrecursionlimit(1000000000)
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
pa,pb=blocks.split("\n\n")
pa=list(pa.splitlines()[1:])
pb=list(pb.splitlines()[1:])
# ~ @cache
K={}
# ~ @cache
def game(A,B):
	# ~ global K
	print(len(K))
	oa=A
	ob=B
	print(oa)
	print(ob)
	if A+":"+B in K:return K[A+":"+B]
	if B+":"+A in K:return "a" if K[A+":"+B]=="b" else "b"
	if not A:
		K[A+":"+B]="b"
		print("p2:",sum((i+1)*int(v) for i,v in enumerate(reversed(B.split(",")))))
		return "b"
	if not B:
		K[A+":"+B]="a"
		print("p2:",sum((i+1)*int(v) for i,v in enumerate(reversed(A.split(",")))))
		return "a"
	# ~ print()
	# ~ print("A:",A)
	# ~ print("B:",B)
	A=list(A.split(","))
	B=list(B.split(","))
	# ~ print(f"A:{A}")
	# ~ print(f"B:{B}")
	# ~ print("p2:",sum((i+1)*int(v) for i,v in enumerate(reversed(A))))
	# ~ print("p2:",sum((i+1)*int(v) for i,v in enumerate(reversed(B))))
	# ~ print("p2:",sum((i+1)*int(v) for i,v in enumerate(reversed(A))))
	# ~ print("p2:",sum((i+1)*int(v) for i,v in enumerate(reversed(B))))
	if int(A[0])<len(A) and int(B[0])<len(B) and True:
		hold=A[0],B[0]
		winner=game(",".join(A[1:1+int(A[0])]),",".join(B[1:1+int(B[0])]))
		if winner=="a":
			res=game(",".join(A[1:]+[hold[0],hold[1]]),",".join(B[1:]))
		else:
			res=game(",".join(A[1:]),",".join(B[1:]+[hold[1],hold[0]]))
		K[oa+":"+ob]=res
		return res
	if int(A[0]) > int(B[0]):
		res=game(",".join(A[1:]+[A[0],B[0]]),",".join(B[1:]))
	else:
		res=game(",".join(A[1:]),",".join(B[1:]+[B[0],A[0]]))
	K[oa+":"+ob]=res
	return res
# ~ print(game([10],[8,9]))	
# ~ print(pa)
print(game(",".join(pa),",".join(pb)))

