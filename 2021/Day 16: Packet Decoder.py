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
def getbs(line):
	r=bin(int(line,16))[2:]
	while len(r)%4:r="0"+r
	print(r)
	return r

def treat(r,lvl=1):
	global ttv
	decal=" ="*lvl
	print(decal,r)
	pv,r=int(r[:3],2),r[3:]
	print(decal,"pv",pv)
	ptid,r=int(r[:3],2),r[3:]
	ttv+=pv
	if ptid==4:
		tex=""
		while True:
			a,b,r=r[0],r[1:5],r[5:]
			tex+=b
			if a=="0":break
		print(" ="*lvl,"lv:",int(tex,2))
		return r
	else:
		ltid,r=r[0],r[1:]
		if ltid=="1":
			nsp,r=int(r[:11],2),r[11:]
			print(decal,"nsp",nsp)
			for sp in range(nsp):
				r=treat(r,lvl+1)
			return r
		else:
			ttlb,r=int(r[:15],2),r[15:]
			print(decal,ttlb)
			tex,r=r[:ttlb],r[ttlb:]
			while tex:
				tex=treat(tex,lvl+1)
			return r
ttv=0
for line in open(fn).read().splitlines()[7:]:
# ~ for line in open(fn).read().splitlines():
	print(line)
	print(treat(getbs(line)))
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
