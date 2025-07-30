#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import sys
m=re.compile("^(\S+) = \((\S+), (\S+)\)")
fn=sys.argv[1]
def lorr(rule):
	while True:
		for c in rule:yield c
Problems=open(fn).read().strip().split("\n\n")
print (len(Problems))
for p in Problems:
	print (p)
	print("*"*66)
rule=Problems[0].splitlines()[0]
print(rule,len(rule))
D={}
for line in Problems[1].splitlines():
	k,g,d=m.search(line).groups()
	# ~ print(k,g,d)
	D[(k,"L")]=g
	D[(k,"R")]=d
c=lorr(rule)
thisdir=next(c)
starts=[a for a,b in D.keys()	if a.endswith("A") and b==thisdir]
print(starts)
for start in starts:
	starters=[start]
	path=[start]
	k=start
	loops=0
	while True:
		loops+=1
		for c in rule:
			k=D[(k,c)]
			path.append(k)
		if k in starters:
			print("looped",loops,starters.index(k))
			break
		starters.append(k)
	print (len(starters),starters,len(path))
	ewz=[i for i,k in enumerate(path) if k.endswith("Z")]
	print(ewz)
for start in starts:
	path=[start]	
	print(start)
	loops=0
	while True:
		loops+=1
		for c in rule:
			k=D[(k,c)]
			path.append(k)
		ewz=[i for i,k in enumerate(path) if k.endswith("Z")]
		if len(ewz)==3:
			print(ewz,len(path),loops)
			break
start=starts[5]
path=[start]
k=start
print("---")
for loop in range(200):
	for c in rule:
		k=D[(k,c)]
		path.append(k)
ewz=[i for i,k in enumerate(path) if k.endswith("Z")]
print(ewz)
print(path[20777])
print(path[41554])

steps=[20277,18673,13939,17621,19199,12361]
P=list(steps)

		
	# ~ input()
	# ~ while cycdec[-1] not in cycdec[:-1]:
		# ~ k,_=cycdec.pop()
		# ~ for c in rule:
			# ~ cycdec.append((k,c))
			# ~ k=D[(k,c)]
		# ~ cycdec.append((k,rule[0]))
		# ~ print (len(cycdec),cycdec)
		# ~ input()
	# ~ ewz=[i for i,(k,r) in enumerate(cycdec) if k.endswith("Z")]
	# ~ print(ewz)
			
	# ~ print (cycdec.index((k,thisdir)))
	# ~ ewz=[i for i,(k,r) in enumerate(cycdec) if k.endswith("Z")]
	# ~ print(ewz)
exit()
c=lorr(rule)
steps=0
while [k.endswith("Z") for k in starts].count(False):
	thisdir=next(c)
	steps+=1
	starts=[D[(k,thisdir)] for k in starts]
	# ~ print(steps,starts)
	
print(steps)
