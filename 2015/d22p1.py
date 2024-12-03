#!/usr/bin/env python
# -*- coding: utf-8 -*-
from copy import deepcopy as dc
import itertools as it
bf=open("d22.txt")
Bhp=int(bf.readline().strip().split(": ")[1])
Bdam=int(bf.readline().strip().split(": ")[1])
print(Bhp,Bdam)
Bda={ "hp":Bhp,"dotdur":0}
Pda={"hp":50,"mana":500,"armordur":0,"mgdur":0}
Player=True
Q=[(True,Bda,Pda,0)]
rec=float('inf')
while Q:
	player,B,P,manaspent=Q.pop()
	if manaspent>rec:continue
	Bda=dc(B)
	Pda=dc(P)
	# ~ print(player,Bda,Pda,manaspent)
	if Pda["armordur"]:Pda["armordur"]-=1
	if Pda["mgdur"]:
		Pda["mgdur"]-=1
		Pda["mana"]+=101
	if Bda["dotdur"]:
		Bda["dotdur"]-=1
		Bda["hp"]-=3
	if player:
		if Pda["hp"]<=0:
			# ~ print(f"player dies, manaspent {manaspent}")
			continue
		if Pda["mana"]<53:continue
		if Pda["mana"]>=53:
			Bt=dc(Bda)
			Pt=dc(Pda)
			Bt["hp"]-=4
			Pt["mana"]-=53
			Q.append((False,Bt,Pt,manaspent+53))
		if Pda["mana"]>=73:
			Bt=dc(Bda)
			Pt=dc(Pda)
			Pt["mana"]-=73
			Pt["hp"]+=2
			Bt["hp"]-=2
			Q.append((False,Bt,Pt,manaspent+73))
		if Pda["mana"]>=113 and not Pda['armordur']:
			Bt=dc(Bda)
			Pt=dc(Pda)
			Pt["mana"]-=113
			Pt['armordur']=6
			Q.append((False,Bt,Pt,manaspent+113))
		if Pda["mana"]>=173 and not Bda['dotdur']:
			Bt=dc(Bda)
			Pt=dc(Pda)
			Pt["mana"]-=173
			Bt["dotdur"]=6
			Q.append((False,Bt,Pt,manaspent+173))
		if Pda["mana"]>=229 and not Pda['mgdur']:
			Bt=dc(Bda)
			Pt=dc(Pda)
			Pt["mana"]-=229
			Pt["mgdur"]=5
			Q.append((False,Bt,Pt,manaspent+229))
		# ~ Q.append((False,dc(Bda),dc(Pda),manaspent))
	else:
		if Bda["hp"]<=0:
			if manaspent<rec:
				print (f"Boss dies manaspent {manaspent}")
				rec=manaspent
			continue
		Bt=dc(Bda)
		Pt=dc(Pda)
		dam=2 if Pt["armordur"] else 9
		Pt["hp"]-=dam
		Q.append((True,Bt,Pt,manaspent))
		
print(rec)
# ~ Your puzzle answer was 900
