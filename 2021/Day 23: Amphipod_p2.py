#!/usr/bin/env python
# -*- coding: utf-8 -*-
part=0
def repres(p,v):print(f"p{p}: {v}")
import re
import sys
import itertools as it
from functools import cache
# ~ import uuid
# ~ import numpy as np
cp=str(sys.argv[0])
dre=re.compile(r"^Day (\d+):")
day=dre.findall(cp)[0]
fn=f"d{day}.txt"
# ~ block=open(fn).read().split("\n\n\n")[part]
# ~ block=open(fn).read().split("\n\n")[part]
rec=float("inf")
class sit():
	def __init__(self):
		self.lobby="-"*11
		self.h="-"*8
		self.e=0
	def copy(self):
		new=sit()
		new.lobby=self.lobby
		new.h=self.h
		new.e=self.e
		return new
	def rep(self):
		return (self.lobby+":"+self.h,self.e)
s=sit()
s.h="1130321031023202" #me
# ~ s.h="1213321031020320" #example
todo=[s]
visited={}
# ~ visited[s.rep()[0]]=s.e
done=0
skipped=0
while todo:
	cs=todo.pop(0)
	print("\rentering",cs.rep(),skipped,done,end="")
	if cs.h=="0123012301230123":
		print (cs.rep())
		rec=min(rec,cs.e)
		continue
	if cs.e>rec:
		skipped+=1
		continue
	if cs.rep()[0] in visited and cs.e>=visited[cs.rep()[0]]:
		skipped+=1
		continue
	for hx in range(4):
		house_content="".join(cs.h[hx+4*depth] for depth in range(4))
		# ~ print("hc",house_content)
		if house_content=="----":continue
		depth=next(i for i,c in enumerate(house_content) if c!="-")
		# ~ print("mob at depth",depth)
		# ~ cm=cs.h[hx]
		cm=house_content[depth]
		# ~ print(cm,hx)
		thismobpos=hx+4*depth
		# ~ move to lobby
		lobpos=2+2*hx
		# ~ print(lobpos)
		if cs.lobby[lobpos]!="-":continue
		aplob=[]
		for x in range(lobpos-1,-1,-1):
			if cs.lobby[x]!="-":break
			if x in [2,4,6,8]:continue
			aplob.append(x)
		for x in range(lobpos+1,11):
			if cs.lobby[x]!="-":break
			if x in [2,4,6,8]:continue
			aplob.append(x)
		# ~ print(aplob)
		for nl in aplob:
			ns=cs.copy()
			ns.lobby=cs.lobby[:nl]+cm+cs.lobby[nl+1:]
			ns.h=cs.h[:thismobpos]+"-"+cs.h[thismobpos+1:]
			ns.e+=(abs(nl-lobpos)+1+depth)*10**int(cm)
			# ~ print(ns.rep())
			todo.append(ns)
		# ~ input()
		
	for lp in range(11):
		cm=cs.lobby[lp]
		if cm=="-":continue
		icm=int(cm)
		house_content="".join(cs.h[icm+4*depth] for depth in range(4))
		# ~ occ=cs.h[icm]+cs.h[icm+4]
		if any(house_content.count(mob) for mob in "0123" if mob!=cm):
			# ~ print(f"skipping trying to move mob {cm} cos home is composed of {occ}")
			# ~ input()
			continue
		depth=[d for d,c in enumerate(house_content) if c=="-"][-1]
		hp=2+2*icm
		la,lb=lp,hp
		clp=lp
		if la>lb:
			la,lb=lb,la
		if any (cs.lobby[w]!="-" for w in range(la+1,lb)):
			# ~ print(f"skipping trying to move mob {cm} cos path occupied hp {hp} clp {clp}")
			# ~ input()
			continue
		# ~ if occ=="--":
			# ~ move to bottom
		ns=cs.copy()
		ns.h=cs.h[:icm+4*depth]+cm+cs.h[icm+4*depth+1:]
		ns.lobby=cs.lobby[:lp]+"-"+cs.lobby[lp+1:]
		ns.e+=(abs(hp-clp)+depth+1)*10**icm
		todo.append(ns)
			# ~ print (f"moved {cm} to bottom occ: {occ} home e:{(abs(hp-clp)+2)*10**icm}")
			# ~ print(ns.rep())
			# ~ input()
		# ~ else:
			# ~ ns=cs.copy()
			# ~ ns.h=cs.h[:icm]+cm+cs.h[icm+1:]
			# ~ ns.lobby=cs.lobby[:lp]+"-"+cs.lobby[lp+1:]
			# ~ ns.e+=(abs(hp-clp)+1)*10**icm
			# ~ todo.append(ns)
			# ~ print (f"moved {cm} to top occ {occ} home e:{(abs(hp-clp)+1)*10**icm}")
			# ~ print(ns.rep())
			# ~ input()
	visited[cs.rep()[0]]=cs.e
	done+=1
repres(2,rec)
