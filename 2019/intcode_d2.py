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
	def run(self):
		while True:
			cmd=str(self.OV[self.pos]).zfill(5)
			# ~ print(cmd,self.pos)
			opcode=int(cmd[-2:])
			# ~ ic,ib,ia=map(int,cmd[:3])
			match opcode:
				case 1:
					pa,pb,pc=self.OV[self.pos+1],self.OV[self.pos+2],self.OV[self.pos+3]
					# ~ s=self.fix(ia,pa) + self.fix(ib,pb)
					# ~ pc=self.fix3(ic,pc)
					pa=self.OV[pa]
					pb=self.OV[pb]
					# ~ pc=self.OV[pc]
					s=pa+pb
					self.OV[pc]=s
					# ~ print("add",self.OV.values())
					# ~ if pc!=self.pos:self.pos+=4
					self.pos+=4
				case 2:
					pa,pb,pc=self.OV[self.pos+1],self.OV[self.pos+2],self.OV[self.pos+3]
					# ~ s=self.fix(ia,pa) * self.fix(ib,pb)
					# ~ pc=self.fix3(ic,pc)
					pa=self.OV[pa]
					pb=self.OV[pb]
					# ~ pc=self.OV[pc]
					s=pa*pb
					self.OV[pc]=s
					# ~ print("mult",self.OV.values())
					# ~ if pc!=self.pos:self.pos+=4
					self.pos+=4
				# ~ case 3:
					# ~ pa=self.OV[self.pos+1]
					# ~ pa=self.fix3(ia,pa)
					# ~ #pa=self.fix(ia,pa)
					# ~ self.OV[pa]=self.inp.pop(0)
					# ~ if pa!=self.pos:self.pos+=2
				# ~ case 4:
					# ~ pa=self.OV[self.pos+1]
					# ~ pa=self.fix(ia,pa) 
					# ~ yield pa
					# ~ self.pos+=2
				# ~ case 5:
					# ~ pa=self.OV[self.pos+1]
					# ~ pa=self.fix(ia,pa)
					# ~ if pa:
						# ~ pb=self.OV[self.pos+2]
						# ~ pb=self.fix(ib,pb)
						# ~ self.pos=pb
					# ~ else:self.pos+=3
				# ~ case 6:
					# ~ pa=self.OV[self.pos+1]
					# ~ pa=self.fix(ia,pa)
					# ~ if not pa:
						# ~ pb=self.OV[self.pos+2]
						# ~ pb=self.fix(ib,pb)
						# ~ self.pos=pb
					# ~ else:self.pos+=3
				# ~ case 7:
					# ~ pa=self.OV[self.pos+1]
					# ~ pb=self.OV[self.pos+2]
					# ~ pc=self.OV[self.pos+3]
					# ~ pa=self.fix(ia,pa)
					# ~ pb=self.fix(ib,pb)
					# ~ pc=self.fix3(ic,pc)
					# ~ if pa<pb:self.OV[pc]=1
					# ~ else:self.OV[pc]=0
					# ~ if pc!=self.pos:self.pos+=4
				# ~ case 8:
					# ~ pa=self.OV[self.pos+1]
					# ~ pb=self.OV[self.pos+2]
					# ~ pc=self.OV[self.pos+3]
					# ~ pa=self.fix(ia,pa)
					# ~ pb=self.fix(ib,pb)
					# ~ pc=self.fix3(ic,pc)
					# ~ if pa==pb:self.OV[pc]=1
					# ~ else:self.OV[pc]=0
					# ~ if pc!=self.pos:self.pos+=4
				# ~ case 9:
					# ~ pa=self.OV[self.pos+1]
					# ~ pa=self.fix(ia,pa)
					# ~ self.rb+=pa
					# ~ self.pos+=2
				case 99:
					# ~ print (self.OV.values())
					yield self.OV[0]
					return
c=computer(1,9,10,3,2,3,11,0,99,30,40,50)
for v in c.flow:print(v)
c=computer(1,0,0,0,99)
for v in c.flow:print(v)
c=computer(2,3,0,3,99)
for v in c.flow:print(v)
c=computer(2,4,4,5,99,0)
for v in c.flow:print(v)
c=computer(1,1,1,4,99,5,6,0,99)
for v in c.flow:print(v)
d=list(map(int,open("d2.txt").readline().strip().split(",")))
d[1]=12
d[2]=2
# ~ print(d)
c=computer(*d)
for v in c.flow:print(v)
for v in range(100):
	d[1]=v
	for n in range(100):
		d[2]=n
		c=computer(*d)
		r=next(c.flow)
		if r==19690720:
			print(100*v+n)
			exit()
