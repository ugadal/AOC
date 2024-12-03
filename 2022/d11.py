#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tqdm import trange
from collections import deque
exp="""Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1"""
DM={}
globmod=1
class monkey():
	def __init__(self,block):
		Lines=block.splitlines()
		self.n=int(Lines[0].split()[1].split(":")[0])
		self.obj=deque(map(int,Lines[1].split(":")[1].split(",")))
		self.op=Lines[2].split("=")[1]
		self.mod=int(Lines[3].split("by")[1])
		self.targok=int(Lines[4].split("monkey")[1])
		self.targfalse=int(Lines[5].split("monkey")[1])
		self.inspected=0
		DM[self.n]=self
	def throw(self):
		for obj in self.obj:
			self.inspected+=1
			old=obj
			new=eval(self.op)%globmod
			# ~ new=new%globmod
			if new%self.mod:DM.get(self.targfalse).obj.append(new)
			else:DM.get(self.targok).obj.append(new)
		self.obj.clear()
# ~ for block in exp.split("\n\n"):monkey(block)	
for block in open("d11.txt").read().split("\n\n"):monkey(block)
Monkeys=list(DM.values())
for monk in Monkeys:globmod*=monk.mod
for xx in trange(10000):
	for monk in Monkeys:
		monk.throw()

for monk in Monkeys:
	print(monk.n,monk.inspected)
a,b=sorted([monk.inspected for monk in Monkeys])[-2:]
print(a*b)
