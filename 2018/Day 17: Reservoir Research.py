#!/usr/bin/env python
# -*- coding: utf-8 -*-
fn="d17.txt"
part=1
Clays=[]
W=[]
class drop():
	def __init__(self,pos=500):
		global W
		self.pos=pos+0*1j
		W.append(self)
		self.dir=1j
for line in open(fn).read().split("\n\n")[part].splitlines():
	D={}
	for part in line.split(", "):
		g,d=part.split("=")
		try:b=e=int(d)
		except:b,e=map(int,d.split(".."))
		D[g]=(b,e)
	for col in range(D["x"][0],D["x"][1]+1):
		for row in range(D["y"][0],D["y"][1]+1):
			Clays.append(col+row*1j)
			
mico=int(min(pos.real for pos in Clays))-1
maco=int(max(pos.real for pos in Clays))+1
miro=int(min(pos.imag for pos in Clays))
maro=int(max(pos.imag for pos in Clays))
M={}
for row in range(miro-5,maro+5):
	for col in range(mico-5,maco+5):
		M[col+row*1j]="."

drop()
for c in Clays:	M[c]="#"

def seek(pos,d):
	sp=pos
	while True:
		if M[sp+d]=="#":return True,sp
		if M[sp+d+1j]not in ("#","o"):return False,sp
		sp+=d
while W:
	P=[d.pos for d in W]
	P=list(set(P))
	W=[drop(d) for d in P]
	d=W.pop(0)
	ori=d.pos
	if M[ori]=="o":
		drop()
		continue
	while M[d.pos+1j]in (".","~"):
		M[d.pos]="~"
		d.pos+=1j
		if d.pos.imag>maro+1:break
	if d.pos.imag>maro+1:continue
	M[d.pos]="~"
	bag,pg=seek(d.pos,-1)
	bad,pd=seek(d.pos,1)
	symbol="o" if bag and bad else "~"
	sp=pg
	while sp.real<=pd.real:
		M[sp]=symbol
		sp+=1
	if bag and bad:drop(ori)
	if not bag:drop(pg-1)
	if not bad:drop(pd+1)

water=wetspot=0
for row in range(miro,maro+1):
	for col in range(mico,maco+1):
		if M[col+row*1j]=="o":water+=1
		elif M[col+row*1j]=="~":wetspot+=1
print(water,water+wetspot)
