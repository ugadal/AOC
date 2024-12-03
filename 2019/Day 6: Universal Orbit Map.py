#!/usr/bin/env python
# -*- coding: utf-8 -*-
fn,part="d6.txt",0
from collections import deque
D=deque([l.split(")") for l in open(fn).read().splitlines()])
K={"COM":0}
while D:
	a,b=D.popleft()
	if a in K:
		cd=K[a]
		K[b]=cd+1
	else:D.append((a,b))
print(sum(K.values()))
