#!/usr/bin/env python
# -*- coding: utf-8 -*-
fn="d10.txt"
# ~ position=<-51522, -51540> velocity=< 5,  5>
class star():
	def __init__(self,defline):
		P=defline.split("<")
		self.x=int(P[1].split(",")[0])
		self.dx=int(P[2].split(",")[0])
		P=defline.split(">")
		self.y=int(P[0].split(",")[1])
		self.dy=int(P[1].split(",")[1])
	def mv(self):
		self.x+=self.dx
		self.y+=self.dy

G=[star(dl) for dl in open(fn).read().splitlines()]
nbs=len(G)
cyc=0
for x in range(10333):
	mx=sum(s.x for s in G)/nbs
	my=sum(s.y for s in G)/nbs
	mix=min(s.x for s in G)
	miy=min(s.x for s in G)
	maxx=max(s.x for s in G)
	maxy=max(s.x for s in G)
	print(cyc,mx,my,maxx-mix,maxy-miy)
	for s in G:s.mv()
	cyc+=1
while True:
	print(cyc,"="*80)
	mix=min(s.x for s in G)
	miy=min(s.x for s in G)
	maxx=max(s.x for s in G)
	maxy=max(s.x for s in G)
	M=set((s.y,s.x) for s in G)
	for row in range(miy,maxy+1):
		r=[]
		for col in range(mix,maxx+1):
			if (row,col) in M:r.append("#")
			else:r.append(" ")
		print("".join(r))
	input()
	for s in G:s.mv()
	cyc+=1
