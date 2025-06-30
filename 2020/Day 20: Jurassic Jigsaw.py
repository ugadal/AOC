#!/usr/bin/env python
# -*- coding: utf-8 -*-
part=0
import re
import sys
cp=str(sys.argv[0])
dre=re.compile(r"^Day (\d+):")
day=dre.findall(cp)[0]
fn=f"d{day}.txt"
blocks=open(fn).read().split("\n\n")
B={}
for block in blocks:
	bid=block.splitlines()[0].split()[1][:-1]
	# ~ print(bid)
	B[bid]=block.splitlines()[1:]
# ~ print(len(B))
lb=B[bid]
# ~ print(lb)
# ~ for row in lb:print(row)
# ~ print()
def flip(b):
	return[r[::-1] for r in b]
# ~ for row in flip(lb):print(row)
def transpose(b):
	# ~ R=zip(*b)
	return ["".join(row) for row in zip(*b)]
def rot(b):
	return(flip(transpose(b)))
def rotl(b):
	return rot(rot(rot(b)))
# ~ print()	
# ~ for row in rot(lb):print(row)
def allrot(b):
	yield b
	yield rot(b)
	yield rot(rot(b))
	yield rotl(b)
	yield flip(b)
	yield flip(rot(b))
	yield flip(rot(rot(b)))
	yield flip(rotl(b))
def compare(x,y):return x[-1]==y[0]
def nmatch(x,y):
	return sum(1 if compare(x,z) else 0 for z in allrot(y))
# ~ for k,b in B.items():
	# ~ print(bid,k,nmatch(lb,b))
	# ~ print(bid,k,nmatch(rot(lb),b))
	# ~ print(bid,k,nmatch(rot(rot(lb)),b))
	# ~ print(bid,k,nmatch(rot(rot(rot(lb))),b))
# ~ for r in allrot(B["1871"]):
	# ~ for row in r:print(row)
	# ~ print()
def sidebyside(x,y):
	return	nmatch(x,y)+nmatch(rot(x),y)+nmatch(rot(rot(x)),y)+nmatch(rot(rot(rot(x))),y)
def toint(s):
	return int()
def desc(b):
	D=[]
	r=b[0]
	D.append(int("".join(["1" if c =="#" else "0" for c in r]),2))
	D.append(int("".join(["1" if c =="#" else "0" for c in r[::-1]]),2))
	r=b[-1]
	D.append(int("".join(["1" if c =="#" else "0" for c in r]),2))
	D.append(int("".join(["1" if c =="#" else "0" for c in r[::-1]]),2))
	r=[x[0] for x in b]
	D.append(int("".join(["1" if c =="#" else "0" for c in r]),2))
	D.append(int("".join(["1" if c =="#" else "0" for c in r[::-1]]),2))
	r=[x[-1] for x in b]
	D.append(int("".join(["1" if c =="#" else "0" for c in r]),2))
	D.append(int("".join(["1" if c =="#" else "0" for c in r[::-1]]),2))
	return D
p1=1
corners=[]
Conn={}
Desc={}
for k,b in B.items():
	Desc[k]=desc(b)
	print(Desc[k])
	Conn[k]=set()
for k in B.keys():
	for t in B.keys():
		if k==t:continue
		if set(Desc[k]) & set(Desc[t]):
			Conn[k].add(t)
			Conn[t].add(k)
corners=[]
p=1
for k in B.keys():
	if len(Conn[k])==2:
		print(k,Conn[k],len(Conn[k]))
		corners.append(k)
		p*=int(k)
print("p1:",p)
print(corners)		
# ~ find left
def isunder(a,b):
	for r in allrot(b):
		if compare(a,r):return True
	return False
def isleftof(a,b):
	v=rotl(a)
	for r in rot(b):
		if compare(v,r):return True
	return False
for corner in corners:
	for t in Conn[corner]:
		print(corner,t,"above",isabove(corner,t))
		print(corner,t,"left of",isleftof(corner,t))
exit()
todo=B.keys()
done=[]
positions={}
curr=todo.pop()
positions[curr]=(0,0)
while todo:
	for t in Conn[curr]:
		if t in done:continue
		
