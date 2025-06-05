#!/usr/bin/env python
# -*- coding: utf-8 -*-
part=0
import re
import sys
cp=str(sys.argv[0])
dre=re.compile(r"^Day (\d+):")
day=dre.findall(cp)[0]
fn=f"d{day}.txt"
p=re.compile(r"\(([^()]*)\)")
s='1 + (2 * 3) + (4 * (5 + 6))'
def meval(S):
	r=p.search(S)
	while r:
		# ~ print(r)
		d,f=r.span()
		return meval(S[:d] + meval(S[d+1:f-1])+S[f:])
	# ~ print("evaluating",S)
	V=S.split()
	res=int(V.pop(0))
	while V:
		o=V.pop(0)
		v=int(V.pop(0))
		if o=="+":res+=v
		else:res*=v
	# ~ print("returning",res)
	return (str(res))
# ~ print(meval("1 + 2 * 3 + 4 * 5 + 6"))
# ~ print(meval("1 + (2 * 3) + (4 * (5 + 6))"))
# ~ print(meval("2 * 3 + (4 * 5)"))
# ~ print(meval("5 + (8 * 3 + 9 + 3 * 4 * 3)"))
# ~ print(meval("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))"))
# ~ print(meval("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2 "))
res=0
for line in open(fn).readlines():
	res+=int(meval(line))
print("p1:",res)
ps=re.compile(r"\d+ \+ \d+")
def mevaltwo(S):
	# ~ print("evaluation of ",S)
	r=p.search(S)
	while r:
		# ~ print(r)
		d,f=r.span()
		return mevaltwo( S[:d] + mevaltwo(S[d+1:f-1]) + S[f:])
	# ~ print("evaluating",S)
	r=ps.search(S)
	while r:
		d,f=r.span()
		# ~ print(r,d,f)
		# ~ print(S[d:f])
		# ~ input()
		a,b=map(int,S[d:f].split(" + "))
		return mevaltwo(S[:d] + str(a+b) + S[f:])
	V=S.split()
	res=int(V.pop(0))
	while V:
		o=V.pop(0)
		v=int(V.pop(0))
		res*=v
	# ~ print("returning",res)
	return (str(res))
# ~ print(mevaltwo("1 + 2 * 3 + 4 * 5 + 6"))
# ~ print(mevaltwo("1 + (2 * 3) + (4 * (5 + 6))"))
# ~ print(mevaltwo("2 * 3 + (4 * 5)"))
# ~ print(mevaltwo("5 + (8 * 3 + 9 + 3 * 4 * 3)"))
# ~ print(mevaltwo("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))"))
# ~ print(mevaltwo("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2 "))
res=0
for line in open(fn).readlines():
	res+=int(mevaltwo(line))
print("p2:",res)
