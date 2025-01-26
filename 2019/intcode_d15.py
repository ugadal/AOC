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
		while True:
			cmd=str(self.OV[self.pos]).zfill(5)
			opcode=int(cmd[-2:])
			ic,ib,ia=map(int,cmd[:3])
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
					self.OV[pa]=self.inp.pop(0)
					self.pos+=2
				case 4:
					va=self.fixr(self.pos+1,ia)
					yield va
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
					yield f"end {self.OV[0]}"
					# ~ return self.OV[0]
					# ~ self.pos+=2
# ~ d=(109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99)
# ~ c=computer(*d)
# ~ for v in c.flow:print(v,end=", ")
# ~ print()
# ~ d=(1102,34915192,34915192,7,4,7,99,0)
# ~ c=computer(*d)
# ~ for v in c.flow:print(v,end=", ")
# ~ d=(104,1125899906842624,99)
# ~ print()
# ~ c=computer(*d)
# ~ for v in c.flow:print(v,end=", ")
# ~ print("====")

import sys


def main(args):
    return 0
def draw(cp):
	mic=int(min(m.real for m in M))
	mxc=int(max(m.real for m in M))
	mir=int(min(m.imag for m in M))
	mxr=int(max(m.imag for m in M))
	S=complex(0,0)
	for r in range(mir,mxr+1):
		R=[]
		for c in range(mic,mxc+1):
			pos=complex(c,r)
			if pos==S:sym="S"
			elif pos==cp:sym="D"
			else:sym=M.get(pos," ")
			R.append(sym)
		print("".join(R))
	print() 

done={}
M={}
cp=complex(0,0)
M[cp]="."
DIRS={cd:d for cd,d in zip((-1j,1j,-1,1),(1,2,3,4))}
LDIRS={a:b for a,b in zip((-1j,1j,-1,1),(-1,1,1j,-1j))}
RDIRS={a:b for a,b in zip((-1j,1j,-1,1),(1,-1,-1j,1j))}
cd=1

if __name__ == '__main__':
	d=open("d15.txt").readline().strip()
	c=computer(d)
	ofound=0
	while True:
		# ~ print(cp,cd)
		c.inp.append(DIRS[cd])
		res=next(c.flow)
		match res:
			case 0:
				M[cp+cd]="#"
				cd=LDIRS[cd]
			case 1:
				M[cp+cd]="."
				cp+=cd
				cd=RDIRS[cd]
			case 2:
				M[cp+cd]="O"
				cp+=cd
				cd=RDIRS[cd]
				ofound+=1
				if ofound==3:break
				# ~ print("oxygen found",cp+cd)
				target=cp
				# ~ go=input("continue")
				# ~ if go=="no":break
		# ~ print(cp,cd)
		# ~ draw(cp)
		# ~ input()
	# ~ print("target",target)
	# ~ input()
	# ~ draw(complex(0,0))
	todo=[(complex(0,0),0)]
	done={}
	while True:
		cp,sd=todo.pop(0)
		if cp in done:continue
		print(cp,sd)
		if cp==target:
			print(sd)
			break
		for cd in (-1,1,1j,-1j):
			if M.get(cp+cd,"#")=="#":continue
			if cp+cd in done:continue
			todo.append((cp+cd,sd+1))
			done[cp]=True
	
