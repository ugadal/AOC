#!/usr/bin/env python
# -*- coding: utf-8 -*-
fn,part="d3.txt",3
# ~ solution bete
a,b=open(fn).read().split("\n\n")[part].splitlines()
print(len(a),len(b))
sa=set()
pos=0+0*1j
for move in a.split(","):
	d=move[0]
	steps=int(move[1:])
	match d:
		case 'U':
			for s in range(steps):
				pos-=1j
				sa.add(pos)
		case 'D':
			for s in range(steps):
				pos+=1j
				sa.add(pos)
		case 'R':
			for s in range(steps):
				pos+=1
				sa.add(pos)
		case 'L':
			for s in range(steps):
				pos-=1
				sa.add(pos)
sb=set()
pos=0+0*1j
for move in b.split(","):
	d=move[0]
	steps=int(move[1:])
	match d:
		case 'U':
			for s in range(steps):
				pos-=1j
				sb.add(pos)
		case 'D':
			for s in range(steps):
				pos+=1j
				sb.add(pos)
		case 'R':
			for s in range(steps):
				pos+=1
				sb.add(pos)
		case 'L':
			for s in range(steps):
				pos-=1
				sb.add(pos)
print(len(sa))
print(len(sb))
print(len(sa&sb))
inter=sa&sb
print(inter)
print (min(abs(p.real)+abs(p.imag) for p in inter))
