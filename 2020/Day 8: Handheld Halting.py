#!/usr/bin/env python
# -*- coding: utf-8 -*-
fn,part="d8.txt",1
data=open(fn).read().split("\n\n")[part].splitlines()
import re
r=re.compile(r"^(.*) ([+-]\d+)$")
pgm=[r.findall(line).pop() for line in data]
class simc:
	def __init__(self,pgm):
		self.pos=0
		self.acc=0
		self.pgm=[[a,int(b)] for a,b in pgm]
		self.exit=len(self.pgm)
	def run(self):
		print("running")
		self.pos=0
		self.acc=0
		visited=set()
		while self.pos not in visited:
			if self.pos==self.exit:return True
			print("current pos",self.pos,self.acc,visited)
			inst,v=self.pgm[self.pos]
			print(inst,v)
			visited.add(self.pos)
			self.pos+=1
			match inst:
				case "nop": pass
				case "acc":
					self.acc+=v
				case "jmp":
					self.pos+=v-1
		print("leaving in pos:",self.pos,self.acc,visited)
		return False
	def runmut(self,mutpos):
		if self.pgm[mutpos][0]=="acc":return False
		self.pos=0
		self.acc=0
		visited=set()
		while self.pos not in visited:
			if self.pos==self.exit:
				print("exiting acc:",self.acc)
				exit()
			# ~ print("current pos",self.pos,self.acc,visited)
			inst,v=self.pgm[self.pos]
			# ~ print(inst,v)
			visited.add(self.pos)
			if self.pos==mutpos:
				match inst:
					case "nop":
						self.pos+=v
						continue
					case "jmp":
						self.pos+=1
						continue
			self.pos+=1
			match inst:
				case "nop": pass
				case "acc":
					self.acc+=v
				case "jmp":
					self.pos+=v-1
		print("leaving in pos:",self.pos,self.acc)
		return False
ts=simc(pgm)
print(ts.run())
for x in range(ts.exit):
	print (x,ts.runmut(x))
