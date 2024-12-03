#!/usr/bin/env python
# -*- coding: utf-8 -*-

def rec(s):
	nc=0
	lvl=0
	pos=0
	garbage=False
	while pos<len(s):
		c=s[pos]
		if c=='{' and not garbage:
			lvl+=1
			pos+=1
			continue
		if c=='}' and not garbage:
			yield lvl
			lvl-=1
			pos+=1
			continue
		if c=="<" and not garbage:
			garbage=True
			pos+=1
			continue
		if c==">" and garbage:
			garbage=False
			pos+=1
			continue
		if c=="!" :
			pos+=2
			continue
		pos+=1
		if garbage:nc+=1
	print(f"=== {nc} ===")
# ~ for line in open("d9.txt").read().splitlines()[1:]:
	# ~ t=line.split()[0][:-1]	
	# ~ print(t)
	# ~ print(sum(v for v in rec(t)))
line=open("d9.txt").read().splitlines()[0]
print(sum(v for v in rec(line)))
