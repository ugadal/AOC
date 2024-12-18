#!/usr/bin/env python3
#
sep="\n\n"
fn,part="d18.txt",1
grid=open(fn).read().split(sep)[part].splitlines()
G={}
NR=71
NC=71
for row in range(NR):
	for col in range(NC):
		p=col+row*1j
		G[p]="."
rocks=[]
for line in grid:
	col,row=line.split(',')
	col=int(col)
	row=int(row)
	p=col+row*1j
	rocks.append(p)
for p in rocks[:1024]:G[p]="#"
target=NC-1+(NR-1)*1j
print(target)
def around(p):
	yield p+1
	yield p+1j
	yield p-1
	yield p-1j
def draw():
	for row in range(NR):
		print( "".join( [ G.get(col+row*1j,"#") for col in range(NC) ] ) )
# ~ draw()
def seekpath():
	shortest=float("Inf")
	V=set()
	todo=[(0+0*1j,0,[])]
	bp=[]
	while todo:
		cpos,l,path=todo.pop(0)
		if cpos==target:
			if l<shortest:
				shortest=l
				bp=path.copy()
			continue
		if l>=shortest:continue
		if cpos in V:continue
		for np in around(cpos):
			if G.get(np,"#")==".":todo.append((np,l+1,path+[cpos]))
		V.add(cpos)
	return shortest,bp
r,bp=seekpath()	
for rock in rocks[1024:]:
	G[rock]="#"
	if not rock in bp:continue
	d,bp=seekpath()
	if not bp:
		print (rock,d)
		break
	else:print(rock,d)
