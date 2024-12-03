#!/usr/bin/env python
# -*- coding: utf-8 -*-
fn,part="d9.txt",0
from  intcode import computer
d=(109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99)
# ~ d=(109,19,204,-34)
c=computer(d)
# ~ c.rb=2000
for v in c.flow:print(v)
c=computer((1102,34915192,34915192,7,4,7,99,0))
for v in c.flow:print(v)
for v in computer((104,1125899906842624,99)).flow:print(v)
# ~ exit()
da=open(fn).readline().strip()
st=0
while True:
	c=computer(da)
	c.inp.append(st)
	res=0
	for v in c.flow:
		print(st,v)
		res+=1
	if res==1:
		print(st)
		input()
	st+=1
