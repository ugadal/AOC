#!/usr/bin/env python
# -*- coding: utf-8 -*-
class computer():
	def __init__(self,*args):
		self.OV={}
		if isinstance(args[0],str):
			TV=args[0].split(",")
			for p,v in enumerate(TV):
				self.OV[p]=int(v)
		else:
			for p,v in enumerate(args):	self.OV[p]=v
		self.pos=0
		self.flow=self.run()
		self.inp=[]
	def run(self):
		while True:
			cmd=str(self.OV[self.pos]).zfill(5)
			# ~ print(cmd,self.pos)
			opcode=int(cmd[-2:])
			ic,ib,ia=map(int,cmd[:3])
			# ~ 0 indirect pa=OV[OV[pos]]
			# ~ 1 direct pa=OV[pos]
			match opcode:
				# ~ Parameters that an instruction writes to will 
				# ~ never be in immediate mode
				case 1: #add
					pa,pb,pc=self.OV[self.pos+1],self.OV[self.pos+2],self.OV[self.pos+3]
					if ia==0:pa=self.OV[pa]# ~ s=self.fix(ia,pa) + self.fix(ib,pb)
					if ib==0:pb=self.OV[pb]# ~ s=self.fix(ia,pa) + self.fix(ib,pb)
					s=pa+pb
					self.OV[pc]=s
					self.pos+=4
				case 2: #mult
					pa,pb,pc=self.OV[self.pos+1],self.OV[self.pos+2],self.OV[self.pos+3]
					if ia==0:pa=self.OV[pa]# ~ s=self.fix(ia,pa) + self.fix(ib,pb)
					if ib==0:pb=self.OV[pb]# ~ s=self.fix(ia,pa) + self.fix(ib,pb)
					s=pa*pb
					self.OV[pc]=s
					self.pos+=4
				case 3:
					pa=self.OV[self.pos+1]
					# ~ if ia==0:pa=self.OV[pa]# ~ s=self.fix(ia,pa) + self.fix(ib,pb)
					self.OV[pa]=self.inp.pop(0)
					self.pos+=2
				case 4:
					pa=self.OV[self.pos+1]
					if ia==0:pa=self.OV[pa]# ~ s=self.fix(ia,pa) + self.fix(ib,pb)
					# ~ pa=self.OV[pa]
					# ~ pa=self.fix(ia,pa) 
					yield pa
					self.pos+=2
				case 5: # jump if non zero param1
					pa=self.OV[self.pos+1]
					if ia==0:pa=self.OV[pa]
					if pa:
						pb=self.OV[self.pos+2]
						if ib==0:pb=self.OV[pb]
						self.pos=pb
					else:self.pos+=3
				case 6: # jump if zero param1
					pa=self.OV[self.pos+1]
					if ia==0:pa=self.OV[pa]
					if pa==0:
						pb=self.OV[self.pos+2]
						if ib==0:pb=self.OV[pb]
						self.pos=pb
					else:self.pos+=3
				case 7: #pa lesser pb than
					pa=self.OV[self.pos+1]
					pb=self.OV[self.pos+2]
					pc=self.OV[self.pos+3]
					if ia==0:pa=self.OV[pa]
					if ib==0:pb=self.OV[pb]
					# ~ pc=self.fix3(ic,pc)
					if pa<pb:self.OV[pc]=1
					else:self.OV[pc]=0
					self.pos+=4
					# ~ if pc!=self.pos:self.pos+=4
				case 8:#pa==pb
					pa=self.OV[self.pos+1]
					pb=self.OV[self.pos+2]
					pc=self.OV[self.pos+3]
					if ia==0:pa=self.OV[pa]
					if ib==0:pb=self.OV[pb]
					# ~ pc=self.fix3(ic,pc)
					if pa==pb:self.OV[pc]=1
					else:self.OV[pc]=0
					self.pos+=4
					# ~ if pc!=self.pos:self.pos+=4
				# ~ case 9:
					# ~ pa=self.OV[self.pos+1]
					# ~ pa=self.fix(ia,pa)
					# ~ self.rb+=pa
					# ~ self.pos+=2
				case 99:
					# ~ print (self.OV.values())
					# ~ print("finishing")
					yield self.OV[0]
					return
d=(3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0)
ps=(4,3,2,1,0)
Amps=[computer(*d) for x in range(5)]
for amp,v in zip(Amps,ps):amp.inp.append(v)
prev=0
for amp in Amps:
	amp.inp.append(prev)
	prev=next(amp.flow)
print(prev)
ps=(0,1,2,3,4)
d=(3,23,3,24,1002,24,10,24,1002,23,-1,23,
101,5,23,23,1,24,23,23,4,23,99,0,0)
Amps=[computer(*d) for x in range(5)]
for amp,v in zip(Amps,ps):amp.inp.append(v)
prev=0
for amp in Amps:
	amp.inp.append(prev)
	prev=next(amp.flow)
print(prev)
ps=(1,0,4,3,2)
d=(3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,
1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0)
Amps=[computer(*d) for x in range(5)]
for amp,v in zip(Amps,ps):amp.inp.append(v)
prev=0
for amp in Amps:
	amp.inp.append(prev)
	prev=next(amp.flow)
print(prev)
d=list(map(int,open("d7.txt").readline().strip().split(",")))
import itertools as it
v=list(range(5))
rec=float("-inf")
for p in it.permutations(v):
	Amps=[computer(*d) for x in range(5)]
	prev=0
	for amp,code in zip(Amps,p):
		amp.inp.extend([code,prev])
		prev=next(amp.flow)
	rec=max(rec,prev)
print(rec)
v=list(range(5,10))
rec=float("-inf")
for p in it.permutations(v):
# ~ for p in [[9,7,8,5,6]]:
	Amps=[computer(*d) for x in range(5)]
	for amp,x in zip(Amps,p):amp.inp.append(x)
	prev=0
	while True:
		flag=False
		for amp,code in zip(Amps,p):
			amp.inp.append(prev)
			try:prev=next(amp.flow)
			except:
				flag=True
				break
		rec=max(rec,prev)
		# ~ if prev==rec:print(prev)
		if flag:break
print(rec)
