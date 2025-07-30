#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
import functools
def categorize(hand):
	C=list(hand.split()[0])
	cbc=[C.count(card) for card in cards]
	if 5 in cbc :return "poker"
	if 4 in cbc :return "square"
	if 3 in cbc and 2 in cbc:return "full"
	if 3 in cbc and not 2 in cbc:return "brelan"
	if cbc.count(2)==2:return "deux paires"
	if cbc.count(2)==1:return "une paire"
	return "podzob"
def newcat(hand):
	C=list(hand.split()[0])
	cbc=[C.count(card) for card in cards2]
	J=cbc[-1]
	if not J:return categorize(hand)
	if J==1:
		if 4 in cbc[:-1]:return "poker"
		if 3 in cbc[:-1]:return "square"
		if cbc[:-1].count(2)==2 :return "full"
		if cbc[:-1].count(2)==1 :return "brelan"
		return "une paire"
	if J==2:
		if 3 in cbc[:-1]:return "poker"
		if cbc[:-1].count(2)==1 :return "square"
		return "brelan"
	if J==3:
		if cbc[:-1].count(2)==1 :return "poker"
		return "square"
	if J>=4:
		return "poker"
def mysort(a,b):
	# ~ print("received",a,b)
	for c,d in zip(a,b):
		if c==d:continue
		if cards.index(c)<cards.index(d):return 1
		return -1
def mysortb(a,b):
	# ~ print("received",a,b)
	for c,d in zip(a,b):
		if c==d:continue
		if cards2.index(c)<cards2.index(d):return 1
		return -1
		
cards=list("AKQJT98765432")
cards2=list("AKQT98765432J")
CAT=["poker","square","full","brelan","deux paires","une paire","podzob"]
CAT.reverse()
GROUPS={}
for cat in CAT:GROUPS[cat]=[]
hands=open(0).read().strip().splitlines()
for hand in hands:
	group=categorize(hand)
	GROUPS[group].append(hand)
count=0
res=0
for cat in CAT:
	for hand in sorted(GROUPS[cat],key=functools.cmp_to_key(mysort)):
		count+=1
		res+=count*int(hand.split()[1])
print (res)

GROUPS={}
for cat in CAT:GROUPS[cat]=[]
for hand in hands:
	group=newcat(hand)
	GROUPS[group].append(hand)
count=0
res=0
for cat in CAT:
	for hand in sorted(GROUPS[cat],key=functools.cmp_to_key(mysortb)):
		count+=1
		res+=count*int(hand.split()[1])
print (res)
