#!/usr/bin/env python
# -*- coding: utf-8 -*-
fn,part="d7.txt",1
data=open(fn).read().split("\n\n")[part].splitlines()
import re
r=re.compile(r"^(.*) bags contain (.*)\.$")
sub=re.compile(r"(\d+) (.*) bags?")
Bags={}
# ~ p1
for line in data:
	# ~ print(line)
	cat,cont=r.findall(line)[0]
	# ~ print(cat,":",cont)
	k=Bags[cat]=set()
	for p in cont.split(", "):
		if sub.match(p):
			amount,nat=sub.findall(p)[0]
			# ~ print(amount,":",nat)
			k.add(nat)
ab=set(Bags.keys())
OK=set(k for k,v in Bags.items() if "shiny gold" in v)
lastok=set()
while lastok!=OK:
	lastok=set(OK)
	# ~ print(len(OK),OK)
	OK=OK|set(k for k,v in Bags.items() if v&OK)
print(len(OK))
# ~ wtf2
