#!/usr/bin/env python3
#
sep="\n\n"
fn,part="d15.txt",8
grid,moves=open(fn).read().split(sep)[part:part+2]
moves="".join(moves.splitlines())
DM={'^':-1j,">":1,"<":-1,"v":1j}
G={}
for row,line in enumerate(grid.splitlines()):
	for col,s in enumerate(line.strip()):
		p=2*col+row*1j
		if s=="@":
			sp=p
			s="."
		if s=="O":
			G[p]="["
			G[p+1]="]"
		else:
			G[p]=s
			G[p+1]=s
NR=row+1
NC=2*col+2
def connecteddirH(pos,dm):
	if G[pos]=="]":pos-=1
	good=set()
	good.add(pos)
	todo=[pos]
	while todo:
		cpo=todo.pop()
		npo=cpo+2*dm
		if G[npo]=="[":
			good.add(npo)
			todo.append(npo)
	return good			
def connecteddirV(pos,dm):
	if G[pos]=="]":pos-=1
	good=set()
	good.add(pos)
	todo=[pos]
	while todo:
		cpo=todo.pop()
		npo=cpo+dm
		if G[npo]=="[":
			good.add(npo)
			todo.append(npo)
		if G[npo]=="]":
			good.add(npo-1)
			todo.append(npo-1)
		npo+=1
		if G[npo]=="[":
			good.add(npo)
			todo.append(npo)
	return good			

def connecteddir(pos,dm):
	if dm.real:return connecteddirH(pos,dm)
	else:return connecteddirV(pos,dm)
			
cpos=sp
print(sp)

def draw(cpos,s="@"):
	for row in range(NR):
		t=[]
		for col in range(NC):
			tp=col+row*1j
			if tp==cpos:t.append(s)
			else:t.append(G[tp])
		print("".join(t) )
# ~ input("resize window then enter")
# ~ draw(cpos)

for dnum,d in enumerate(moves):
	dm=DM[d]
	nc=cpos+dm
	if G.get(nc,".")==".":
		cpos+=dm
		continue
	if G.get(nc,".")=="#":continue
	B=connecteddir(nc,dm)
	if any(G.get(pos+dm)=="#" or G.get(pos+dm+1)=="#" for pos in B):pass
	else:
		for pos in B:
			G[pos]="."
			G[pos+1]="."
		for pos in B:
			G[pos+dm]="["
			G[pos+dm+1]="]"
		cpos=nc
# ~ draw(cpos)
print(sum(100*p.imag+p.real for p,v in G.items() if v=="["))
