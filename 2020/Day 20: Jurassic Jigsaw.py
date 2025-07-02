#!/usr/bin/env python
# -*- coding: utf-8 -*-
part=0
import re
import sys
import itertools as it
cp=str(sys.argv[0])
dre=re.compile(r"^Day (\d+):")
day=dre.findall(cp)[0]
fn=f"d{day}.txt"
blocks=open(fn).read().split("\n\n")
B={}
for block in blocks:
	bid=block.splitlines()[0].split()[1][:-1]
	B[bid]=block.splitlines()[1:]
lb=B[bid]
def flip(b):
	return[r[::-1] for r in b]
def transpose(b):
	return ["".join(row) for row in zip(*b)]
def rot(b):
	return flip(transpose(b))
def rotl(b):
	return rot(rot(rot(b)))
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
for k,t in it.combinations(B.keys(),2):
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
def isunder(a,b):
	for r in allrot(b):
		if a[-1]==r[0]:return r
	return False
def isleftof(a,b):
	v="".join(r[0] for r in a)
	for tr in allrot(b):
		w="".join(r[-1] for r in tr)
		if v==w:return tr
	return False
def isrightof(a,b):
	v="".join(r[-1] for r in a)
	for tr in allrot(b):
		w="".join(r[0] for r in tr)
		if v==w:return tr
	return False
def isabove(a,b):
	for r in allrot(b):
		if a[0]==r[-1]:return r
	return False
todo=list(B.keys())
done=[]
positions={}
curr=todo.pop(0)
positions[curr]=(0,0)
while todo:
	if curr not in positions:
		todo.append(curr)
		curr=todo.pop(0)
		continue
	print(f"working on {curr}: {Conn[curr]}")
	cr,cc=positions[curr]
	for t in Conn[curr]:
		# ~ print(f"positioning {t}")
		if t in done:
			print(f"skipping {t} already positioned")
			continue
		u=isunder(B[curr],B[t])
		if u:
			print(t,"under",curr)
			B[t]=u
			positions[t]=(cr+1,cc)
			continue
		u=isleftof(B[curr],B[t])
		if u:
			print(t,"left of",curr)
			B[t]=u
			positions[t]=(cr,cc-1)
			continue
		u=isrightof(B[curr],B[t])
		if u:
			print(t,"right of",curr)
			B[t]=u
			positions[t]=(cr,cc+1)
			continue
		u=isabove(B[curr],B[t])
		if u:
			print(t,"above of",curr)
			B[t]=u
			positions[t]=(cr-1,cc)
			continue
		else:
			print("not positioned")
			input()
	done.append(curr)
	curr=todo.pop(0)
mir=min(r for r,c in positions.values())
mic=min(c for r,c in positions.values())
print(mir,mic)
postopiece={}
for k,(r,c) in positions.items():
	positions[k]=r-mir,c-mic
	postopiece[r-mir,c-mic]=k
print(postopiece.keys())
mxr=max(r for r,c in positions.values())
mxc=max(c for r,c in positions.values())
print(mxr,mxc)
tl=postopiece[0,0]
def shorten(b):	return [row[1:-1] for row in b[1:-1]]
for k,v in B.items():
	B[k]=shorten(v)
ss=len(B[tl][0])
nmap=set()
for r in range(mxr+1):
	br=r*ss
	for c in range(mxc+1):
		bc=c*ss
		block=B[postopiece[r,c]]
		for ir,row in enumerate(block):
			for ic,c in enumerate(row):
				if c=="#":
					pos=complex(bc+ic,br+ir)
					nmap.add(pos)
smt="""                  # 
#    ##    ##    ###
 #  #  #  #  #  #   """
sm=set()
for r,row in enumerate(smt.splitlines()):
	for c,s in enumerate(row):
		if s=="#":
			pos=complex(c,r)
			sm.add(pos)
mxr=int(max(pos.imag for pos in nmap))
mxc=int(max(pos.real for pos in nmap))
nmap={complex(mxc-(x.real),x.imag) for x in nmap} #flip
for x in range(3): #rot 3 times
	nmap={x*1j for x in nmap}
	mir=min(pos.imag for pos in nmap)
	mic=min(pos.real for pos in nmap)
	nmap={x-mir-mic for x in nmap}
insm=set()
mxr=int(max(pos.imag for pos in nmap))
mxc=int(max(pos.real for pos in nmap))
print(sm,mxr,mxc)
for row in range(mxr+1):
	for col in range(mxc+1):
		base=complex(col,row)
		smp={s+base for s in sm}
		inter=smp&nmap
		if (smp&nmap)==smp:
			insm=insm|smp
print(len(nmap-insm))
