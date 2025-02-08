#!/usr/bin/env python
# -*- coding: utf-8 -*-
fn,part="d20.txt",0
data=open(fn).read().split("\n\n")[part]
M={}
for r,row in enumerate(data.splitlines()):
	for c,s in enumerate(row):
		pos=complex(c,r)
		M[pos]=s
NR=r+1
NC=c+1
def draw(cp=-1):
	mic=int(min(m.real for m in M))
	mxc=int(max(m.real for m in M))
	mir=int(min(m.imag for m in M))
	mxr=int(max(m.imag for m in M))
	S=complex(-10,-10)
	for r in range(mir,mxr+1):
		R=[]
		for c in range(mic,mxc+1):
			pos=complex(c,r)
			if pos==S:sym="S"
			elif pos==cp:sym="D"
			else:sym=M.get(pos,"?")
			R.append(sym)
		print("".join(R))
	print() 
draw()
def around(p):
	yield p-1
	yield p+1
	yield p+1j
	yield p-1j
def gets(p):
	return [M.get(tp,"#") for tp in around(p)]

def removedeadends(M):
	DE=[k for k,v in M.items() if v=="." and gets(k).count("#")>=3]
	return DE
while True:
	TR=removedeadends(M)
	if not TR:break
	for k in TR:M[k]="#"
draw()

NODES={}
class nodes():
	def __init__(self,sym,pos):
		# ~ global NODES
		self.sym=sym
		self.pos=pos
		self.con={}
		self.l=None
		self.r=None
		self.b=None
		self.t=None
		# ~ NODES[sym]=self
		NODES[pos]=self
		self.d=0
SP=[nodes(v,k) for k,v in M.items() if v=="." and gets(k).count(".")==2]
print(len(SP))
TP=[nodes(v,k) for k,v in M.items() if v=="." and gets(k).count(".")==1]
print(len(TP))
FK=[nodes(v,k) for k,v in M.items() if v=="." and gets(k).count(".")>=3]
print(len(FK))
for n in TP:
	print (n.sym,n.pos,gets(n.pos))
