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
		self.con=set()
		NODES[pos]=self
		self.remote=""
SP=[nodes(v,k) for k,v in M.items() if v=="." and gets(k).count(".")==2]
print(len(SP))
TP=[nodes(v,k) for k,v in M.items() if v=="." and gets(k).count(".")==1]
print(len(TP))
FK=[nodes(v,k) for k,v in M.items() if v=="." and gets(k).count(".")>=3]
print(len(FK))
for n in TP:
	cont=next(p for p in around(n.pos) if M[p]!="#" and M[p]!=".")
	nxcont=2*cont-n.pos
	tl=[M[cont],M[nxcont]]
	tl.sort()
	tl="".join(tl)
	# ~ print (n.pos,tl)
	n.remote=tl
snode=next(n for n in TP if n.remote=="AA")
enode=next(n for n in TP if n.remote=="ZZ")
print(snode.pos,enode.pos)
for n in TP:
	try:c=next(z for z in TP if z.remote==n.remote and z!=n)
	except:continue
	n.con.add(c)
	c.con.add(n)
for n in NODES.values():
	for p in (p for p in around(n.pos) if M[p]=="."):
		t=NODES[p]
		n.con.add(t)
		t.con.add(n)
todo=[([snode],0)]
while True:
	path,d=todo.pop(0)
	cp=path[-1]
	if cp==enode:
		print(d)
		break
	for p in cp.con:
		if p in path:continue
		todo.append((path+[p],d+1))
