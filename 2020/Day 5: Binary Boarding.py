#!/usr/bin/env python
# -*- coding: utf-8 -*-
fn,part="d5.txt",1
data=open(fn).read().split("\n\n")[part]
mx=0
sids=[]
for l in data.splitlines():
	row=l[:7]
	col=l[7:]
	row=row.replace("F","0")
	row=row.replace("B","1")	
	col=col.replace("L","0")
	col=col.replace("R","1")
	row=int(row,2)
	col=int(col,2)
	sid=row*8+col
	sids.append(sid)
	mx=max(mx,sid)
print("p1:",mx)
mis=min(sids)
mas=max(sids)
print("p2:",set(range(mis,mas+1))-set(sids))

