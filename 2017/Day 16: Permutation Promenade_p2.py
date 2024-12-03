#!/usr/bin/env python
# -*- coding: utf-8 -*-

P=list("abcdefghijklmnop")
todo=open('d16.txt').readline().split(",")
seen=set()
seen.add("abcdefghijklmnop")
run=0
for run in range(1000000000):
	# ~ print(run,len(seen))
	for inst in todo:
		match list(inst):
			case ["s",*arg]:
				k=int(inst[1:])
				P=P[-k:]+P[:16-k]
			case ["x",*arg]:
				a,b=map(int,(inst[1:].split("/")))
				P[a],P[b]=P[b],P[a]
			case ["p",*arg]:
				a,b=inst.strip()[1:].split("/")
				a=P.index(a)
				b=P.index(b)
				P[a],P[b]=P[b],P[a]
	t="".join(P)
	if t in seen: print(run+1,t)
	seen.add(t)
	
# ~ cycle de 60, prendre le 40ème cad 1000000000%60
	
