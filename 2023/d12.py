#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# ~ "#.#.###"
import itertools as it
from alive_progress import alive_bar
def contiguous(s):
	C=[]
	if s[0]=="#":ttl=1
	else :ttl=0
	for c in s[1:]:
		if c=="#":ttl+=1
		else:
			if ttl:C.append(ttl)
			ttl=0
	if ttl:C.append(ttl)
	return tuple(C)
def sub(s,P):
	L=list(s)
	for p in P:L[p]="#"
	return "".join(L)
def ana(l):
	a,b=l.split()	
	exp=tuple(map(int,b.split(",")))
	ttexp=sum(exp)
	print(a)
	print(exp,ttexp)
	if contiguous(a)==exp:return 1
	already_in=a.count("#")
	qm=[i for i,s in enumerate(a) if s=="?"]
	# ~ print(already_in,qm)
	z=a.replace("?",".")
	tc=0
	for p in it.combinations(qm,ttexp-already_in):
		if contiguous(sub(z,p))==exp:tc+=1
	return tc
def validate(s,wanted):
	# ~ print("validating",s,wanted)
	tc=contiguous(s)
	# ~ print(tc)
	for a,b in zip(tc[:-1],wanted[:-1]):
		if a!=b:return False
	return True
def anab(l):
	a,b=l.split()	
	a="?".join([a]*5)
	hit=0
	exp=tuple(map(int,b.split(",")*5))
	print(a,exp)
	# ~ print(a)
	# ~ print(exp)
	with alive_bar(0) as bar:
		P=[""]
		while P:
			curr=P.pop()
			p=len(curr)
			if p==len(a):
				if contiguous(curr)==exp:
					# ~ print ("XXXX",curr)
					hit+=1
				continue
			# ~ print("curr",curr,p,s[p])
			match a[p]:
				case "#":
					curr+="#"
					if validate (curr,exp):P.append(curr)
				case ".":
					curr+="."
					if validate (curr,exp):P.append(curr)
				case "?":
					if validate (curr+"#",exp):P.append(curr+"#")
					if validate (curr+".",exp):P.append(curr+".")
			bar()
	print("returning",hit)
	return hit
		
ex="""???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1"""

D=0
# ~ for l in ex.splitlines():
for l in open("d12.txt").read().splitlines():
	D+=anab(l)
print(D)
# ~ with alive_bar(6) as bar:
	
