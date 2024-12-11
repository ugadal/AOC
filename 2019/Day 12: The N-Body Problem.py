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
for x in range(1000):
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
for moon in Moons:print(moon)
print(sum(m.E for m in Moons))
