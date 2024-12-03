#!/usr/bin/env python
# -*- coding: utf-8 -*-
I=open(0).read().strip().split(", ")
dx,dy=0,1
cx,cy=0,0
for i in I:
	lr=i[0]
	s=int(i[1:])
	if lr=="R":
		dx,dy=dy,-dx
	else:
		dx,dy=-dy,dx
	cx+=dx*s
	cy+=dy*s
	print(cx,cy)		
		
print(abs(cx)+abs(cy))
