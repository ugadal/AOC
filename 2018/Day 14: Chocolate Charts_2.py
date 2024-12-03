#!/usr/bin/env python
# -*- coding: utf-8 -*-
mykey="864801"
# ~ mykey="59414"
# ~ mykey="236021"
mkl=len(mykey)
mykey=list(mykey)
recdone=0
class recipe():
	def __init__(self,v):
		global recdone
		recdone+=1
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
while len(G)<mkl+1:
	nr=str(ea.v+eb.v)
	for c in list(nr):
		G.append(recipe(int(c)))
		lr(G[-2],G[-1])
	for t in range(1+ea.v):ea=ea.next
	for t in range(1+eb.v):eb=eb.next
p=G[-1]
lasts=[]
while len(lasts)<=mkl:
	lasts.append(p.v)
	p=p.prev
lasts.reverse()
print(lasts)
while True:
	testa=all(a==int(b) for a,b in zip(lasts,mykey))
	testb=all(a==int(b) for a,b in zip(lasts[1:],mykey))
	if any((testa,testb)):
		print(recdone-mkl-1,testa,recdone-mkl,testb)
		exit()
	nr=str(ea.v+eb.v)
	for c in list(nr):
		G.append(recipe(int(c)))
		lr(G[-2],G[-1])
		lasts.pop(0)
		lasts.append(G[-1].v)
	for t in range(1+ea.v):ea=ea.next
	for t in range(1+eb.v):eb=eb.next
# ~ 20279773 wrong
# ~ 20279772 okay
