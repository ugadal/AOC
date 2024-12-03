#!/usr/bin/env python
# -*- coding: utf-8 -*-
fn="d13.txt"
G=[]
for line in open(fn).read().split("\n\n")[2].splitlines():
	G.append(list(line))
NR=len(G)
NC=max(len(row) for row in G)
print("dims",NR,NC)
east=(0,1)
north=(-1,0)
west=(0,-1)
south=(1,0)
def left(d):
	dr,dc=d
	return -dc,dr
def right(d):
	dr,dc=d
	return dc,-dr
def straight(d):return d
def decision():
	while True:
		for d in (left,straight,right):yield d
Carts=[]
class cart():
	def __init__(self,row,col,pointing):
		self.row=row
		self.col=col
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
	TB=list(sorted(Carts,key=lambda c: c.queuepos()))
	for c in TB:
		if c.killed:continue
		print(c.row,c.col,c.pointing)
		occupied=set((c.row,c.col) for c in TB if not c.killed)
		dr,dc=c.pointing
		nr,nc=c.row+dr,c.col+dc
		if (nr,nc) in occupied:	
			print("Crash",nc,nr)
			c.killed=True
			hit=next(c for c in TB if c.row==nr and c.col==nc and not c.killed)
			print("hit",hit.row,hit.col,hit.pointing)
			hit.killed=True
			continue
		match G[nr][nc]:
			case "+":
				c.pointing=next(c.rot)(c.pointing)
			case "/":
				c.pointing=slash[c.pointing]
			case "\\" :
				c.pointing=antislash[c.pointing]
		c.row=nr
		c.col=nc
	TB=[cart for cart in Carts if not cart.killed]
	print("len TB",len(TB))
	if len(TB)==1:
		print("the end")
		c=TB.pop()
		print (c.col,c.row,c.pointing)
		exit()
