#!/usr/bin/env python
# -*- coding: utf-8 -*-
I=open(0).read().strip().splitlines()
cx,cy=1,1
code=[]
for i in I:
	for c in i:
		match c:
			case 'U':
				cy=max(0,cy-1)
			case 'D':
				cy=min(2,cy+1)
			case 'L':
				cx=max(0,cx-1)
			case 'R':
				cx=min(2,cx+1)
	code.append(3*cy+cx+1)
print(code)
