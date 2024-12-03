#!/usr/bin/env python
# -*- coding: utf-8 -*-
inf=open("d21.txt").read().split("\n\n")[1].splitlines()
from mylib import flip,transpose,mirror
S=set()
Rules={}
def pl(L):
	for row in L:print(row)
def asS(L):return "/".join(["".join([str(x) for x in l ]) for l in L])
def flip(L):return tuple(row[::-1] for row in L)
def trans(L):return tuple(zip(*L))
for ruledef in inf:
	rule,result=ruledef.split(" => ")
	rule=tuple(tuple(s) for s in rule.split("/"))
	result=tuple(tuple(s) for s in result.split("/"))
	Rules[rule]=result
	for x in range(4):
		rule=flip(rule)
		Rules[rule]=result
		rule=trans(rule)
		Rules[rule]=result
def sub(G):
	# ~ print(f"G is {G}")
	l=len(G[0])
	if l%2==0:step=2
	else:step=3
	parts=l//step
	print(f"split in {step}x{step} to {step+1}x{step+1} corresponding")
	newG=[]
	for x in range(parts*(step+1)):newG.append([0]*(step+1)*parts)
	for br in range(0,parts):
		for bc in range(0,parts):
			source=tuple(G[step*br+dr][step*bc:step*bc+step] for dr in range(step))
			target=Rules[source]
			for nr,targetrow in zip(range(step+1),target):
				for nc,symbol in zip (range(step+1),targetrow):
					newG[br*(step+1)+nr][bc*(step+1)+nc]=symbol
	return tuple(tuple(row) for row in newG)
start=".#./..#/###"
start=tuple(tuple(s) for s in start.split("/"))
for x in range(5):
	start=sub(start)
	for row in start:print("".join(row))
	print(sum([row.count("#") for row in start]))
input()
for x in range(13):
	start=sub(start)
	for row in start:print("".join(row))
	print(sum([row.count("#") for row in start]))
