#!/usr/bin/env python3
#
#  Day 1: Secret Entrance.py
sep="\n\n"
fn,part="d1.txt",0
names,_,inst=open(fn).read().splitlines()
names=names.split(",")
p=1 
mx=len(names)
for i in inst.split(","):
	s=int(i[1:])
	match i[0]:
		case "L":p=max(1,p-s)
		case "R":p=min(mx,p+s)
print("p1 :",names[p-1])
data=""""Jorathnylor,Aelgaz,Zynzrak,Rylarorath,Morntyr,Agnarthyn,Aeoreth,Gavrilor,Ulmarhal,Hyradrith,Pylarwyris,Jorathardith,Cyndmir,Jallorath,Glaurendris,Thymnarel,Irynselor,Vyrlmirath,Quorxar,Phyrzar

L19,R11,L16,R9,L18,R6,L7,R13,L16,R18,L5,R14,L5,R14,L5,R18,L5,R8,L5,R11,L9,R11,L18,R7,L7,R10,L8,R15,L7"""
names,_,inst=data.splitlines()
names=names.split(",")
mx=len(names)
p=0
for i in inst.split(","):
	s=int(i[1:])
	match i[0]:
		case "L":p=(p-s)%mx
		case "R":p=(p+s)%mx
print("p2 :",names[p])
data="""Cynvarvalir,Luthirin,Glynnsor,Kaltor,Yndirin,Zarzar,Jaerbryn,Myndeldrin,Axalsar,Jorathsyx,Thalkryth,Shaelyth,Drelhal,Shaelath,Thyrosix,Quarnkryth,Xanthel,Cyndereldrin,Torilor,Tyreth,Oronvor,Sarnpyr,Ravasis,Wyndra,Xarkynar,Hyraris,Orahulth,Durnlon,Adalquin,Aelitheldrith

L46,R5,L46,R7,L46,R24,L45,R32,L32,R19,L7,R32,L38,R23,L42,R16,L19,R28,L35,R37,L5,R13,L5,R31,L5,R39,L5,R35,L5,R8,L5,R23,L5,R19,L5,R23,L5,R38,L5,R18,L38,R18,L22,R15,L44,R24,L46,R21,L25,R7,L11,R10,L28,R13,L16,R40,L20,R30,L22"""
names,_,inst=data.splitlines()
names=names.split(",")
mx=len(names)
for i in inst.split(","):
	s=int(i[1:])
	if i[0]=="L":s=mx-s
	s=s%mx
	names[0],names[s]=names[s],names[0]
print("p3 :",names[0])
