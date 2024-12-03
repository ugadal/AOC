#!/usr/bin/env python
# -*- coding: utf-8 -*-
fn,part="d24.txt",1
import sys
from heapq import heappush, heappop
try:
	part=int(sys.argv[1])
	boost=int(sys.argv[2])
except:
	part=0
	boost=0
class grp():
	def __init__(self,line,cgt,number):
		# ~ print(line)
		self.gt=cgt
		lp,rp=line.split(" units each with ")
		self.nbunits=int(lp)
		self.nb=number+1
		self.hp=int(rp.split()[0])
		lp,rp=rp.split("with an attack that does ")
		dmg,self.dmgt=rp.split()[:2]
		self.dmg=int(dmg)
		self.initiative=int(rp.split("at initiative ")[1])
		self.immunity=[]
		self.weakness=[]
		if line.count("("):
			info=line.split("(")[1]
			info=info.split(")")[0]
			if info.count(";"):
				parts=info.split("; ")
			else:parts=[info]
			for part in parts:
				lp,rp=part.split(" to ")
				target=self.immunity if lp=="immune" else self.weakness
				if rp.count(","):
					matters=rp.split(", ")
					target.extend(matters)
				else:target.append(rp)
		if self.gt=="Immune System":
			self.dmg+=boost
	def __str__(self):
		return f"{self.gt} {self.nb} init:{self.initiative} of {self.nbunits} units at {self.hp} HP, AP:{self.dmg} {self.dmgt}, weakness {self.weakness} immune {self.immunity}, {self.EP()}"
	def sh(self):
		return f"{self.gt} {self.nb}"
	def EP(self):
		return self.nbunits*self.dmg
lines=open(fn).read().split("#\n")[part].splitlines()
G={}
for line in lines:
	if line.endswith(":"):
		cgt=line[:-1]
		G[cgt]=[]
		target=G[cgt]
		continue
	if line=="":continue
	target.append(grp(line,cgt,len(target)))
allgrp=[]
for g in G.values():allgrp.extend(g)
while True:
	for g in allgrp:g.targeted=False
	for faction in G.keys():
		print()
		print(faction,'targeting')
		print("=============================")
		fighters=[]
		for g in allgrp:
			if g.gt!=faction:continue
			if not g.nbunits:continue
			heappush(fighters,(-g.EP(),-g.initiative,g))
		for ep,ini,g in fighters:g.target=None
		print(faction,"unordered fighters")
		for ep,ini,g in fighters:print(-ep,-ini,g.sh())
		while fighters:
			ep,ini,g=heappop(fighters)
			print(g.sh(),"targeting")
			targets=[]
			for t in allgrp:
				if t.gt==faction:continue
				if not t.nbunits:continue
				if t.targeted:continue
				ep=g.EP()
				if g.dmgt in t.weakness:ep*=2
				elif g.dmgt in t.immunity:ep=0
				# ~ next step may sound stupid but is required
				# ~ sometimes an ennemy is picked while not damaged preventing
				# ~ next figther from effectively  damaging
				if ep==0:continue
				heappush(targets,(-ep,-t.EP(),-t.initiative,t))
			print("unordered opponents")
			for ep,tep,tini,t in targets:print(-ep,-tep,-tini,t.sh())
			if targets:
				ep,tep,tini,target=heappop(targets)
				target.targeted=True
				g.target=target
				print("targeting",target.sh(),-ep,"damage")
	print()
	print("attacks")
	print()
	attackorder=[]
	for g in allgrp:
		if not g.nbunits:continue
		if not g.target:continue
		heappush(attackorder,(-g.initiative,g))
	while attackorder:
		ini,att = heappop(attackorder)
		if not att.nbunits:
			print("attackant died in between")
			# ~ input()
			continue
		t=att.target
		if not t.nbunits:
			print("target died in between, this is impossible")
			exit()
			continue
		print(att.sh(),"attacks",t.sh())
		ep=att.EP()
		if att.dmgt in t.weakness:ep*=2
		elif att.dmgt in t.immunity:ep=0
		killed=min(t.nbunits,ep//t.hp)
		print("killing",killed)
		t.nbunits-=killed
	z=1
	for k,v in G.items():
		ts=sum(p.nbunits for p in v)
		z*=ts
		print(k,ts)
	if not z:break
# ~ 6590
# ~ <7696
