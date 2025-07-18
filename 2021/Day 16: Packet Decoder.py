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
def getlitv(s,lvl=1):
	print("="*lvl,s)
	global ttv
	cp=0
	tv=""
	while True:
		tv+=s[cp+1:cp+5]
		if s[cp]=="0":break
		cp+=5
		print(tv,len(tv)*5//4)
	print(tv,len(tv)*5//4)
	print("lit value",int(tv,2),cp+5)
	return cp+5
def op(s,lvl=0):
	if s[0]=="1":
		sp=int(s[1:12],2)
		print("# subpackets",sp)
		cp=0
		for x in range(sp):
			cp+=res(s[12+cp:])
	else:
		tex=int(s[1:16],2)
		print("examine next",tex,s[16:16+tex])
		res(s[16:16+tex],lvl+1)
def res(s,lvl=1):
	print("res","="*lvl,s)
	global ttv
	pv=int(s[:3],2)
	ptid=int(s[3:6],2)
	if ptid==4:
		print("litval")
		ttv+=pv
		return 6+getlitv(s[6:],lvl+1)
	else:
		print("operator")
		return op(s[6:],lvl+1)
def getbs(line):
	r=bin(int(line,16))[2:]
	while len(r)%4:r="0"+r
	print(r)
	return r
ttv=0
for line in open(fn).read().splitlines()[:2]:
# ~ for line in open(fn).read().splitlines():
	print(line)
	print(res(getbs(line)))
print("ttv:",ttv)
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
