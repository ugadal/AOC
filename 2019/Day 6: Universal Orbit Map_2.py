#!/usr/bin/env python
# -*- coding: utf-8 -*-
fn,part="d6.txt",0
from collections import deque
D=deque([l.split(")") for l in open(fn).read().splitlines()])
K={"COM":(0,"NONE")}
while D:
	a,b=D.popleft()
	if a in K:
		cd,p=K[a]
		K[b]=(cd+1,a)
	else:D.append((a,b))
print(sum(a for a,b in K.values()))
p="YOU"
path=[]
while p!="COM":
	path.append(K[p][1])
	p=K[p][1]
yp=set(path)
p="SAN"
path=[]
while p!="COM":
	path.append(K[p][1])
	p=K[p][1]
sp=set(path)
md=max(K[k][0] for k in sp&yp)
fourche=next(k for k in sp&yp if K[k][0]==md)
dy=K["YOU"][0]
ds=K["SAN"][0]
df=K[fourche][0]
print(dy+ds-2*df-2)
