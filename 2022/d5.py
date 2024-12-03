#!/usr/bin/env python
# -*- coding: utf-8 -*-
blocks,instructions=open("d5.txt").read().split("\n\n")
blocks=[[c for c in block]for block in blocks.splitlines()]
for l in blocks:print(l)
blocks=list(zip(*blocks))
NL=len(blocks)
blocks=[list("".join(reversed(block[:-1])).strip()) for i,block in enumerate(blocks) if i%4==1]
for b in blocks:print(b)
# ~ print(instructions)
for l in instructions.splitlines():
	# ~ move 6 from 9 to 3
	print(l)
	print(l.split())
	_,c,_,fp,_,tp= l.split()
	c,fp,tp=map(int,(c,fp,tp))
	blocks[tp-1].extend(reversed(blocks[fp-1][-c:]))
	for b in blocks:print(b)
	input()
