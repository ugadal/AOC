#!/usr/bin/env python
# -*- coding: utf-8 -*-
fn="d13.txt"
G=[]
for line in open(fn).read().split("\n\n")[2].splitlines():
	G.append(list(line))
NR=len(G)
NC=max(len(row) for row in G)
print("dims",NR,NC)
east=1
north=-1j
west=-1
south=1j
def left(d):return (-1j)*d
def right(d):return d*1j
def straight(d):return d
def decision():
	while True:
		for d in (left,straight,right):yield d
Carts=[]
class cart():
	def __init__(self,row,col,pointing):
		self.pos=col+row*1j
		self.pointing=pointing
		self.rot=decision()
		self.killed=False
	def queuepos(self):
		return self.row*NC+self.col
for ir,row in enumerate(G):
	for ic,char in enumerate(row):
		match char:
			case '/':continue
			case '\\':continue
			case ' ':continue
			case '+':continue
			case ">":
				Carts.append(cart(ir,ic,east))
				G[ir][ic]="-"
			case "<":
				Carts.append(cart(ir,ic,west))
				G[ir][ic]="-"
			case "^":
				Carts.append(cart(ir,ic,north))
				G[ir][ic]="|"
			case "v":
				Carts.append(cart(ir,ic,south))
				G[ir][ic]="|"
slash={east:north,north:east,west:south,south:west}
antislash={east:south,north:west,west:north,south:east}
while True:
	TB=[cart for cart in Carts if not cart.killed]
	TB=list(sorted(Carts,key=lambda c: (c.pos.imag,c.pos.real)))
	for c in TB:
		if c.killed:continue
		print(c.pos.imag,c.pos.real,c.pointing)
		occupied=set(c.pos for c in TB if not c.killed)
		npos=c.pos+c.pointing
		if npos in occupied:
			print("Crash",npos)
			c.killed=True
			hit=next(c for c in TB if c.pos==npos and not c.killed)
			print("hit",hit.pos,hit.pointing)
			hit.killed=True
			continue
		match G[int(npos.imag)][int(npos.real)]:
			case "+":c.pointing=next(c.rot)(c.pointing)
			case "/":c.pointing=slash[c.pointing]
			case "\\" :c.pointing=antislash[c.pointing]
		c.pos=npos
	TB=[cart for cart in Carts if not cart.killed]
	if len(TB)==1:
		print("the end")
		c=TB.pop()
		print (c.pos,c.pointing)
		exit()
