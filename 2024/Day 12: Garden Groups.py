#!/usr/bin/env python3
#
sep="\n\n"
fn,part="d12.txt",5
data=open(fn).read().split(sep)[part].splitlines()
# ~ from functools import cache
G={}
for row,line in enumerate(data):
	for col,s in enumerate(line):G[col+row*1j]=s
NR=row+1
NC=col+1
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
# ~ def interior(S,s): pick theorem un-applyable today because of interior polygons
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
def price(S,s):
	area=len(S)
	perimeter=sum(nfence(p) for p in S)
	print(f"symbol: {s} area {area} perimeter {perimeter}")
	price=area*perimeter
	return price
todo=set(G.keys())
cost=0
while todo:
	p=todo.pop()
	todo.add(p)
	g=group(p)
	currs=G[p]
	pr=price(g,currs)
	print(currs,pr)
	cost+=pr
	for p in g:todo.remove(p)
print(cost)
