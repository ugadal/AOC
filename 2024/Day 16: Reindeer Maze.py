#!/usr/bin/env python3
#
sep="\n\n"
fn,part="d16.txt",2
grid=open(fn).read().split(sep)[part]
G={}
for row,line in enumerate(grid.splitlines()):
	for col,s in enumerate(line.strip()):
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
todo=[(sp,1,0)]
record=float("inf")
while todo:
	cp,cd,cs=todo.pop(0)
	# ~ print(f"pos {cp}, dir {cd}, cs {cs}")
	if cs>record:continue
	if (cp,cd) in V and V[(cp,cd)]<cs:continue
	if cp==ep:
		print (cs)
		record=cs
		continue
	if G[cp+cd]!="#":todo.append((cp+cd,cd,cs+1))
	todo.append((cp,cd*1j,cs+1000))
	todo.append((cp,cd*(-1j),cs+1000))
	V[(cp,cd)]=cs
# ~ 124428 too high
