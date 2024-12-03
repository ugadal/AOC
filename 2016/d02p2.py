#!/usr/bin/env python
# -*- coding: utf-8 -*-
I=open(0).read().strip().splitlines()
cr,cc=2,0
code=[]
    # ~ x   : 0 1 2 3 4
    # ~ mxy : 0 1 2 1 0
V={}
V[0,2]="D"
V[1,1]="A"
V[1,2]="B"
V[1,3]="C"
V[2,0]="5"
V[2,1]="6"
V[2,2]="7"
V[2,3]="8"
V[2,4]="9"
V[3,1]="2"
V[3,2]="3"
V[3,3]="4"
V[4,2]="1"
for i in I:
	for c in i:
		match c:
			case 'U':
				if (cr+1,cc) in V:cr+=1
			case 'D':
				if (cr-1,cc) in V:cr-=1
			case 'L':
				if (cr,cc-1) in V:cc-=1
			case 'R':
				if (cr,cc+1) in V:cc+=1
	code.append(V[cr,cc])
print(code)
