#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  day5.py
parts=open(0).read().strip().split("\n\n")
oriseeds=list(map(int,parts.pop(0).split(":")[1].split()))
seeds=list(oriseeds)
def genfun(targ,beg,ran):
	def x(v):
		if beg<=v<beg+ran:return (True,targ-beg+v)
		return(False,v)
	return x
def genfunp2(t,c,d):
	def x(a,b):
			untouched=[]
			print(a,a+b-1)
			if a>=c+d:return(False,[f"over right limit {c} {c+d-1}"])
			if a+b<=c:return(False,[f"behind left limit {c} {c+d-1}"])
			if a<=c and a+b<=c+d: # 3
				if c-a:untouched.append((a,c-a))
				changed=(t,b+a-c)
				return(True,untouched,changed)
			if c+d+1<=a+b+1 and c<a: # 4
				if a+b-1 -c-d+1:untouched.append((c+d,a+b-c-d))
				changed=(t+a-c,)
				return(True,untouched,changed)
			return("untreated")
	return x
# ~ test=genfun(10,50,11)
# ~ for x in range(40,70):print(x,test(x))
# ~ print(seeds)
for part in parts:
	FUN=[genfun(*map(int,rule.split())) for rule in part.splitlines()[1:]]
	NS=[]
	for seed in seeds:
		for fun in FUN:
			boo,v=fun(seed)
			if boo:
				NS.append(v)
				break
		else:NS.append(seed)
	# ~ print(NS)
	seeds=list(NS)
print (min(seeds))
seeds=list(oriseeds)
new_seeds=[]
while seeds:
	a=seeds.pop(0)
	b=seeds.pop(0)
	new_seeds.append((a,b))
for part in parts:
	FUN=[genfunp2(*map(int,rule.split())) for rule in part.splitlines()[1:]]

test=genfunp2(50,60,11)
print(test(40,11))
print(test(80,11))
print(test(55,8))
print(test(60,8))
print(test(65,11))
