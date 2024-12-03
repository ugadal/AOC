#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
day=sys.argv[0].split(".")[0][1:]
# ~ print(day)
import re
exp=f"exp{day}.txt"
real=f"d{day}.txt"
# ~ neig=[(dx,dy,dz) for dx in range(-1,2) for dy in range(-1,2) for dz in range(-1,2)]
neig=[
	(1,0,0),
	(-1,0,0),
	(0,1,0),
	(0,-1,0),
	(0,0,1),
	(0,0,-1)]
def GetFaces(t):
	x,y,z=t
	yield (x,y,z),(x,y,z+1),(x+1,y,z+1),(x+1,y,z)
	yield (x,y+1,z),(x,y+1,z+1),(x+1,y+1,z+1),(x+1,y+1,z)
	yield (x+1,y,z),(x+1,y,z+1),(x+1,y+1,z+1),(x+1,y+1,z)
	yield (x,y,z),(x,y,z+1),(x,y+1,z+1),(x,y+1,z)
	yield (x,y,z+1),(x,y+1,z+1),(x+1,y+1,z+1),(x+1,y,z+1)
	yield (x,y,z),(x,y+1,z),(x+1,y+1,z),(x+1,y,z)
# ~ python3 d18.py|sort |uniq -u|wc -l
lines=open(exp).read().strip().splitlines()
lines=open(real).read().strip().splitlines()
cubes=[eval(l) for l in lines]
faces=[face for cube in cubes for face in GetFaces(cube)]
minx=min([x for x,y,z in cubes])
maxx=max([x for x,y,z in cubes])
miny=min([y for x,y,z in cubes])
maxy=max([y for x,y,z in cubes])
minz=min([z for x,y,z in cubes])
maxz=max([z for x,y,z in cubes])
print(minx,maxx,miny,maxy,minz,maxz)
Out=[]
for x in range(minx,maxx+1):
	for y in range(miny,maxy+1):
		for z in range(minz,maxz+1):
			if (x,y,z) in cubes:continue
			Out.append((x,y,z))
print (len(Out),(maxx-minx+1)*(maxy-miny+1)*(maxz-minz+1),len(cubes))
"""flood"""
Flooded=set()
for x in (minx,maxx):
	for y in range(miny,maxy+1):
		for z in range(minz,maxz+1):
			if (x,y,z) not in cubes:Flooded.add((x,y,z))
for x in range(minx,maxx+1):
	for y in (miny,maxy):
		for z in range(minz,maxz+1):
			if (x,y,z) not in cubes:Flooded.add((x,y,z))
for x in range(minx,maxx+1):
	for y in range(miny,maxy+1):
		for z in (minz,maxz):
			if (x,y,z) not in cubes:Flooded.add((x,y,z))
print ("on borders flooded",len(Flooded))
print(len(set(Out)-Flooded))
Q=list(Flooded)
while Q:
	fx,fy,fz=Q.pop(0)
	for dx,dy,dz in neig:
		if minx<=fx+dx<=maxx and miny<=fy+dy<=maxy and minz<=fz+dz<=maxz:
			if (fx+dx,fy+dy,fz+dz) in Flooded:continue
			if (fx+dx,fy+dy,fz+dz) in cubes:continue
			Q.append((fx+dx,fy+dy,fz+dz))
			Flooded.add((fx+dx,fy+dy,fz+dz))
print ("after flood",len(Flooded))
print("inner cubes",len(set(Out)-Flooded))
# ~ print(set(Out)-Flooded)
for cube in set(Out)-Flooded:
	faces.extend(GetFaces(cube))		
	faces.extend(GetFaces(cube))		
print(len(faces)-len(set(faces)))
# ~ for face in faces:print(f"face {face}")
D={}
for face in faces:D[face]=D.get(face,0)+1
R=[k for k,v in D.items() if v==1]
print(len(R))
