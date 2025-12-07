#!/usr/bin/env python3
#
import itertools as it
fn,part="d5.txt",0
sep="\n\n"
fresh,ingred=open(fn).read().split(sep)[:2]
fresh,ingred=open(fn).read().split(sep)[2:]
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
F=[]
for line in fresh.splitlines():
	a,b=map(int,line.split("-"))
	F.append((a,b))
# ~ print(F)
res=0
def fre(v):
	for a,b in F:
		if a<=v<=b:return True
	return False
for l in ingred.splitlines():
	v=int(l)
	if fre(v):res+=1
print("p1 :",res)
while True:
	for (a,b),(c,d) in it.combinations(F,2):
		if b<c:continue
		if a>d:continue
		F.remove((a,b))
		F.remove((c,d))
		F.append((min(a,c),max(b,d)))
		break
	else:
		res=0
		for a,b in F:
			res+=b-a+1
		print ("p2 :",res)
		break

