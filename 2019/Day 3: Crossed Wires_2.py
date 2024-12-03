#!/usr/bin/env python
# -*- coding: utf-8 -*-
fn,part="d3.txt",3
# ~ solution bete
a,b=open(fn).read().split("\n\n")[part].splitlines()
print(len(a),len(b))
sa=set()
la=[]
pos=0+0*1j
for move in a.split(","):
	d=move[0]
	steps=int(move[1:])
	match d:
		case 'U':
			for s in range(steps):
				pos-=1j
				la.append(pos)
		case 'D':
			for s in range(steps):
				pos+=1j
				la.append(pos)
		case 'R':
			for s in range(steps):
				pos+=1
				la.append(pos)
		case 'L':
			for s in range(steps):
				pos-=1
				la.append(pos)
sb=set()
lb=[]
pos=0+0*1j
for move in b.split(","):
	d=move[0]
	steps=int(move[1:])
	match d:
		case 'U':
			for s in range(steps):
				pos-=1j
				lb.append(pos)
		case 'D':
			for s in range(steps):
				pos+=1j
				lb.append(pos)
		case 'R':
			for s in range(steps):
				pos+=1
				lb.append(pos)
		case 'L':
			for s in range(steps):
				pos-=1
				lb.append(pos)
sa=set(la)
sb=set(lb)
# ~ print(len(sa))
# ~ print(len(sb))
# ~ print(len(sa&sb))
inter=sa&sb
# ~ print(la)
# ~ print(lb)
# ~ print(inter)
print (min([la.index(p)+lb.index(p) for p in inter])+2)
# ~ for p in inter:
	# ~ print (p,la.index(p))
	# ~ print (p,lb.index(p))
	# ~ print()
