#!/usr/bin/env python
# -*- coding: utf-8 -*-
B={}
O={}
def mget(D,k,cc):
	if k in D:return D[k]
	return cc(k)
	
class cbot():
	def __init__(s,n):
		# ~ print(f"creating bot {n} {len(B)}")
		s.val=[]
		s.lot=None
		s.hit=None
		B[n]=s
	def trans(s):
		a,b=s.val
		if a>b:a,b=b,a
		s.lot.val.append(a)
		s.hit.val.append(b)
		s.val=[]
class coutp():
	def __init__(s,n):
		# ~ print(f"creating output {n}  {len(O)}")
		s.val=[]
		O[n]=s
for line in open(0).read().splitlines():
	if line.startswith("value"):
		_,v,_,_,_,b=line.split()
		v=int(v)
		b=int(b)
		bot=mget(B,b,cbot)
		bot.val.append(v)
	if line.startswith("bot "):
		E=line.split()
		bid=int(E[1])
		lot=int(E[6])
		hit=int(E[11])
		bot=mget(B,bid,cbot)
		if E[5]=="output":bot.lot=mget(O,lot,coutp)
		else:bot.lot=mget(B,lot,cbot)
		if E[10]=="output":bot.hit=mget(O,hit,coutp)
		else:bot.hit=mget(B,hit,cbot)
		
gottwo=[bot for i,bot in B.items() if len(bot.val)>=2]
while gottwo:
	for bot in gottwo:bot.trans()
	gottwo=[bot for i,bot in B.items() if len(bot.val)>=2]
for k in range(3):print(k,O[k].val)
