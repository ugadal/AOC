#!/usr/bin/env python
# -*- coding: utf-8 -*-
part=1
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
# ~ block=open(fn).read().split("\n\n")[part]
inst=open(fn).readline()
m=computer(inst)
def put(s):
	m.inp=[ord(c) for c in s]+[10]
	print( readmsg() )
def readmsg():
	msg=[]
	while True:
		k=next(m.flow)
		if k=="waiting":
			return "".join(msg)
		msg.append(chr(k))
msg=readmsg()
print(msg)
# ~ while True:
	# ~ d=input("nc ? : ")
	# ~ match d:
		# ~ case "n":put("north")
		# ~ case "s":put("south")
		# ~ case "e":put("east")
		# ~ case "w":put("west")
		# ~ case _ :put(d)
# ~ exit()
put("south")
# ~ put("take space law space brochure")
put("south")
# ~ put("take mouse")
put("west")
put("north")
put("north")
put("take wreath")
put("south")
put("south")
put("east")
put("south")
put("take astrolabe")
put("south")
put("take mug")
put("north")
put("north")
put("north")
put("west")
put("take sand")
put("north")
# ~ put("take manifold")
put("south")
put("west")
put("west")
put("west")
put("inv")
input()
exit()
ite=["space law space brochure","mouse","wreath","astrolabe","mug","sand","manifold"]
carried=set(ite)
Alert=re.compile(r"Alert!")
for pack in range(2,7):
	for comb in it.combinations(ite,pack):
		for i in comb:
			if i not in carried:
				put(f"take {i}")
				carried.add(i)
		for i in list(carried):
			if i not in comb:
				put(f"drop {i}")
				carried.remove(i)
		m.inp=[ord(c) for c in "west"]+[10]
		msg=readmsg()
		if not Alert.search(msg):break
		print(carried)
		print (msg)
		# ~ input()

d=input("nc ? : ")
match d:
	case "n":put("north")
	case "s":put("south")
	case "e":put("east")
	case "w":put("west")
	case _ :put(d)

