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
s.h="11303202" #me
# ~ s.h="12130320" #example
todo=[s]
visited={}
# ~ visited[s.rep()[0]]=s.e
done=0
skipped=0
while todo:
	cs=todo.pop(0)
	print("\rentering",cs.rep(),skipped,done,end="")
	if cs.h=="01230123":
		print (cs.rep())
		rec=min(rec,cs.e)
		continue
	if cs.e>rec:
		skipped+=1
		continue
	if cs.rep()[0] in visited and cs.e>=visited[cs.rep()[0]]:
		# ~ print(cs.rep())
		# ~ print("skipped already visited")
		# ~ print(visited[cs.rep()])
		# ~ input()
		skipped+=1
		continue
	for hx in range(4):
		cm=cs.h[hx]
		# ~ print(cm,hx)
		if cm!="-":
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
				ns.h=cs.h[:hx]+"-"+cs.h[hx+1:]
				ns.e+=(abs(nl-lobpos)+1)*10**int(cm)
				# ~ print(ns.rep())
				todo.append(ns)
			# ~ exit()
	for hx in range(4):
		cm=cs.h[hx]
		# ~ print(cm,hx)
		if cm=="-":
			if cs.h[hx+4]=="-":continue
			cm=cs.h[hx+4]
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
				ns.h=cs.h[:hx+4]+"-"+cs.h[hx+5:]
				ns.e+=(abs(nl-lobpos)+2)*10**int(cm)
				# ~ print(ns.rep())
				todo.append(ns)
			# ~ exit()
	for lp in range(11):
		cm=cs.lobby[lp]
		if cm=="-":continue
		icm=int(cm)
		occ=cs.h[icm]+cs.h[icm+4]
		if any(occ.count(mob) for mob in "0123" if mob!=cm):
			# ~ print(f"skipping trying to move mob {cm} cos home is composed of {occ}")
			# ~ input()
			continue
		hp=2+2*icm
		la,lb=lp,hp
		clp=lp
		if la>lb:
			la,lb=lb,la
		if any (cs.lobby[w]!="-" for w in range(la+1,lb)):
			# ~ print(f"skipping trying to move mob {cm} cos path occupied hp {hp} clp {clp}")
			# ~ input()
			continue
		if occ=="--":
			# ~ move to bottom
			ns=cs.copy()
			ns.h=cs.h[:icm+4]+cm+cs.h[icm+5:]
			ns.lobby=cs.lobby[:lp]+"-"+cs.lobby[lp+1:]
			ns.e+=(abs(hp-clp)+2)*10**icm
			todo.append(ns)
			# ~ print (f"moved {cm} to bottom occ: {occ} home e:{(abs(hp-clp)+2)*10**icm}")
			# ~ print(ns.rep())
			# ~ input()
		else:
			ns=cs.copy()
			ns.h=cs.h[:icm]+cm+cs.h[icm+1:]
			ns.lobby=cs.lobby[:lp]+"-"+cs.lobby[lp+1:]
			ns.e+=(abs(hp-clp)+1)*10**icm
			todo.append(ns)
			# ~ print (f"moved {cm} to top occ {occ} home e:{(abs(hp-clp)+1)*10**icm}")
			# ~ print(ns.rep())
			# ~ input()
	visited[cs.rep()[0]]=cs.e
	done+=1
repres(1,rec)
