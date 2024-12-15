#!/usr/bin/env python3
#
sep="\n\n"
fn,part="d15.txt",2
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
NC=2*col+1
def getnextempty(cpos,dm):
	tpos=cpos+dm
	while True:
		if G.get(tpos)=="#":return -1000-1000*1j
		if G.get(tpos,".")!=".":tpos+=dm
		else:return tpos
cpos=sp
print(sp)
def draw():
	for row in range(NR):
		print( "".join( [ G.get(col+row*1j) for col in range(NC) ] ) )
draw()
exit()
for dnum,d in enumerate(moves):
	dm=DM[d]
	nc=cpos+dm
	if G.get(nc,".")==".":
		cpos+=dm
		continue
	if G.get(nc,".")=="#":continue
	ng=getnextempty(cpos,dm)
	if 0<=ng.real<NC and 0<=ng.imag<NR:
		G[ng]="O"
		G[nc]="."
		cpos=nc
	# ~ draw()
print(sum(100*p.imag+p.real for p,v in G.items() if v=="O"))
