#!/usr/bin/env python
# -*- coding: utf-8 -*-
import itertools as it
fn="d16.txt"
block=open(fn).read().split("\n\n\n")[0]
def addr(a,b,c,reg):
	nreg=list(reg)
	nreg[c]=reg[a]+reg[b]
	return nreg
def addi(a,b,c,reg):
	nreg=list(reg)
	nreg[c]=reg[a]+b
	return nreg
def mulr(a,b,c,reg):
	nreg=list(reg)
	nreg[c]=reg[a]*reg[b]
	return nreg
def muli(a,b,c,reg):
	nreg=list(reg)
	nreg[c]=reg[a]*b
	return nreg
def banr(a,b,c,reg):
	nreg=list(reg)
	nreg[c]=reg[a]&reg[b]
	return nreg
def bani(a,b,c,reg):
	nreg=list(reg)
	nreg[c]=reg[a]&b
	return nreg
def borr(a,b,c,reg):
	nreg=list(reg)
	nreg[c]=reg[a]|reg[b]
	return nreg
def bori(a,b,c,reg):
	nreg=list(reg)
	nreg[c]=reg[a]|b
	return nreg
def setr(a,b,c,reg):
	nreg=list(reg)
	nreg[c]=reg[a]
	return nreg
def seti(a,b,c,reg):
	nreg=list(reg)
	nreg[c]=a
	return nreg
def gtir(a,b,c,reg):
	nreg=list(reg)
	nreg[c]=1 if a>reg[b] else 0
	return nreg
def gtri(a,b,c,reg):
	nreg=list(reg)
	nreg[c]=1 if reg[a]>b else 0
	return nreg
def gtrr(a,b,c,reg):
	nreg=list(reg)
	nreg[c]=1 if reg[a]>reg[b] else 0
	return nreg
def eqir(a,b,c,reg):
	nreg=list(reg)
	nreg[c]=1 if a==reg[b] else 0
	return nreg
def eqri(a,b,c,reg):
	nreg=list(reg)
	nreg[c]=1 if reg[a]==b else 0
	return nreg
def eqrr(a,b,c,reg):
	nreg=list(reg)
	nreg[c]=1 if reg[a]==reg[b] else 0
	return nreg
funs=[addi,addr,bani,banr,bori,borr,eqir,eqri,eqrr,gtir,gtri,gtrr,muli,mulr,seti,setr]
print (mulr(2,1,2,[3,2,1,1]))
for fun in funs:
	print(fun(2,1,2,[3,2,1,1])==[3,2,2,1])
opfun={}
count=0
for tlset in block.split("\n\n"):
	la,lb,lc=tlset.splitlines()
	pr=list(map(int,la.split(": ")[1][1:-1].split(", ")))
	op,a,b,c=list(map(int,lb.split(" ")))
	if op not in opfun:opfun[op]=list(funs)
	ar=list(map(int,lc.split(":  ")[1][1:-1].split(", ")))	
	opfun[op]=[fun for fun in opfun[op] if fun(a,b,c,pr)==ar]
for k,v in opfun.items():print(k,len(v),v)
ops=list(opfun.keys())
fixed=[]
tofix=list(opfun.keys())
while True:
	while tofix:
		try:resolv=next(op for op in tofix if len(opfun[op])==1)
		except:break
		funtodel=opfun[resolv][0]
		# ~ print(resolv,funtodel,"to be cleaned")
		fixed.append(resolv)
		fixed.append(funtodel)
		tofix.remove(resolv)
		for op in tofix:
			if funtodel in opfun[op]:
				opfun[op].remove(funtodel)
				# ~ print(funtodel,"removed from op",op)
		# ~ print("after simplification")
		# ~ for k in tofix:print(k,len(opfun[k]))
	if all(len(v)==1 for v in opfun.values()):break
for k in opfun.keys():opfun[k]=opfun[k][0]
block=open(fn).read().split("\n\n\n")[1]
reg=[0,0,0,0]
for line in block.splitlines()[1:]:
	op,a,b,c=map(int,line.split())
	reg=opfun[op](a,b,c,reg)
print(reg[0])
