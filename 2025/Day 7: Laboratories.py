#!/usr/bin/env python3
#
import itertools as it
fn,part="d7.txt",1
sep="\n\n"
data=open(fn).read().split(sep)[part]
# ~ def readG(data):
	# ~ G={}
	# ~ for row,line in enumerate(data.splitlines()):
		# ~ for col,s in enumerate(line):
			# ~ pos=complex(col,row)
			# ~ G[pos]=s
	# ~ return G,row+1,col+1
# ~ G,R,C=readG(data)
# ~ def pmap(G):
	# ~ for row in range(R):
		# ~ print("".join([G[complex(col,row)] for col in range(C)]))
# ~ def around(pos):
	# ~ for dc in (-1,0,1):
		# ~ for dr in (-1j,0,1j):
			# ~ if dc+dr:yield pos+dc+dr
L=data.splitlines()
beams=[L[0].index("S")]
splitting=0
for l in L[1:]:
	if not l.count("^"):continue
	spl=[b for b in beams if l[b]=="^"]
	nospl=[b for b in beams if l[b]=="."]
	splitting+=len(spl)
	beams=set(b-1 for b in spl)
	beams=beams | set(b+1 for b in spl)
	beams=beams | set(nospl)
print("p1 :",splitting)
beams={}
beams[L[0].index("S")]=1
for l in L[1:]:
	if not l.count("^"):continue
	newbeams={}
	for beam,bc in beams.items():
		if l[beam]=="^":
			newbeams[beam-1]=newbeams.get(beam-1,0)+bc
			newbeams[beam+1]=newbeams.get(beam+1,0)+bc
		else:
			newbeams[beam]=newbeams.get(beam,0)+bc
	beams=newbeams
print("p2 :",sum(beams.values()))
