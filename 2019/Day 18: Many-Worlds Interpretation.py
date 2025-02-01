#!/usr/bin/env python
# -*- coding: utf-8 -*-
fn,part="d18.txt",4
data=open(fn).read().split("\n\n")[part]
# ~ print(data)
keys=list(map(chr,range(97,123)))
locks=list(map(chr,range(65,91)))
M={}
rk=[]
for r,row in enumerate(data.splitlines()):
	for c,s in enumerate(row):
		pos=complex(c,r)
		M[pos]=s
		if s=="@":sp=pos
		if s in keys:rk.append(s)
print(rk)
NR=r+1
NC=c+1
print(NR,NC,sp)
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
# ~ input()
def around(p):
	yield p-1
	yield p+1
	yield p+1j
	yield p-1j
def gets(p):return [M.get(tp,"#") for tp in around(p)]

def removedeadends(M):
	DE=[k for k,v in M.items() if (v=="." or v in locks) and gets(k).count("#")>=3]
	return DE
while True:
	TR=removedeadends(M)
	if not TR:break
	# ~ print(len(TR))
	for k in TR:M[k]="#"
draw()
# ~ exit()
# ~ input()
todo=[(sp,"",0)]
visited={}
leave=False
doit="n"
# ~ doit=input("do partone ?")
if doit=="y":doit=True
else:doit=False
while doit:
	newtodo=[]
	if leave:break
	for pos,ks,steps in todo:
		# ~ print(pos,ks,steps)
		if leave:break
		if all(s in ks for s in rk):
			print(pos,steps-1,ks)
			leave=True
			break
		if visited.get((pos,ks),float("Inf"))<steps:
			continue
		# ~ input()
		cs=M.get(pos,"#")
		if cs in keys and cs not in ks:
			ks+=cs
			ks=list(ks)
			ks.sort()
			ks="".join(ks)
		if cs in locks and cs.lower() not in ks:continue
		for np in around(pos):
			if M.get(np,"#")=="#":continue
			newtodo.append((np,ks,steps+1))
		visited[pos,ks]=steps
	todo=set(newtodo)
	print(len(newtodo),len(todo),pos,ks,steps)
	if not todo:break
# ~ print (visited)
# ~ p2
# ~ exit()
M[sp-1j]="#"
M[sp+1j]="#"
M[sp-1]="#"
M[sp+1]="#"
M[sp]="#"
SPS=(sp-1-1j,sp-1+1j,sp+1-1j,sp+1+1j)
for s in SPS:M[s]="@"
draw()
DE=[(k,v) for k,v in M.items() if v!="#" and gets(k).count("#")==1]
for k,v in DE:M[k]="§"
draw()
# ~ print(DE)
NODES={}
class nodes():
	def __init__(self,sym,pos):
		global NODES
		self.sym=sym
		self.pos=pos
		self.con={}
		# ~ NODES[sym]=self
		NODES[pos]=self
		self.d=0
		
while True:
	try:pos,sy=next((k,v) for k,v in M.items() if v not in "#.@" and gets(k).count("#")>=3)
	except:break
	print(pos,sy)	
	if pos in NODES:cn=NODES[pos]
	else:cn=nodes(sy,pos)
	print(cn)
	pn=next(k for k in around(pos) if M.get(k,"#")!="#")
	print(pn,M[pn])
	if M[pn]==".":
		M[pn]=sy
		M[pos]="#"
		cn.pos=pn
		cn.d+=1
		# ~ draw()
		# ~ input()
		continue
	if pn in NODES:nxn=NODES[pn]
	else:nxn=nodes(sy,pos)
	nxn.con[cn]=cn.d
	cn.con[nxn]=cn.d
	print(nxn.pos,nxn.con)
	M[cn.pos]="#"
	# ~ draw()
	# ~ input()
draw()
for x in SPS:
	cs=NODES[x]
	print(cs.con)
exit()
def gets(L):return [M.get(p,"#") for p in L]
todo=[(SPS,"",0)]
visited={}
print("=== P2 ===")
while True:
	newtodo=[]
	for PS,ks,steps in todo:
		if all(s in ks for s in rk):
			print(*PS,steps-1,ks)
			exit()
		if visited.get((str(PS),ks),float("Inf"))<steps:continue
		CS=gets(PS)
		if any([cs in locks and cs.lower() not in ks for cs in CS]):continue
		if any([cs in keys and cs not in ks for cs in CS]):
			for cs in [cs for cs in CS if cs in keys and cs not in ks]:
				ks+=cs
				ks=list(ks)
				ks.sort()
				ks="".join(ks)
		for p,pos in enumerate(PS):
			for np in around(pos):
				if M.get(np,"#")=="#":continue
				NP=list(PS)
				NP[p]=np
				newtodo.append((tuple(NP),ks,steps+1))
				# ~ print(newtodo)
				# ~ input()
		visited[str(PS),ks]=steps
	# ~ print(newtodo)
	todo=set(newtodo)
	print(len(todo),len(visited),PS,ks,steps)
		
