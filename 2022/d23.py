#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ~ import sympy
import sys
day=sys.argv[0].split(".")[0][1:]
exp=f"exp{day}.txt"
real=f"d{day}.txt"
N=[-1+1j,0+1j,1+1j]
E=[1+1j,1+0*1j,1-1j]
S=[-1-1j,0-1j,1-1j]
W=[-1+1j,-1+0*1j,-1-1j]
dirs=[N,S,W,E]
around=list(set(N+S+E+W))
print(around)
# ~ exit()

Occupied=[]
def map():
	maxr=int(max(elf.pos.imag for elf in Pop))
	minr=int(min(elf.pos.imag for elf in Pop))
	maxc=int(max(elf.pos.real for elf in Pop))
	minc=int(min(elf.pos.real for elf in Pop))
	# ~ for row in range(maxr,minr-1,-1):
		# ~ print ("".join(["#" if col+row*1j in Occupied else "." for col in range(minc,maxc+1)]))
	# ~ print("="*(1+maxc-minc))
	# ~ print((maxc-minc+1)*(maxr-minr+1)-len(Pop))
	# ~ print(minr,maxr,minc,maxc)
moved=0
class elves():
	def __init__(s,row,col):
		s.pos=col-row*1j
		s.nxtpos=s.pos
		Pop.append(s)
	def cnxtpos(s):
		s.nxtpos=s.pos
		if all([s.pos+delta not in Occupied for delta in around]):return
		for D in dirs:
			if any([s.pos+delta in Occupied for delta in D]):continue
			s.nxtpos=s.pos+D[1]
			break
	def move(s):
		if ANP.count(s.nxtpos)==1 and s.pos!=s.nxtpos:
			s.pos=s.nxtpos
			return True
		return False
		
for fn in [real]:
	Pop=[]
	for row,l in enumerate(open(fn).read().splitlines()):
		for col,c in enumerate(l):
			if c=="#":elves(row,col)
	Occupied=[elf.pos for elf in Pop]
	map()
	print (len(Pop))
	e=0
	while True:
		e+=1
		for elf in Pop:elf.cnxtpos()
		ANP=[elf.nxtpos for elf in Pop]
		M=[elf.move() for elf in Pop]
		moved=M.count(True)
		print(f"{moved} elves moved at round {e}")
		if moved==0:
			break
		Occupied=[elf.pos for elf in Pop]
		map()
		dirs.append(dirs.pop(0))
	
# 912<x<937
# ~ 916
