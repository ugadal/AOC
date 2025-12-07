#!/usr/bin/env python3
#
import itertools as it
fn,part="d6.txt",1
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
L=[l.split() for l in L]
res=0
for v in zip(*L):
	op=v[-1]
	v=v[:-1]
	v=list(map(int,v))
	if op=="+":
		res+=sum(v)
	else:
		t=1
		for i in v:t*=i
		res+=t
print("p1 :",res)
L=data.splitlines()
t=0
res=0
for row in zip(*L):
	if row[-1]!=' ':
		op=row[-1]
		t=int("".join(row[:-1]))
		continue
	if all(s==" " for s in row):
		res+=t
		continue
	v=int("".join(row[:-1]))
	if op=="+":t+=v
	else:t*=v
print("p2 :",res+t)
		
