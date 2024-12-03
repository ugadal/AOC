#!/usr/bin/env python
# -*- coding: utf-8 -*-
line=open("d5.txt").readline().strip()
print(f"original length {len(line)}")
def treat(line):
	pos=0
	lp=len(line)
	while pos!=lp-1:
		a=line[pos]
		b=line[pos+1]
		if a!=b and a.upper()==b.upper():
			line=line[:pos]+line[pos+2:]
			pos-=2
			lp-=2
		pos+=1
		pos=max(pos,0)
	# ~ print(f"final length {len(line)}")
	return len(line)
	
print(treat(line))
symbols=set(line.lower())
for s in symbols:
	t=line.replace(s,'')
	s=s.upper()
	t=t.replace(s,'')
	print(s,treat(t))
