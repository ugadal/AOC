#!/usr/bin/env python
# -*- coding: utf-8 -*-
inf=open("d20.txt").read().splitlines()
# ~ p=<-11104,1791,5208>, v=<-6,36,-84>, a=<19,-5,-4>
P=[]
class particle():
	def __init__(self,line):
		p,v,d=line.split(", ")
		self.x,self.y,self.z=map(int,p[3:-1].split(","))
		self.vx,self.vy,self.vz=map(int,v[3:-1].split(","))
		self.dx,self.dy,self.dz=map(int,d[3:-1].split(","))
		self.dist=sum(map(abs,[self.x,self.y,self.z]))
		self.dd=0
		self.speed=0
	def move(self):
		self.vx+=self.dx
		self.vy+=self.dy
		self.vz+=self.dz
		self.x+=self.vx
		self.y+=self.vy
		self.z+=self.vz
		ndist=sum(map(abs,[self.x,self.y,self.z]))
		self.dd=ndist-self.dist
		self.dist=ndist
		self.speed=sum(map(abs,[self.vx,self.vy,self.vz]))
	def rep(self,i):
		print(f"particle {i} {self.dist} {self.x},{self.y},{self.z}")
# ~ P=[particle(line) for line in inf[:96]]
P=[particle(line) for line in inf]
step=0
while True:
	step+=1
	for p in P:p.move()
	spots=[(p.x,p.y,p.z) for p in P]
	if len(set(spots))!=len(spots):
		print(f"collision {step}")
		toremove=[]
		for spot in (spot for spot in set(spots) if spots.count(spot)>1):
			print(spot)
			toremove.extend([pos for pos,part in enumerate(spots) if part==spot])
			# ~ print(toremove)
		toremove.sort()
		toremove.reverse()
		print(toremove)
		for p in toremove:P.pop(p)
		# ~ input(f"cleanup, remains {len(P)}")
		print(f"cleanup, remains {len(P)}")
