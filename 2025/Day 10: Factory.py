#!/usr/bin/env python3
#
from malib import *
# ~ part=0
data=open(fn).read().split(sep)[part]
res=0
for line in data.splitlines():
	parts=line.split()
	target=parts[0]
	buttons=parts[1:-1]
	goal=[True if c=="#" else False for c in target[1:-1]]
	buttons=[list(map(int,b[1:-1].split(",")))  for b in buttons ]
	press=1
	found=False
	while not found:
		for co in it.product(buttons,repeat=press):
			# ~ print("comb",co)
			status=[False]*len(goal)
			for but in co:
				for v in but:
					status[v]=not status[v]
			if status==goal:
				# ~ print("found",press)
				res+=press
				found=True
				break
		else:
			press+=1
print("p1 :",res)
res=0
for line in data.splitlines():
	parts=line.split()
	target=parts[-1]
	buttons=parts[1:-1]
	goal=list(map(int,target[1:-1].split(",")))
	buttons=[list(map(int,b[1:-1].split(",")))  for b in buttons ]
	pool=[]
	for but in buttons:
		mp=min(goal[v] for v in but)
		pool.extend([but]*mp)
	print(pool)
	# ~ exit()
	press=1
	found=False
	while not found:
		print(press)
		for co in it.combinations(pool,press):
			# ~ print("comb",co)
			status=[0]*len(goal)
			for but in co:
				for v in but:
					status[v]+=1
			if status==goal:
				# ~ print("found",press)
				res+=press
				found=True
				break
		else:
			press+=1
print("p2 :",res)
