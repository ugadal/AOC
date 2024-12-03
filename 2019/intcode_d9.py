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
		self.rb=0
	def fixa(self,pos,ia):
		pa=self.OV[pos]
		if ia==0:return self.OV[pa]
		if ia==2:return self.OV[pa-self.rb]
		return pa
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
				case 9:
					pa=self.OV[self.pos+1]
					if ia==0:pa=self.OV[pa]
					if ia==2:pa=self.OV[pa-self.rb]
					assert pa==self.fixa(self.pos+1,ia)
					# ~ pa=self.fix(ia,pa)
					self.rb+=pa
					self.pos+=2
				case 99:
					# ~ print (self.OV.values())
					# ~ print("finishing")
					yield self.OV[0]
					return
d=(109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99)
c=computer(*d)
for v in c.flow:print(v,end=", ")
