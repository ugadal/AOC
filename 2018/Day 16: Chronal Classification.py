#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
# ~ print (mulr(2,1,2,[3,2,1,1]))
# ~ for fun in funs:
	# ~ print(fun(2,1,2,[3,2,1,1])==[3,2,2,1])
count=0
for tlset in block.split("\n\n"):
	la,lb,lc=tlset.splitlines()
	# ~ Before: [1, 1, 2, 2]
	# ~ 10 0 2 0
	# ~ After:  [0, 1, 2, 2]
	pr=list(map(int,la.split(": ")[1][1:-1].split(", ")))
	op,a,b,c=list(map(int,lb.split(" ")))
	ar=list(map(int,lc.split(":  ")[1][1:-1].split(", ")))	
	# ~ print(pr,a,b,c,ar)
	working=[fun(a,b,c,pr)==ar for fun in funs].count(True)
	if working>=3:count+=1
print(count)
