#!/usr/bin/env python
# -*- coding: utf-8 -*-
I=open(0).read().strip().split(", ")
dx,dy=0,1
cx,cy=0,0
V=[(cx,cy)]
for i in I:
	lr=i[0]
	s=int(i[1:])
	if lr=="R":
		dx,dy=dy,-dx
	else:
		dx,dy=-dy,dx
	for _ in range(s):
		cx+=dx
		cy+=dy
		if (cx,cy) in V:
			print(abs(cx)+abs(cy))
			exit()
		V.append((cx,cy))
	
