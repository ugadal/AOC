#!/usr/bin/env python
# -*- coding: utf-8 -*-
class computer():
	def __init__(self,inst,a,b,c):
		self.inst=inst
		v=0
		print(v)
		self.reg=[a,b,c]
		self.pos=0
		self.flow=self.run()
		self.inp=[]
		self.rb=0
	def fixop(self,op):
		if op==7:return 7
		if op&4:return self.reg[op&3]
		return op
	def run(self):
		while True:
			try:
				cmd=self.inst[self.pos]
				operand=self.inst[self.pos+1]
			except:cmd=99
			combo=self.fixop(operand)
			match cmd:
				case 0: #div A//op >A
					self.reg[0]//=2**combo
					self.pos+=2
				case 1: #B xor op >B
					self.reg[1]^=operand
					self.pos+=2
				case 2: 
					self.reg[1]=combo%8
					self.pos+=2
				case 3:
					if self.reg[0]:self.pos=operand
					else:self.pos+=2
				case 4: 
					self.reg[1]^=self.reg[2]
					self.pos+=2
				case 5:
					yield combo%8
					self.pos+=2
				case 6:
					self.reg[1]=self.reg[0]//2**combo
					self.pos+=2
				case 7:
					self.reg[2]=self.reg[0]//2**combo
					self.pos+=2
				case 99:
					# ~ yield f"end"
					return
import sys


def main(args):
    return 0


if __name__ == '__main__':
	# ~ cc=computer((2,4,1,3,7,5,0,3,1,5,4,4,5,5,3,0),130606920348432,0,0)
	cc=computer((2,4,1,3,7,5,0,3,1,5,4,4,5,5,3,0),35184372088833,0,0)
	r=",".join(map(str,(cc.flow)))
	print(len(r))
	print(r)
	print(cc.reg)
