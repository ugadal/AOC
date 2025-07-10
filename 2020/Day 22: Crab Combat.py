#!/usr/bin/env python
# -*- coding: utf-8 -*-
part=1
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
sys.setrecursionlimit(10000)
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
def game(A,B):
	oa=A
	ob=B
	print("started new (sub)game")
	print(oa)
	print(ob)
	V=set()
	def turn(A,B):
		# ~ print("started new turn")
		# ~ print(A)
		# ~ print(B)
		if (A,B) in V:return "a"
		V.add((A,B))
		if not A:
			print("p2:",sum((i+1)*int(v) for i,v in enumerate(reversed(B.split(",")))))
			return "b"
		if not B:
			print("p2:",sum((i+1)*int(v) for i,v in enumerate(reversed(A.split(",")))))
			return "a"
		A=list(A.split(","))
		B=list(B.split(","))
		if int(A[0])<len(A) and int(B[0])<len(B) and True:
			hold=A[0],B[0]
			winner=game(",".join(A[1:1+int(A[0])]),",".join(B[1:1+int(B[0])]))
			if winner=="a":
				res=turn(",".join(A[1:]+[hold[0],hold[1]]),",".join(B[1:]))
			else:
				res=turn(",".join(A[1:]),",".join(B[1:]+[hold[1],hold[0]]))
			return res
		if int(A[0]) > int(B[0]):
			res=turn(",".join(A[1:]+[A[0],B[0]]),",".join(B[1:]))
		else:
			res=turn(",".join(A[1:]),",".join(B[1:]+[B[0],A[0]]))
		return res
	return turn(A,B)
print(game(",".join(pa),",".join(pb)))
# ~ n=8
# ~ for c in it.permutations(range(1,n+1)):
	# ~ pa=",".join(map(str,c[:n//2]))
	# ~ pb=",".join(map(str,c[n//2:]))
	# ~ print(pa,pb)
	# ~ print (game(pa,pb))
