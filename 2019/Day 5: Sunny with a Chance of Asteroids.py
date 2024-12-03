#!/usr/bin/env python
# -*- coding: utf-8 -*-
fn,part="d5.txt",0
def treat(line,inp=1):
	TV=line.split(",")
	OV=list(map(int,TV))
	pos=0
	print(OV)
	while True:
		cmd=str(OV[pos])
		while len(cmd)<5:cmd="0"+cmd
		opcode=int(cmd[-2:])
		ic,ib,ia=map(int,cmd[:3])
		# ~ print("position",pos,TV[pos],"opcode:",opcode,"flags:",ic,ib,ia)
		match opcode:
			case 1:
				# ~ 3parameters
				pa,pb,pc=OV[pos+1:pos+4]
				# ~ print(pa,pb,pc)
				s=(pa if ia else OV[pa]) + (pb if ib else OV[pb])
				# ~ print(s)
				OV[pc]=s
				# ~ print(OV)
				pos+=4
			case 2:
				# ~ 3parameters
				pa,pb,pc=OV[pos+1:pos+4]
				# ~ print(pa,pb,pc)
				s=(pa if ia else OV[pa]) * (pb if ib else OV[pb])
				# ~ print(s)
				OV[pc]=s
				# ~ print(OV)
				pos+=4
			case 3:
				pa=OV[pos+1]
				OV[pa]=inp
				pos+=2
				# ~ print(OV)
			case 4:
				pa=OV[pos+1]
				print("out:",pa,OV[pa])
				pos+=2
			case 99:
				# ~ print("returning")
				# ~ print()
				return OV[0]
treat("1101,100,-1,4,0")
# ~ exit()
for line in open(fn).read().splitlines()[:2]:
	treat(line)
# ~ print("1002"[-2:])
# ~ print("002"[-2:])
# ~ print("02"[-2:])
# ~ print("2"[-2:])
