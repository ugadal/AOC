#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ~ import sympy
import sys
from random import shuffle as shf
day=sys.argv[0].split(".")[0][1:]
exp=f"exp{day}.txt"
real=f"d{day}.txt"
D={}
lines=open(0).read().splitlines()
remn=[line for line in lines]
cp=0
while True:
	symbols=([line[cp] for line in remn])
	oc=symbols.count("1")
	zc=symbols.count("0")
	filt="0" if zc>oc else "1"
	# ~ print(filt,cp)
	remn=[line for line in remn if line[cp]==filt]
	# ~ print(len(remn))
	# ~ for line in remn:print(line)
	# ~ print("=====")
	if len(remn)==1:break
	cp+=1
oxg=remn[0]
print(oxg,int(oxg,2))
remn=[line for line in lines]
cp=0
while True:
	symbols=([line[cp] for line in remn])
	oc=symbols.count("1")
	zc=symbols.count("0")
	filt="1" if oc<zc else "0"
	print(filt)
	remn=[line for line in remn if line[cp]==filt]
	for line in remn:print(line)
	print()
	if len(remn)==1:break
	cp+=1
cosc=remn[0]
print(cosc,int(cosc,2))
print(int(cosc,2)*int(oxg,2))
