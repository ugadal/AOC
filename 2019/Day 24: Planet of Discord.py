#!/usr/bin/env python
# -*- coding: utf-8 -*-
part=0
def repres(p,v):print(f"p{p}: {v}")
import re
import sys
import itertools as it
from functools import cache
import random
from intcoded23 import *
# ~ import uuid
# ~ import numpy as np
cp=str(sys.argv[0])
dre=re.compile(r"^Day (\d+):")
day=dre.findall(cp)[0]
fn=f"d{day}.txt"
# ~ block=open(fn).read().split("\n\n\n")[part]
block=open(fn).read().split("\n\n")[part]
# ~ print(block)
M=[computer(block) for x in range(50)]
for ic,m in enumerate(M):
	m.inp.append(ic)
nat=[None,None,None,None]
while True:
	idle=True
	for ic,m in enumerate(M):
		while True:
			x=next(m.flow)
			if x=="waiting":break
			idle=False
			y=next(m.flow)
			z=next(m.flow)
			print(ic,x,y,z)
			if x==255:
				lastnat=(y,z)
				# ~ if c==y and d==z:
					# ~ print(nat)
					# ~ exit()
			else:
				M[x].inp.extend((y,z))
	if idle:
		a,b,c,d=nat
		y,z=lastnat
		nat=[c,d,y,z]
		if c==y and d==z:
				print(nat[-1])
				exit()
		M[0].inp.extend((y,z))		
				
