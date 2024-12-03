#!/usr/bin/env python
# -*- coding: utf-8 -*-
class computer():
	def __init__(self,line):
		self.OV={}
		if isinstance(line,str):
			TV=line.split(",")
			for p,v in enumerate(TV):
				self.OV[p]=int(v)
		else:
			for p,v in enumerate(line):
				self.OV[p]=v
		self.pos=0
		self.inp=[]
		self.flow=self.run()
		self.rb=0
	def fix(self,i,v):
		# ~ 0 indirect
		# ~ 1 direct
		# ~ 2 relative
		if i==0:return self.OV.get(v,0)
		if i==1:return v
		# ~ if i==2:return self.rb+self.OV[v]
		if i==2:return self.OV[v+self.rb]
		# ~ if i==2:return self.rb+v
	def fix3(self,i,v):
		# ~ 0 direct
		# ~ 1 direct
		# ~ 2 relative
		if i==0:return v
		if i==1:return v
		if i==2:return self.rb+v
		
	def run(self):
		while True:
			cmd=str(self.OV[self.pos]).zfill(5)
			opcode=int(cmd[-2:])
			ic,ib,ia=map(int,cmd[:3])
			match opcode:
				case 1:
					pa,pb,pc=self.OV[self.pos+1],self.OV[self.pos+2],self.OV[self.pos+3]
					s=self.fix(ia,pa) + self.fix(ib,pb)
					pc=self.fix3(ic,pc)
					self.OV[pc]=s
					if pc!=self.pos:self.pos+=4
				case 2:
					pa,pb,pc=self.OV[self.pos+1],self.OV[self.pos+2],self.OV[self.pos+3]
					s=self.fix(ia,pa) * self.fix(ib,pb)
					pc=self.fix3(ic,pc)
					self.OV[pc]=s
					if pc!=self.pos:self.pos+=4
				case 3:
					pa=self.OV[self.pos+1]
					pa=self.fix3(ia,pa)
					# ~ pa=self.fix(ia,pa)
					self.OV[pa]=self.inp.pop(0)
					if pa!=self.pos:self.pos+=2
				case 4:
					pa=self.OV[self.pos+1]
					pa=self.fix(ia,pa) 
					yield pa
					self.pos+=2
				case 5:
					pa=self.OV[self.pos+1]
					pa=self.fix(ia,pa)
					if pa:
						pb=self.OV[self.pos+2]
						pb=self.fix(ib,pb)
						self.pos=pb
					else:self.pos+=3
				case 6:
					pa=self.OV[self.pos+1]
					pa=self.fix(ia,pa)
					if not pa:
						pb=self.OV[self.pos+2]
						pb=self.fix(ib,pb)
						self.pos=pb
					else:self.pos+=3
				case 7:
					pa=self.OV[self.pos+1]
					pb=self.OV[self.pos+2]
					pc=self.OV[self.pos+3]
					pa=self.fix(ia,pa)
					pb=self.fix(ib,pb)
					pc=self.fix3(ic,pc)
					if pa<pb:self.OV[pc]=1
					else:self.OV[pc]=0
					if pc!=self.pos:self.pos+=4
				case 8:
					pa=self.OV[self.pos+1]
					pb=self.OV[self.pos+2]
					pc=self.OV[self.pos+3]
					pa=self.fix(ia,pa)
					pb=self.fix(ib,pb)
					pc=self.fix3(ic,pc)
					if pa==pb:self.OV[pc]=1
					else:self.OV[pc]=0
					if pc!=self.pos:self.pos+=4
				case 9:
					pa=self.OV[self.pos+1]
					# ~ pa=self.fix(ia,pa)
					self.rb+=pa
					self.pos+=2
				case 99:
					print (self.OV.values())
					yield self.OV[0]
					return
# ~ c=computer((1,9,10,3,2,3,11,0,99,30,40,50))
# ~ assert(next(c.flow)==3500)
c=computer((3,0,4,0,99))
c.inp.append(3145)
print(next(c.flow))
