#!/usr/bin/env python
# -*- coding: utf-8 -*-
KW={}
def iswall(x,y):
	if (x,y) in KW:return KW[x,y]
	t=x*x + 3*x + 2*x*y + y + y*y+1352
	v=t.bit_count()
	v%=2
	v=v==1	
	KW[x,y]=v
	return v
step=0
seen=[(1,1)]
todo=[(1,1)]
while True:
	step+=1
	print(step,len(todo),len(seen))
	nxttodo=[]
	for (cx,cy) in todo:
		if cx==31 and cy==39:
			print(step-1)
			exit()
		for dx,dy in ((1,0),(0,1),(-1,0),(0,-1)):
			if cx+dx<0 or cy+dy<0:continue
			nc=(cx+dx,cy+dy)
			if not iswall(*nc) and nc not in seen:
				nxttodo.append(nc)
				seen.append(nc)
	todo=nxttodo
	if not todo:exit()
				
			
