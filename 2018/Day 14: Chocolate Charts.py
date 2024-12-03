#!/usr/bin/env python
# -*- coding: utf-8 -*-
mykey=864801
# ~ mykey=2018
class recipe():
	def __init__(self,v):
		self.v=v
		self.prev=None
		self.next=None
def lr(a,b):
	a.next=b
	b.prev=a
	b.next=first
G=[recipe(3),recipe(7)]
first,last=G
lr(first,last)
ea,eb=first,last
while len(G)<10+mykey:
	nr=str(ea.v+eb.v)
	for c in list(nr):
		G.append(recipe(int(c)))
		lr(G[-2],G[-1])
	for t in range(1+ea.v):ea=ea.next
	for t in range(1+eb.v):eb=eb.next
	# ~ print(ea.v,eb.v)
p=first
for t in range(mykey):p=p.next
for t in range(10):
	print(p.v,end="")
	p=p.next
print()
