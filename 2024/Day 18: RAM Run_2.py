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
draw()
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
		# ~ print("V",V)
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
draw()
exit()
sp=next(p for p,v in G.items() if v=="S")
ep=next(p for p,v in G.items() if v=="E")
print(sp,ep)
cpos=sp
sco=0
V={}
todo=[(sp,1,0,[])]
record=float("inf")
inpath=set()
while todo:
	cp,cd,cs,path=todo.pop(0)
	# ~ print(f"pos {cp}, dir {cd}, cs {cs}")
	if cs>record:continue
	if (cp,cd) in V and V[(cp,cd)]<cs:continue
	if cp==ep:
		if cs<record:
			inpath=set()
			record=cs
		if cs==record:
			for p in path:inpath.add(p)
			continue
	if G[cp+cd]!="#":todo.append((cp+cd,cd,cs+1,path+[cp]))
	todo.append((cp,cd*1j,cs+1000,path))
	todo.append((cp,cd*(-1j),cs+1000,path))
	V[(cp,cd)]=cs
print(record,len(inpath)+1)
