#!/usr/bin/env python
# -*- coding: utf-8 -*-
fn,part="d21.txt",1
tp=5
reg=[0]*6
instructions=open(fn).read().splitlines()
from alive_progress import alive_bar
def addr(a,b,c):
	def fun(reg):
		reg[c]=reg[a]+reg[b]
		# ~ print(reg)
	return fun
def addi(a,b,c):
	def fun(reg):
		reg[c]=reg[a]+b
		# ~ print (reg)
	return fun
def mulr(a,b,c):
	def fun(reg):
		reg[c]=reg[a]*reg[b]
		# ~ print(reg)
	return fun
def muli(a,b,c):
	def fun(reg):
		reg[c]=reg[a]*b
		# ~ print(reg)
	return fun
def banr(a,b,c):
	def fun(reg):
		reg[c]=reg[a]&reg[b]
		# ~ print(reg)
	return fun
def bani(a,b,c):
	def fun(reg):
		reg[c]=reg[a]&b
		# ~ print(reg)
	return fun
def borr(a,b,c):
	def fun(reg):
		reg[c]=reg[a]|reg[b]
		# ~ print(reg)
	return fun
def bori(a,b,c):
	def fun(reg):
		reg[c]=reg[a]|b
		# ~ print(reg)
	return fun
def setr(a,b,c):
	def fun(reg):
		reg[c]=reg[a]
		# ~ print(reg)
	return fun
def seti(a,b,c):
	def fun(reg):
		reg[c]=a
		# ~ print(reg)
	return fun
def gtir(a,b,c):
	def fun(reg):
		reg[c]=1 if a>reg[b] else 0
		# ~ print(reg)
	return fun
def gtri(a,b,c):
	def fun(reg):
		reg[c]=1 if reg[a]>b else 0
		# ~ print(reg)
	return fun
def gtrr(a,b,c):
	def fun(reg):
		reg[c]=1 if reg[a]>reg[b] else 0
		# ~ print(reg)
	return fun
def eqir(a,b,c):
	def fun(reg):
		reg[c]=1 if a==reg[b] else 0
		# ~ print(reg)
	return fun
def eqri(a,b,c):
	def fun(reg):
		reg[c]=1 if reg[a]==b else 0
		# ~ print(reg)
	return fun
def eqrr(a,b,c):
	def fun(reg):
		reg[c]=1 if reg[a]==reg[b] else 0
		# ~ print(reg)
	return fun
op=[]

funs=[addi,addr,bani,banr,bori,borr,eqir,eqri,eqrr,gtir,gtri,gtrr,muli,mulr,seti,setr]
FD={}
for fun in funs:FD[fun.__name__]=fun

for line in instructions[1:]:
	fun,a,b,c=(line.split())
	op.append(FD[fun](int(a),int(b),int(c)))
print(op)
ip=0
a=0
with alive_bar() as bar:
	while True:
		reg[0]*6
		reg[0]=a
		# ~ print("testing",a)
		for test in range(1000000):
			# ~ print(ip)
			try:fu=op[ip]
			except:
				 print(a,reg,"break at cycle",test)
				 break
			reg[tp]=ip
			# ~ print(reg)
			fu(reg)
			ip=reg[tp]
			ip+=1
		a+=1
		bar()
	
