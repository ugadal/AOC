#!/usr/bin/env python3
#
fn="everybody_codes_e2024_q01_p1.txt"
enemies=open(fn).readline().strip()
print(enemies.count("B")+3*enemies.count("C"))
fn="everybody_codes_e2024_q01_p2.txt"
enemies=open(fn).readline().strip()
ttl=0
pos=0
while pos<len(enemies):
	duet=enemies[pos:pos+2]
	extra=0 if duet.count("x") else 2
	ttl+=extra+duet.count("B")+3*duet.count("C")+5*+duet.count("D")
	pos+=2
print(ttl)
fn="everybody_codes_e2024_q01_p3.txt"
enemies=open(fn).readline().strip()
ttl=0
pos=0
while pos<len(enemies):
	duet=enemies[pos:pos+3]
	match duet.count("x"):
		case 0: extra=6
		case 1: extra=2
		case 2: extra=0
		case 3: extra=0
	ttl+=extra+duet.count("B")+3*duet.count("C")+5*+duet.count("D")
	pos+=3
print(ttl)
# ~ 22004
# ~ 19302
# ~ startswith 2 and is 5 symbol
