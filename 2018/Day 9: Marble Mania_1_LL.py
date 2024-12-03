#!/usr/bin/env python
# -*- coding: utf-8 -*-
fn="d9.txt"
# ~ 9 players; last marble is worth 25 points: high score is 32
inp=open(fn).read().splitlines()
def pgen(n):
	PL=range(1,n+1)
	while True:
		for p in PL:yield p
class marble():
	def __init__(self,v):
		self.prev=None
		self.next=None
		self.v=v


for l in inp:
	l=l.split(":")[0]
	nbp=int(l.split()[0])
	pg=pgen(nbp)
	nballs=int(l.split()[-2])
	cp=marble(0)
	cp.prev=cp
	cp.next=cp
	fstm=cp
	player=next(pg)
	D={p:0 for p in range(1,nbp+1)}
	nxb=1
	for x in range(100*nballs):
	# ~ for x in range(25):
		if nxb%23:
			l=cp.next
			r=l.next
			cp=marble(nxb)
			l.next=cp
			cp.prev=l
			cp.next=r
			r.prev=cp
		else:
			todel=cp
			for x in range(7):todel=todel.prev
			l=todel.prev
			r=todel.next
			l.next=r
			r.prev=l
			D[player]+=nxb
			D[player]+=todel.v
			cp=r
		nxb+=1
		player=next(pg)
	print(max(D.values()))
