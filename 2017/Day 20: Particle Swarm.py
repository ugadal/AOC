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
for p in P:p.move()
# ~ while any(p.dd<0 for p in P):
while any(p.dd<0 for p in P):
	print(f"{[p.dd<0 for p in P].count(True)} closing in")
	for p in P:p.move()
# ~ for i,p in enumerate(P):p.rep(i)
while True:
# ~ closest
	closest=min(range(len(P)), key=lambda i:P[i].dist)
	print(closest)
	slowest=min(range(len(P)), key=lambda i:P[i].speed)
	print(slowest)
	for p in P:p.move()
	# ~ input()
