#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ~ 50x6
D=[]
for r in range(6):D.append(["-"]*50)
def rep():
	for row in D:print ("".join(row))
for line in open("d08.txt").read().splitlines():
	match line.split():
		case ["rect",arg]:
			a,b=map(int,arg.split("x"))
			for c in range(a):
				for r in range(b):
						D[r][c]="#"
		case ['rotate',"row",*arg]:
			a,_,c=arg
			row=int(a.split("=")[1])
			c=int(c)
			t=D[row]
			D[row]=t[-c:]+t[:-c]
		case ['rotate',"column",*arg]:
			a,_,c=arg
			row=int(a.split("=")[1])
			c=int(c)
			D=list(map(list,zip(*D)))
			t=D[row]
			D[row]=t[-c:]+t[:-c]
			D=list(map(list,zip(*D)))
rep()
print(sum([row.count("#") for row in D]))
