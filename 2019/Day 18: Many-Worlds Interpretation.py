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
def gets(p):
	return [M.get(tp,"#") for tp in around(p)]

def removedeadends(M):
	DE=[k for k,v in M.items() if (v=="." or v in locks) and gets(k).count("#")>=3]
	return DE
M[sp-1j]="#"
M[sp+1j]="#"
M[sp-1]="#"
M[sp+1]="#"
M[sp]="#"
SPS=(sp-1-1j,sp-1+1j,sp+1-1j,sp+1+1j)
for s in SPS:M[s]="@"
while True:
	TR=removedeadends(M)
	if not TR:break
	# ~ print(len(TR))
	for k in TR:M[k]="#"
draw()
input()
DE=[(k,v) for k,v in M.items() if v=="." and gets(k).count("#")==1 and v!="@"]
# ~ for i,(k,v) in enumerate(DE):M[k]=f"fork{i}"
# ~ draw()
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
for k,v in M.items():
	if v in locks or	v in keys:nodes(v,k)
for i,(k,v) in enumerate(DE):
	nodes(f"fork{i}",k)
for i,k in enumerate(SPS):
	nodes(f"start{i}",k)
print(len(NODES))

draw()
while True:
	try:cn=next(node for node in NODES.values() if gets(node.pos).count("#")==3 and M[node.pos]!="#" and not node.sym.startswith("start"))
	except:break
	nxpos=next(k for k in around(cn.pos) if M.get(k,"#")!="#")
	try:
		v=next(node for node in NODES.values() if node.pos==nxpos)
		print(v.sym)
		cn.con[v]=cn.d+1
		v.con[cn]=cn.d+1
		M[cn.pos]="#"
	except:
		M[cn.pos]="#"
		cn.pos=nxpos
		cn.d+=1
	# ~ draw()
	# ~ input()
# ~ for p in SPS:
	# ~ s=NODES[p]
	# ~ print(s.sym,[(t.sym,d) for t,d in s.con.items()])
for node in NODES.values():
	print (node.sym,[(p.sym,d) for p,d in node.con.items()])
input()
leave=False
todo=[(tuple(NODES[p] for p in SPS),"",0)]
visited={}
record=float("Inf")
while todo:
	newtodo=[]
	if leave:break
	for cpos,ks,steps in todo:
		# ~ print([p.sym for p in cpos],ks,steps)
		# ~ input()
		if leave:break
		currsit="".join([p.sym for p in cpos])+ks
		if visited.get(currsit,record)<steps:
			# ~ print("skipping")
			continue
		# ~ print(currsit)
		currkeys=[p.sym for p in cpos if p.sym in keys]
		# ~ print(currkeys)
		for k in currkeys:
			if k not in ks:
				ks+=k
				ks=list(ks)
				ks.sort()
				ks="".join(ks)
		currlocks=[p.sym for p in cpos if p.sym in locks]
		# ~ print(currlocks)
		for l in currlocks:
			if l not in ks:continue
		if all(s in ks for s in rk):
			print("ok:",pos,steps,ks)
			record=steps
			continue
			leave=True
			break
		for n,d in cpos[0].con.items():
			if n.sym in locks and n.sym.lower() not in ks:continue
			newtodo.append(((n,cpos[1],cpos[2],cpos[3]),ks,steps+d))
		for n,d in cpos[1].con.items():
			if n.sym in locks and n.sym.lower() not in ks:continue
			newtodo.append(((cpos[0],n,cpos[2],cpos[3]),ks,steps+d))
		for n,d in cpos[2].con.items():
			if n.sym in locks and n.sym.lower() not in ks:continue
			newtodo.append(((cpos[0],cpos[1],n,cpos[3]),ks,steps+d))
		for n,d in cpos[3].con.items():
			if n.sym in locks and n.sym.lower() not in ks:continue
			newtodo.append(((cpos[0],cpos[1],cpos[2],n),ks,steps+d))
		visited[currsit]=steps
	todo=set(newtodo)
	print(len(newtodo),len(todo),[p.sym for p in cpos],ks,steps)
	if not todo:break
# ~ < 2219
# ~ <2162
# ~ <2220 obviously
# ~ ?>2187
