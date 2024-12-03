#!/usr/bin/env python
# -*- coding: utf-8 -*-

P=list("abcdefghijklmnop")
for inst in open('d16.txt').readline().split(","):
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
print("".join(P))
