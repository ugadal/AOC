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
	cat,cont=r.findall(line)[0]
	k=Bags[cat]=set()
	for p in cont.split(", "):
		if sub.match(p):
			amount,nat=sub.findall(p)[0]
			k.add(nat)
ab=set(Bags.keys())
OK=set(k for k,v in Bags.items() if "shiny gold" in v)
lastok=set()
while lastok!=OK:
	lastok=set(OK)
	OK=OK|set(k for k,v in Bags.items() if v&OK)
print("p1:",len(OK))
# ~ p2
class bag:
	pool={}
	def __init__(self,name):
		self.name=name
		self.sons=[]
		bag.pool[name]=self
	def size(self):
		v=1+sum(v*k.size() for k,v in self.sons)
		return v
for n in ab:bag(n)
for line in data:
	cat,cont=r.findall(line)[0]
	b=bag.pool[cat]
	for p in cont.split(", "):
		if sub.match(p):
			amount,nat=sub.findall(p)[0]
			b.sons.append((bag.pool[nat],int(amount)))
b=bag.pool["shiny gold"]
print("p2:",b.size()-1)
