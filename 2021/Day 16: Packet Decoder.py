#!/usr/bin/env python
# -*- coding: utf-8 -*-
part=0

import re
import sys
import itertools as it
from functools import cache
import uuid
cp=str(sys.argv[0])
dre=re.compile(r"^Day (\d+):")
day=dre.findall(cp)[0]
fn=f"d{day}.txt"
# ~ block=open(fn).read().split("\n\n\n")[part]
# ~ block=open(fn).read().split("\n\n")[part]
def getlitv(s):
	cp=0
	tv=""
	while True:
		tv+=s[cp+1:cp+5]
		if s[cp]=="0":break
		cp+=5
	print("lit value",int(tv,2),cp+11)
	return cp+11
def op(s):
	if s[0]=="1":
		sp=int(s[1:12],2)
		print("# subpackets",sp)
		cp=0
		for x in range(sp):
			cp+=treat(s[12+cp:])
def treat(bs):
	# ~ pv=int(bs[:3],2)
	# ~ ptid=int(bs[3:6],2)
	x=int(bs[:6],2)
	# ~ print (f"pv: {pv}, ptid: {ptid}")
	# ~ if ptid==4:
	if x&4==4:
		# ~ print (x&4==ptid)
		return getlitv(bs[6:])
	else:
		op(bs[6:])
def res(s):
	h=int(s[:7],2)
	if h&8==8:
		print("litval")
		getlitv(s[6:])
	else:print("operator")

for line in open(fn).read().splitlines()[:-1]:
	res(bin(int(line,16))[2:])
# ~ 110100 lit val
		# ~ 10111	11110	00101	000
# ~ 110100	10111	11110	00101	000
"""
00111000000000000110111101000101001010010001001000000000
001110 op
	  0  > read 15 bits => 27
	   000000000011011 >examine 27 next bits
					  1101000101001010010001001000000000
					  110100
					        01010
					  010100
					        10001
					        00100   0000000
11101110000000001101010000001100100000100011000001100000
111011 op
	  1 > read 11 bits
	   00000000011 > 3 read 3 sub packets
				  01010000001100100000100011000001100000
				  010100 lit value
						00001 >1
				  100100 lit value 
						00010 >2
				  001100 lit value 
						00011 >3
								00000
100010100000000001001010100000000001101010000000000000101111010001111000
100010 op    v 4
		1 >read 11 bits
		 00000000001 > 1 sub packet
					001010 op   v 1
							1 read 11 bits
							 00000000001 > 1 sub packet
										101010 op  v5
											  0 > reads 15 bits
											  000000000001011 > examine 11  next bits
															  110100 lit val  v6
																	01111 > 15   
																			R=000
01100010000000001000000000000000000101100001000101010110001011001000100000000010000100011000111000110100
011000 op v3
      1 >read 11 bits
       00000000010 > 2 sub packets
                  00000000000000000101100001000101010110001011001000100000000010000100011000111000110100
                  000000 op v0
                        0 read 15 bits
                         000000000010110 > examine 22 bits
									    0001000101010110001011:001000100000000010000100011000111000110100
									    0001000101010110001011
									    000100 lit value v0 
									     01010 lv 10 
									    101100 lit value v 5
									     01011 lv 11
				  001000 op v 1 
				   1 read 11 bits 
				    00000000010000100011000111000110100
				    00000000010 >2 sub packets
								:000100 lit val v0 
								  01100 lv 12 
								 :011100 lit val v3
								  01101  lv 13  00


"""
