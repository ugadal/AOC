#!/usr/bin/env python
# -*- coding: utf-8 -*-
fn="d8.txt"
inp=open(fn)
V=list(map(int,inp.readline().strip().split())) #test data
V=list(map(int,inp.readline().strip().split())) #real data, comment to use test data
class tree():
	def __init__(self,data):
		self.nsons=data.pop(0)
		self.md=data.pop(0)
		self.sons=[tree(data) for n in range(self.nsons)]
		self.mdata=[data.pop(0) for n in range(self.md)]
	def rep(self):
		for k in dir(self):
			if k.startswith('__'):continue
			v=self.__getattribute__(k)
			if type(v)==type(self.rep):continue
			print(k,self.__getattribute__(k))
	def total(self):
		return sum(self.mdata) + sum(son.total() for son in self.sons)

	def get_son(self, son):
		if son < len(self.sons):return self.sons[son].special()
		return 0
	
	def special(self):
		if not self.sons: return sum(self.mdata)
		tt=0
		for idx in self.mdata: tt+=self.get_son(idx - 1) 
		return tt


t=tree(V)
print(t.total())
print(t.special())
