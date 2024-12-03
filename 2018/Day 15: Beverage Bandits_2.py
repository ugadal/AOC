#!/usr/bin/env python
# -*- coding: utf-8 -*-
fn="d15.txt"
block=open(fn).read().split("\n\n")[4]
class grid():
	def __init__(self):
		self.map={}
		self.dirs=[-1j,-1,1,1j]
	def reachable(self,	startpos,targets):
		targset=set()
		for pos in targets:targset.add(pos)
		visited=set()
		todo=[startpos]
		steps=0
		while todo:
			newtodo=set()
			steps+=1
			for pos in todo:visited.add(pos)
			for pos in todo:
				npos=[pos+dpos for dpos in self.dirs]
				npos=[pos for pos in npos if self.map[pos]=="."]
				npos=[pos for pos in npos if not pos in visited]
				for pos in npos:newtodo.add(pos)
			reached=newtodo & targset
			if reached:return steps,reached
			todo=list(newtodo)
		return None,None
	def getdist(self,startpos,endpos):
		if startpos==endpos:return 0
		d,rts=self.reachable(startpos,[endpos])
		return d
M=grid()
for row,line in enumerate(block.splitlines()):
	for col,sym in enumerate(line):
		M.map[row*1j+col]=sym
M.NR=int(max(pos.imag for pos in M.map.keys()))
M.NC=int(max(pos.real for pos in M.map.keys()))
class mob():
	def __init__(self,pos,t):
		self.pos=pos
		self.elf=t
		self.hp=200
		self.ops=None
		self.reached=None
		self.paths=None
		self.attackp=3
	def canattack(self):
		attackable=[]
		for dpos in dirs:
			targ=self.pos+dpos
			attackable.extend((opp for opp in self.ops if opp.pos==targ and opp.hp>0))
		attackable=sorted(attackable,key=lambda m:(m.hp,m.pos.imag,m.pos.real))
		return attackable[:1]
	def attack(self):
		fight=self.canattack()[0]
		if fight.hp<=0:
			print("elf" if fight.elf else "goblin",f"at {fight.pos} attacked but already killed {fight.hp} before fight")
		print("elf" if fight.elf else "goblin",f"at {fight.pos} attacked {fight.hp} before fight")
		print("attack !!")
		fight.hp-=mob.attackp
		if fight.hp<=0:
			print("elf" if fight.elf else "goblin",f"at {fight.pos} killed")
			M.map[fight.pos]="."
	def aop(self):
		accop=set()
		for op in self.ops:
			if op.hp<=0:continue
			for dpos in dirs:
				targ=op.pos+dpos
				if M.map[targ]==".":accop.add(targ)
		return accop
	def iam(self):
		return "elf" if self.elf else "goblin"
dirs=[-1j,-1,1,1j]
Elves=[mob(pos,True) for pos,symb in M.map.items() if symb=="E"]
ttelves=len(Elves)
Goblins=[mob(pos,False) for pos,symb in M.map.items() if symb=="G"]
for mob in Elves:
	mob.ops=Goblins
	mob.attackp=23
for mob in Goblins:mob.ops=Elves
def draw():
	for row in range(1+M.NR):
		rt=[]
		for col in range(1+M.NC):
			rt.append(M.map[row*1j+col])
		print(row,"\t","".join(rt))
# ~ input()
fullcycles=1
while True:
	draw()
	print("new cycle",fullcycles)
	Elves=[elf for elf in Elves if elf.hp>0]
	Goblins=[goblin for goblin in Goblins if goblin.hp>0]
	ooa=Elves+Goblins
	ooa=sorted(ooa,key=lambda x:(x.pos.imag,x.pos.real))
	for mob in ooa:
		# ~ draw()
		# ~ print("working on",mob.iam(),mob.pos)
		if mob.hp<=0:continue
		fight=mob.canattack()
		if fight:
			mob.attack()
			if all(op.hp<=0 for op in mob.ops):
				print("all enemies dead",fullcycles,ttelves,"initially , ",len([elf for elf in Elves if elf.hp>0]))
				print(fullcycles*sum(mob.hp for mob in ooa if mob.hp>0))
				print((fullcycles-1)*sum(mob.hp for mob in ooa if mob.hp>0))
				exit()
			continue
		dist,rts=M.reachable(mob.pos,mob.aop())
		if dist:
			# ~ print(f"mob at {mob.pos} moves")
			goingto=sorted(rts,key=lambda pos:(pos.imag,pos.real))[0]
			# ~ print("goingto",goingto)
			avail=[mob.pos+dpos for dpos in M.dirs]
			# ~ print("pre",avail)
			avail=[pos for pos in avail if M.map[pos]=="."]
			# ~ print("post",avail)
			for pos in avail:
				if M.getdist(pos,goingto)==dist-1:
					firstep=pos
					break
			print(f"{mob.iam()} at {mob.pos} moves to  {firstep}")
		else:continue
		cpos=mob.pos
		csym=M.map[cpos]
		M.map[firstep]=csym
		M.map[cpos]="."
		mob.pos=firstep
		fight=mob.canattack()
		if fight:
			mob.attack()
			if all(op.hp<=0 for op in mob.ops):
				print("all enemies dead",fullcycles,ttelves,"initially , ",len([elf for elf in Elves if elf.hp>0]))
				print(fullcycles*sum(mob.hp for mob in ooa if mob.hp>0))
				print((fullcycles-1)*sum(mob.hp for mob in ooa if mob.hp>0))
				exit()
			
	fullcycles+=1
