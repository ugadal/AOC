#!/usr/bin/env python3
#
sep="\n\n"
fn,part="d12.txt",5
data=open(fn).read().split(sep)[part].splitlines()
# ~ from functools import cache
G={}
for row,line in enumerate(data):
	for col,s in enumerate(line):G[col+row*1j]=s
def around(p):
	for d in [1,1j,-1,-1j]:
		yield p+d
def group(p):
	Visited=set()
	todo=[p]
	while todo:
		p=todo.pop()
		if p in Visited:continue
		for np in around(p):
			if G.get(np,"")==G[p]:todo.append(np)
		Visited.add(p)
	return Visited
# ~ def interior(S,s):
	# ~ mic=min(x.real for x in S)
	# ~ mac=max(x.real for x in S)
	# ~ mir=min(x.imag for x in S)
	# ~ mar=max(x.imag for x in S)
	# ~ count=0
	# ~ for p in S:
		# ~ if all(G.get(p+d,"")==s for d in [0,1,1j,1+1j]):
			# ~ count+=1
	# ~ return count
def nfence(p):
	res=sum(1 if G.get(x,"")!=G[p] else 0 for x in around(p))
	return res
def ofence(S,d,s): #oriented fence, d: direction n,s,e,w s:symbol=current crop
	F=set() # fences in direction d
	for c in S:
		if G.get(c+d,"")!=G[c]:F.add(c)
	tc=list(F)
	for c in tc:
		if c+s in F:F.remove(c+s)
	return len(F)
# ~ def price(S,s):
	# ~ area=len(S)
	# ~ perimeter=sum(nfence(p) for p in S)
	# ~ print(f"symbol: {s} area {area} perimeter {perimeter}")
	# ~ pick
	# ~ A=i+b/2 -1
	# ~ b=2*(A+1-i)
	# ~ intpoint=interior(S,s)
	# ~ perimeter=2*(area+1-intpoint)
	price=area*perimeter
	return price
todo=set(G.keys())
cost=0
while todo:
	p=todo.pop()
	todo.add(p)
	g=group(p)
	currs=G[p]
	area=len(g)
	nf=ofence(g,-1j,1)
	sf=ofence(g,1j,1)
	ef=ofence(g,1,1j)
	wf=ofence(g,-1,1j)
	fe=nf+sf+ef+wf
	cost+=area*fe
	for p in g:todo.remove(p)
print(cost)
