#!/usr/bin/env python
# -*- coding: utf-8 -*-
D={}
inst=open("d18.txt").read().split("\n\n")[1].splitlines()
print(inst)
# ~ pos=0
# ~ def myint(s):
	# ~ r=1
	# ~ if s.startswith("-"):
		# ~ r=-1
		# ~ s=s[1:]
	# ~ if s.isdigit():return r*int(s)
	# ~ return D.get(s,0)
# ~ print("part2")
class prog():
	def __init__(self,pid):
		self.other=self
		self.reg={}
		self.pid=pid
		self.reg["p"]=pid
		self.queue=[]
		self.pos=0
		self.done=0
	def rep(self):
		print(f"pid {self.pid} rec {self.done} reg {self.reg} queue {self.queue} pos {self.pos}")
	def myint(self,s):
		r=1
		if s.startswith("-"):
			r=-1
			s=s[1:]
		if s.isdigit(): return r*int(s)
		return self.reg.get(s,0)
	def step(self):
		ti=inst[self.pos]
		print(f"prog {self.reg["p"]} on inst {ti}")
		match ti.split():
			case ["set",*arg]:
				t,v=arg
				v=self.myint(v)
				self.reg[t]=v
				self.pos+=1
			case ["add",*arg]:
				t,v=arg
				v=self.myint(v)
				self.reg[t]+=v
				self.pos+=1
			case ["mul",*arg]:
				targ,v=arg
				t=self.myint(targ)
				v=self.myint(v)
				self.reg[targ]=t*v
				self.pos+=1
			case ["mod",*arg]:
				t,v=arg
				v=self.myint(v)
				self.reg[t]%=v
				self.pos+=1
			case ["jgz",*arg]:
				t,v=arg
				t=self.myint(t)
				v=self.myint(v)
				if t>0:self.pos+=v
				else:self.pos+=1
			case ["snd",*arg]:
				print(arg)
				v=arg[0]
				v=self.myint(v)
				self.other.queue.append(v)
				self.pos+=1
				self.done+=1
			case ["rcv",*arg]:
				if not self.queue: return False
				print(arg)
				t=arg[0]
				v=self.queue.pop(0)
				self.reg[t]=v
				self.pos+=1
		return True



pa=prog(0)
pb=prog(1)
pa.other=pb
pb.other=pa
pa.rep()
pb.rep()
go=True
while go:
	go=False
	while pa.step():
		pa.rep()
		pb.rep()
		go=True
	while pb.step():
		pa.rep()
		pb.rep()
		go=True
print(pb.done)
