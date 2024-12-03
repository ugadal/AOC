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
					print("finishing")
					yield self.OV[0]
					return
c=computer(3,0,4,0,99)
c.inp.append(456)
print(next(c.flow))
c=computer(1002,4,3,4,33)
print(next(c.flow))
d=list(map(int,open("d5.txt").readline().strip().split(",")))
c=computer(*d)
c.inp.append(1)
for v in c.flow:print(v)
print("equals 8")
for i in range(10):
	c=computer(3,9,8,9,10,9,4,9,99,-1,8)
	c.inp.append(i)
	print(i,":",next(c.flow))
print("less than 8")
for i in range(10):
	c=computer(3,9,7,9,10,9,4,9,99,-1,8)
	c.inp.append(i)
	print(i,":",next(c.flow))
	
print("equals 8")
for i in range(10):
	c=computer(3,3,1108,-1,8,3,4,3,99)
	c.inp.append(i)
	print(i,":",next(c.flow))

print("less than 8")
for i in range(10):
	c=computer(3,3,1107,-1,8,3,4,3,99)
	c.inp.append(i)
	print(i,":",next(c.flow))
	
print("non zero")
for i in range(-5,6):
	c=computer(3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9)
	c.inp.append(i)
	print(i,":",next(c.flow))
print("non zero")
for i in range(-5,6):
	c=computer(3,3,1105,-1,9,1101,0,0,12,4,12,99,1)
	c.inp.append(i)
	print(i,":",next(c.flow))
	
print("999 if < 8,  1000 if == 8, 1001 if > 8")
for i in range(0,20):
	c=computer(3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99)
	c.inp.append(i)
	print(i,":",next(c.flow))
c=computer(*d)
c.inp.append(5)
for v in c.flow:print(v)
