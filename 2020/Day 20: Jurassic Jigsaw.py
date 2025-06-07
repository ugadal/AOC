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
	yield (b)
	yield (rot(b))
	yield (rot(rot(b)))
	yield (rot(rot(rot(b))))
	yield (flip(b))
	yield (flip(rot(b)))
	yield (flip(rot(rot(b))))
	yield (flip(rot(rot(rot(b)))))
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
p1=1
corners=[]
Conn={}
for k,b in B.items():
	Conn[k]=[]
	ok=0
	for t,c in B.items():
		if k==t:continue
		if sidebyside(b,c):
			ok+=1
			Conn[k].append(t)
	if ok==2:
		p1*=int(k)
		corners.append(k)
print("p1:",p1)
print(corners)
def isabove(a,b):
	return compare(a,b)
def isleftof(a,b):
	return compare(rot(a),b)
for corner in corners:
	print(corner,Conn[corner])
	base=B[corner]
	for cmp in Conn[corner]:
		tg=B[cmp]
		if any(isabove(base,ar) for ar in allrot(tg)) :print(cmp,"under",corner)
		if any(isleftof(base,ar) for ar in allrot(tg)) :print(cmp,"right of",corner)
		# ~ if isabove(base,flip(tg)):print(cmp,"flipped under",corner)
		# ~ if isleftof(base,tg):print(cmp,"right of",corner)
# ~ for k,v in Conn.items():
	# ~ print(k,v)
def cmpalb(a,b):
	rc="".join(x[-1] for x in a)
	# ~ for r in a:print(r)
	# ~ print()
	# ~ print(rc)
	# ~ print(rot(a)[-1])
	# ~ exit()
	
	return any(rc==x[-1] for x in allrot(b))
for b in corners:
	for k,v in B.items():
		if b==k:continue
		if cmpalb(B[b],v):print(b,"left of",k)
# ~ b=corners[-1]
# ~ print(b)
# ~ for row in B[b]:print(row)
# ~ print()
# ~ def edges(a):
	# ~ for z in allrot(a):
		# ~ yield z[-1]
# ~ for edg in edges(B[b]):print(edg)
