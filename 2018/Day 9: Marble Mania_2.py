#!/usr/bin/env python
# -*- coding: utf-8 -*-
fn="d9.txt"
# ~ 9 players; last marble is worth 25 points: high score is 32
inp=open(fn).read().splitlines()
def pgen(n):
	PL=range(1,n+1)
	while True:
		for p in PL:yield p
for l in inp:
	print(l)
	l=l.split(":")[0]
	print(l)
	nbp=int(l.split()[0])
	pg=pgen(nbp)
	nballs=int(l.split()[-2])
	circle=[0]
	nxb=1
	player=next(pg)
	D={p:0 for p in range(1,nbp+1)}
	cp=0
	for x in range(100*nballs):
		lc=len(circle)
		if nxb%23:
			rp=(cp+1)%lc
			ip=(cp+2)%lc
			if ip<=rp:
				circle.append(nxb)
				cp=lc
			else:
				circle.insert(ip,nxb)
				cp=ip
		else:
			D[player]+=nxb
			dp=(cp+lc-7)%lc
			D[player]+=circle.pop(dp)
			cp=dp
			# ~ print("===",max(D.values()))
		nxb+=1
		player=next(pg)
	print(max(D.values()))
