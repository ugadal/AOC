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
def getlitv(s):
	cp=0
	tv=""
	while True:
		tv+=s[cp+1:cp+5]
		if s[cp]=="0":break
		cp+=5
	print("lit value",int(tv,2),cp+11)
	return cp+11
def op(s):
	if s[0]=="1":
		sp=int(s[1:12],2)
		print("# subpackets",sp)
		cp=0
		for x in range(sp):
			cp+=treat(s[12+cp:])
def treat(bs):
	# ~ pv=int(bs[:3],2)
	# ~ ptid=int(bs[3:6],2)
	x=int(bs[:6],2)
	# ~ print (f"pv: {pv}, ptid: {ptid}")
	# ~ if ptid==4:
	if x&4==4:
		# ~ print (x&4==ptid)
		return getlitv(bs[6:])
	else:
		op(bs[6:])
for line in open(fn).read().splitlines()[:-1]:
	treat(bin(int(line,16))[2:])
