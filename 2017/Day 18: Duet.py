#!/usr/bin/env python
# -*- coding: utf-8 -*-
D={}
inst=open("d18.txt").read().split("\n\n")[1].splitlines()
print(inst)
pos=0
def myint(s):
	r=1
	if s.startswith("-"):
		r=-1
		s=s[1:]
	if s.isdigit():return r*int(s)
	return D.get(s,0)
while True:
	ti=inst[pos]
	match ti.split():
		case ["set",*arg]:
			t,v=arg
			v=myint(v)
			D[t]=v
			pos+=1
		case ["add",*arg]:
			t,v=arg
			v=myint(v)
			D[t]+=v
			pos+=1
		case ["mul",*arg]:
			targ,v=arg
			t=myint(targ)
			v=myint(v)
			D[targ]=t*v
			pos+=1
		case ["mod",*arg]:
			t,v=arg
			v=myint(v)
			D[t]%=v
			pos+=1
		case ["jgz",*arg]:
			t,v=arg
			t=myint(t)
			v=myint(v)
			if t>0:pos+=v
			else:pos+=1
		case ["snd",*arg]:
			print(arg)
			v=arg[0]
			v=myint(v)
			D["sound"]=v
			pos+=1
		case ["rcv",*arg]:
			print(arg)
			v=arg[0]
			v=myint(v)
			if v!=0:
				print(D)
				exit()
			pos+=1
	print(pos,D)
			
