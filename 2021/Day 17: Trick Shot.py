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
# ~ print(run(6,9))
dx=0
while dx*(dx+1)/2<lc:dx+=1 #min x speed
rec=0
dy=0
while dy<=-br:
	dy+=1
	# ~ if dy>-br:break
	mh=run(dx,dy)
	# ~ print(dx,dy,mh)
	if mh and mh<=rec:break
	rec=max(rec,mh)
	# ~ input()
print("p1:",rec)
def runp2(dx,dy):
	px=py=mh=0
	while True:
		px+=dx
		py+=dy
		mh=max(mh,py)
		dx=max(0,dx-1)
		dy-=1
		# ~ print(px,py,dx,dy,px>lc,py<br)
		if lc<=px<=rc and br<=py<=tr:return True
		if px>rc or py<br:return False
mx=0
ok=0

while mx*(mx+1)/2<lc:mx+=1 #min x speed
for dx in range(mx,rc+1):
	for dy in range(br-1,-br+1):
		hit=runp2(dx,dy)
		if hit:ok+=1
print("p2:",ok)
