#!/usr/bin/env python
# -*- coding: utf-8 -*-
fn,part="d5.txt",0
def treat(line,inp=1):
	TV=line.split(",")
	OV=list(map(int,TV))
	pos=0
	print(OV,inp)
	while True:
		cmd=str(OV[pos])
		while len(cmd)<5:cmd="0"+cmd
		opcode=int(cmd[-2:])
		ic,ib,ia=map(int,cmd[:3])
		# ~ print("position",pos,OV[pos:pos+4],"opcode:",opcode,"flags:",ic,ib,ia)
		match opcode:
			case 1:
				# ~ 3parameters
				pa,pb,pc=OV[pos+1:pos+4]
				# ~ print(pa,pb,pc)
				s=(pa if ia else OV[pa]) + (pb if ib else OV[pb])
				# ~ print(s)
				OV[pc]=s
				# ~ print(OV)
				if pc!=pos:pos+=4
			case 2:
				# ~ 3parameters
				pa,pb,pc=OV[pos+1:pos+4]
				# ~ print(pa,pb,pc)
				s=(pa if ia else OV[pa]) * (pb if ib else OV[pb])
				# ~ print(s)
				OV[pc]=s
				# ~ print(OV)
				if pc!=pos:pos+=4
			case 3:
				pa=OV[pos+1]
				OV[pa]=inp
				if pa!=pos:pos+=2
				# ~ print(OV)
			case 4:
				pa=OV[pos+1]
				pa=pa if ia else OV[pa]
				# ~ print("out:",pa,OV[pa])
				print("out:",pa)
				pos+=2
			case 5:
				pa=OV[pos+1]
				pa=pa if ia else OV[pa]
				if pa:
					pb=OV[pos+2]
					pb=pb if ib else OV[pb]
					pos=pb
				else:pos+=3
			case 6:
				pa=OV[pos+1]
				pa=pa if ia else OV[pa]
				if not pa:
					pb=OV[pos+2]
					pb=pb if ib else OV[pb]
					pos=pb
				else:pos+=3
			case 7:
				pa=OV[pos+1]
				pb=OV[pos+2]
				pc=OV[pos+3]
				pa=pa if ia else OV[pa]
				pb=pb if ib else OV[pb]
				if pa<pb:
					pc=OV[pos+3]
					# ~ pc=pc if ic else OV[pc]
					OV[pc]=1
				else:OV[pc]=0
				if pc!=pos:pos+=4
			case 8:
				pa=OV[pos+1]
				pb=OV[pos+2]
				pc=OV[pos+3]
				pa=pa if ia else OV[pa]
				pb=pb if ib else OV[pb]
				if pa==pb:
					pc=OV[pos+3]
					# ~ pc=pc if ic else OV[pc]
					OV[pc]=1
				else:OV[pc]=0
				if pc!=pos:pos+=4
			case 99:
				# ~ print("returning")
				# ~ print()
				return OV[0]
for x in range(1,15):
	# ~ treat("3,9,8,9,10,9,4,9,99,-1,8",x)
	# ~ treat("3,9,7,9,10,9,4,9,99,-1,8",x)
	# ~ treat("3,3,1108,-1,8,3,4,3,99",x)
	# ~ treat("3,3,1107,-1,8,3,4,3,99",x)
	# ~ treat("3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9",x)
	# ~ treat("3,3,1105,-1,9,1101,0,0,12,4,12,99,1",x)
	treat("3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99",x)
# ~ exit()
for line in open(fn).read().splitlines()[:2]:
	treat(line,5)
# ~ print("1002"[-2:])
# ~ print("002"[-2:])
# ~ print("02"[-2:])
# ~ print("2"[-2:])
