#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
fe="exp19.txt"
fr="d19.txt"
import re
mre=re.compile("[<>]")
from copy import deepcopy as dc
global F
F={}
def R(gift):
	print("rule : R",gift)
	return 0
def A(gift):
	print("rule : A",gift)
	r=1
	for (a,b) in gift.values():
		r*=b-a
	return r
F["R"]=R
F["A"]=A
def newgen(rulestring):
	name,rule=rulestring.split("{")
	rule=rule[:-1]
	rulesparts=rule.split(",")
	def fun(gift):
		print("rule : ",name,gift)
		final=rulesparts[-1]
		V=[]
		for rule in rulesparts[:-1]:
			cond,target=rule.split(":")
			op=mre.search(cond).group()
			att,val=mre.split(cond)
			val=int(val)
			c=val
			(g,d)=gift[att]
			match op:
				case '<':
					if val>=d:
						V.append(F[target](gift))
					elif val<=g:continue
					else:
						ggift=dc(gift)
						ggift[att]=(g,c)
						V.append(F[target](ggift))
						gift[att]=(c,d)
				case '>':
					if val<=g:
						V.append(F[target](gift))
					elif val>=d:continue
					else:
						dgift=dc(gift)
						dgift[att]=(c+1,d)
						V.append(F[target](dgift))
						gift[att]=(g,c+1)
			V.append(F[final](gift))
		return (sum(V))		
	F[name]=fun
class problem():
	def __init__(self,fn):
		rules,gifts=open(fn).read().split("\n\n")
		for rule in rules.splitlines():newgen(rule)
		# ~ G=[]
		# ~ for gift in gifts.splitlines():
			# ~ to={}
			# ~ xmas=[x.split("=") for x in gift[1:-1].split(",")]
			# ~ for (k,v) in xmas:to[k]=int(v)
			# ~ G.append(to)
		# ~ self.G=G
		# ~ self.start=F["in"]
	def go(self):
		ttl=0
		for gift in self.G:
			ttl+=self.start(gift)
		print(ttl)
# ~ fun_gen("px{a<2006:qkq,m>2090:A,rfg}")
# ~ P=problem(fr)
# ~ in{s<1351:A,R}
# ~ newgen("in{s<100:A,b}")
# ~ newgen("b{s>200:A,c}")
# ~ newgen("c{t>500:R,A}")
P=problem(fe)
# ~ print(F)
# ~ v=F["in"]({"s":(90,210), "t":(400,600)})
v=F["in"]({"x":(1,4001), "m":(1,4001),"a":(1,4001),"s":(1,4001)})
print(v)
print(167409079868000)
print(v-167409079868000)
# ~ P.go()
