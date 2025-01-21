#!/usr/bin/env python
# -*- coding: utf-8 -*-
fn,part="d12.txt",3
sep="\n\n"
data=open(fn).read().split(sep)[part].splitlines()
class moon():
	def __init__(self,line):
		print("initing moon",line)
		P=line[1:-1].split(", ")
		P=[p.split("=")[1] for p in P]
		P=list(map(int,P))
		self.x,self.y,self.z=P
		self.dx=0
		self.dy=0
		self.dz=0
		self.cx=0
		self.cy=0
		self.cz=0
		self.E=0
		self.pote=0
		self.kine=0
		self.offset=0
	def __str__(self):
		return f"{self.x},{self.y},{self.z},'==',{self.dx},{self.dy},{self.dz} [{self.E}]"
	def recenter(self,x,y,z):
		self.offset=(x,y,z)
		self.x-=x
		self.y-=y
		self.z-=z
	def move(self):
		self.x+=self.dx
		self.y+=self.dy
		self.z+=self.dz
		self.cx+=self.dx
		self.cy+=self.dy
		self.cz+=self.dz
		# ~ self.energ()
		self.rp()
		self.kin()
	def rp(self):
		self.pote=abs(self.x)+abs(self.y)+abs(self.z)
	def kin(self):
		self.kine=abs(self.dx)+abs(self.dy)+abs(self.dz)
		return self.kine
	def energ(self):
		pote=abs(self.x)+abs(self.y)+abs(self.z)
		kine=abs(self.dx)+abs(self.dy)+abs(self.dz)
		self.E=pot*kin
Moons=[moon(line) for line in data]
nbm=len(Moons)
xcg=sum(m.x for m in Moons)/nbm
ycg=sum(m.y for m in Moons)/nbm
zcg=sum(m.z for m in Moons)/nbm
print(xcg,ycg,zcg)
# ~ for moon in Moons:moon.recenter(xcg,ycg,zcg)
# ~ exit()
cyc=0
# ~ V={}
# ~ hashmoons="".join([m.__str__() for m in Moons])
# ~ tte=sum(m.E for m in Moons)
# ~ V[tte]=[hashmoons]
moona=Moons[0]
V=[moona.__str__()]
pcyc=0
print(moona.kin())
print([m.kin() for m in Moons])
ttke=sum(m.kin() for m in Moons)
print(ttke)
# ~ exit()
while True:
	cyc+=1
	for pa,ma in enumerate(Moons[:-1]):
		for mb in Moons[pa+1:]:
			if ma.x<mb.x:
				ma.dx+=1
				mb.dx-=1
			elif ma.x>mb.x:
				ma.dx-=1
				mb.dx+=1
			if ma.y<mb.y:
				ma.dy+=1
				mb.dy-=1
			elif ma.y>mb.y:
				ma.dy-=1
				mb.dy+=1
			if ma.z<mb.z:
				ma.dz+=1
				mb.dz-=1
			elif ma.z>mb.z:
				ma.dz-=1
				mb.dz+=1
	# ~ for moon in Moons:print(moon)
	for moon in Moons:moon.move()
	ttke=sum(abs(m.dz) for m in Moons)
	print(cyc,ttke)
	# ~ if Moons[3].kin()==0:
		# ~ print(cyc,cyc-pcyc)
		# ~ pcyc=cyc
		# ~ exit()
# ~ for moon in Moons:pr
# ~ x:1014
# ~ y: 2949
# ~ z:2351
# ~ 9 14 22
# ~ ppcm 115807, 48118, 72312
def pgcd(a,b):
	while b:a,b=b,a%b
	return a
def ppcm(a,b):
	return a*b/pgcd(a,b)
print(ppcm(ppcm(115807,48118),72312))
