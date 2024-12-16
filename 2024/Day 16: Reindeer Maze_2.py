#!/usr/bin/env python3
#
sep="\n\n"
fn,part="d16.txt",2
grid=open(fn).read().split(sep)[part].splitlines()
G={}
for row,line in enumerate(grid):
	for col,s in enumerate(line):
		p=col+row*1j
		G[p]=s
NR=row+1
NC=col+1
def draw():
	for row in range(NR):
		print( "".join( [ G.get(col+row*1j) for col in range(NC) ] ) )
draw()
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
