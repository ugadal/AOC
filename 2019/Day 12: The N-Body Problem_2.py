#!/usr/bin/env python
# -*- coding: utf-8 -*-
fn,part="d12.txt",3
sep="\n\n"
data=open(fn).read().split(sep)[part].splitlines()
class moon():
	def __init__(self,line):
		print("initing moon",line)
		P=line[1:-1].split(", ")
		P=[p.split("=")[1] for p in P]
		P=list(map(int,P))
		self.x,self.y,self.z=P
		self.dx=0
		self.dy=0
		self.dz=0
		self.E=0
	def __str__(self):
		return f"{self.x},{self.y},{self.z},'==',{self.dx},{self.dy},{self.dz} [{self.E}]"
	def move(self):
		self.x+=self.dx
		self.y+=self.dy
		self.z+=self.dz
		self.energ()
	def energ(self):
		pot=abs(self.x)+abs(self.y)+abs(self.z)
		kin=abs(self.dx)+abs(self.dy)+abs(self.dz)
		self.E=pot*kin
Moons=[moon(line) for line in data]
cyc=0
# ~ V={}
# ~ hashmoons="".join([m.__str__() for m in Moons])
# ~ tte=sum(m.E for m in Moons)
# ~ V[tte]=[hashmoons]
moona=Moons[0]
V=[moona.__str__()]
pcyc=0
while True:
	cyc+=1
	for pa,ma in enumerate(Moons[:-1]):
		for mb in Moons[pa+1:]:
			if ma.x<mb.x:
				ma.dx+=1
				mb.dx-=1
			elif ma.x>mb.x:
				ma.dx-=1
				mb.dx+=1
			if ma.y<mb.y:
				ma.dy+=1
				mb.dy-=1
			elif ma.y>mb.y:
				ma.dy-=1
				mb.dy+=1
			if ma.z<mb.z:
				ma.dz+=1
				mb.dz-=1
			elif ma.z>mb.z:
				ma.dz-=1
				mb.dz+=1
	# ~ for moon in Moons:print(moon)
	for moon in Moons:moon.move()
	if moona.E==0:
		print(cyc,cyc-pcyc)
		pcyc=cyc
		# ~ exit()
# ~ for moon in Moons:print(moon)
	# ~ tte=sum(m.E for m in Moons)
	# ~ if cyc%100000==0:print(cyc,tte)
	# ~ print(cyc,tte)
	# ~ if tte not in V:V[tte]=[]
	# ~ else:print("known energy")
	# ~ hashmoons="".join([m.__str__() for m in Moons])
	# ~ if hashmoons in V[tte]:
		# ~ print(cyc)
		# ~ for moon in Moons:print(moon)
		# ~ exit()
	# ~ V[tte].append(hashmoons)
	# ~ scm=moona.__str__()
	# ~ if scm in V:
		# ~ print(scm,cyc,V.index(scm))
		# ~ exit()
	# ~ else:V.append(scm)
	# ~ print(len(V))
