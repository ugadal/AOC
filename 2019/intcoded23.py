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
		# ~ self.flow=self.run()
		self.inp=[]
		self.rb=0
		self.out=False
		self.flow=self.run()
		self.comp=0
	def fixr(self,pos,f):
		pa=self.OV[pos]
		if f==0:return self.OV.get(pa,0)
		if f==2:return self.OV.get(pa+self.rb,0)
		return pa #1
	def fixw(self,pos,f): #target cell
		pa=self.OV[pos]
		if f==0:return pa
		if f==2:return pa+self.rb
		return pa 
	def run(self):
		# ~ self.pos=0
		while True:
			cmd=str(self.OV[self.pos]).zfill(5)
			opcode=int(cmd[-2:])
			ic,ib,ia=map(int,cmd[:3])
			# ~ print("curr cmd",cmd,opcode)
			self.comp+=1
			if self.comp>100000:
				yield "waiting"
				self.comp=0
			match opcode:
				case 1: #add
					va=self.fixr(self.pos+1,ia)
					vb=self.fixr(self.pos+2,ib)
					tc=self.fixw(self.pos+3,ic)
					self.OV[tc]=va+vb
					self.pos+=4
				case 2: #mult
					va=self.fixr(self.pos+1,ia)
					vb=self.fixr(self.pos+2,ib)
					tc=self.fixw(self.pos+3,ic)
					self.OV[tc]=va*vb
					self.pos+=4
				case 3:
					pa=self.fixw(self.pos+1,ia)   #!!!
					try:
						# ~ print("popped",self.inp)
						self.OV[pa]=self.inp.pop(0)
						# ~ print("read",self.OV[pa])
					except:
						# ~ print("unable to pop from inp using -1")
						self.OV[pa]=-1
						# ~ return
					self.pos+=2
				case 4:
					va=self.fixr(self.pos+1,ia)
					self.out=True
					yield va
					self.out=False
					self.comp=0
					self.pos+=2
				case 5: # jump if non zero param1
					pa=self.fixr(self.pos+1,ia)
					pb=self.fixr(self.pos+2,ib)
					if pa:self.pos=pb
					else:self.pos+=3
				case 6: # jump if zero param1
					pa=self.fixr(self.pos+1,ia)
					pb=self.fixr(self.pos+2,ib)
					if pa==0:self.pos=pb
					else:self.pos+=3
				case 7: #pa lesser pb than
					pa=self.fixr(self.pos+1,ia)
					pb=self.fixr(self.pos+2,ib)
					tc=self.fixw(self.pos+3,ic)
					if pa<pb:self.OV[tc]=1
					else:self.OV[tc]=0
					self.pos+=4
				case 8:#pa==pb
					pa=self.fixr(self.pos+1,ia)
					pb=self.fixr(self.pos+2,ib)
					tc=self.fixw(self.pos+3,ic)
					if pa==pb:self.OV[tc]=1
					else:self.OV[tc]=0
					self.pos+=4
				case 9:
					pa=self.fixr(self.pos+1,ia)
					self.rb+=pa
					self.pos+=2
				case 99:
					# ~ print("ending")
					# ~ self.out.append(self.OV[0])
					yield self.OV[0]
					# ~ yield self.OV[0]
					# ~ yield f"end {self.OV[0]}"
if __name__ == '__main__':
	d=open("d17.txt").readline().strip()
	c=computer(d)
	print(next(c.flow))
