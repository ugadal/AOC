#!/usr/bin/env python
# -*- coding: utf-8 -*-
part=0

import re
import sys
import itertools as it
from functools import cache
import uuid
cp=str(sys.argv[0])
dre=re.compile(r"^Day (\d+):")
day=dre.findall(cp)[0]
fn=f"d{day}.txt"
# ~ block=open(fn).read().split("\n\n\n")[part]
# ~ block=open(fn).read().split("\n\n")[part]
# ~ target area: x=192..251, y=-89..-59
lc,rc,br,tr=192,251,-89,-59
# ~ target area: x=20..30, y=-10..-5
# ~ lc,rc,br,tr=20,30,-10,-5
def run(dx,dy):
	# ~ The probe's x position increases by its x velocity.
	# ~ The probe's y position increases by its y velocity.
	# ~ Due to drag, the probe's x velocity changes by 1 toward the value 0; that is, it decreases by 1 if it is greater than 0, increases by 1 if it is less than 0, or does not change if it is already 0.
	# ~ Due to gravity, the probe's y velocity decreases by 1.
	px=py=mh=0
	while True:
		px+=dx
		py+=dy
		mh=max(mh,py)
		dx=max(0,dx-1)
		dy-=1
		# ~ print(px,py,dx,dy,px>lc,py<br)
		if lc<=px<=rc and br<=py<tr:return (mh)
		if px>rc or py<br:return False
print(run(6,9))
dx=0
while dx*(dx+1)/2<lc:dx+=1 #min x speed
rec=0
dy=0
while dy<=-br:
	dy+=1
	# ~ if dy>-br:break
	mh=run(dx,dy)
	print(dx,dy,mh)
	if mh and mh<=rec:break
	rec=max(rec,mh)
	# ~ input()
print("p1:",rec)
