#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
day=sys.argv[0].split(".")[0][1:]
print(day)
import re
exp=f"exp{day}.txt"
real=f"d{day}.txt"
def wg(s): # wind generator endless
	while True:
		for iw,c in enumerate(s):yield iw,c
top=ptop=pri=removed=0

# ~ 0<real<8
# ~ 0<=imaginary

def sg():
	global ptop
	rocks=[(3,4,5,6),(4,3+1j,5+1j,4+2j),(3,4,5,5+1j,5+2j),(3,3+1j,3+2j,3+3j),(3,4,3+1j,4+1j)]
	while True:
		for ir,rock in enumerate(rocks):
			iw,w=next(wind)
			k=-1 if w=="<" else 1
			if iw==0:
				print("first wind at new rock",ir,top-ptop)
				ptop=top
			yield ir,[x+k+(top+3)*1j for x in rock]
# ~ wind=wg(open(exp).readline().strip())
wind=wg(open(real).readline().strip())
rock=sg()
Occupied=set()
cmbc=[0,0,0,0,0,0,0]
def rep():
	for row in range(int(top),-1,-1):
		print("".join(["X" if c+row*1j in Occupied else "." for c in range(1,8)]))
def clean(ri,r):
	# ~ rep()
	# ~ input()
	global cmbc,Occupied,top,removed
	nh=[max([0]+[x.imag for x in r if x.real==c]) for c in range(1,8)]
	cmbc=[max(a,b) for a,b in zip(cmbc,nh)]
	if min(cmbc):
		k=min(cmbc)
		Occupied=set(x-k*1j for x in Occupied if x.imag>=k)
		removed+=k
		cmbc=[max([0]+[x.imag for x in Occupied if x.real==c]) for c in range(1,8)]
		top=max(cmbc)+1
		print("new cmbc,top,ri",top,ri,cmbc,removed)
rc=0
while True:
	rc+=1
	_,r=next(rock)
	while True:
		if any([x-1j in Occupied or x.imag==0 for x in r]):	pass
		else:r=[x-1j for x in r]
		_,w=next(wind)
		if w=="<":# ~ left <
			if any([x.real==1 for x in r]):	pass
			elif any([x-1 in Occupied for x in r]):	pass 
			else:r=[x-1 for x in r]
		else: # ~ right >
			if any([x.real==7 for x in r]):	pass
			elif any([x+1 in Occupied for x in r]):	pass 
			else:r=[x+1 for x in r]
		if any([x-1j in Occupied or x.imag==0 for x in r]):
			for x in r:Occupied.add(x)
			top=max(top,1+max([x.imag for x in r]))
			# ~ clean(rc,r) #use this and comment next three to identify loop,cycle visually
			if rc in (1702,1702+1098):
				print(rc,top)
			if rc>1702+1098:exit()
			break
