#!/usr/bin/env python3
#
import re
print("part 1".center(60).title())
fn="everybody_codes_e2024_q03_p1.txt"
# ~ fn="t.txt"
G={}
for r,row in enumerate(open(fn).read().splitlines()):
	for c,s in enumerate(row):
		t=complex(c,r)
		G[t]=s
NR=r+1
NC=c+1
def rep():
	for r in range(NR):
		L=[]
		for c in range(NC):
			p=complex(c,r)
			L.append(str(G[p]))
		print("".join(L))
	print()
rep()
def around(p):
	yield p+1
	yield p-1
	yield p+1j
	yield p-1j
	
for k,v in G.items():
	if v=="#":G[k]=1
	# ~ if v==".":G[k]=-1
rep()
lvl=1
while True:
	todo=[]
	for k,v in G.items():
		if v!=lvl:	continue
		if all((G.get(p,-5)==lvl for p in around(k))):
			todo.append(k)
	if todo:
		for k in todo:G[k]=lvl+1
		lvl+=1
	else:break
print(todo,lvl)
rep()
print(sum(v for k,v in G.items() if v !="."))
print("part 2".center(60).title())
fn="everybody_codes_e2024_q03_p2.txt"
print("part 3".center(60).title())
fn="everybody_codes_e2024_q03_p3.txt"
