#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ~ import sympy
tf=open("d8.txt")
tb=open("d8.txt",'rb')
s=r''
'''

""
"abc"
"aaa\"aaa"
"\x27"

'''
ttl=0
tte=0
i=0
while True:
	i+=1
	c=tb.read(1)
	print(i,c,c.decode())
	if c.decode()=='"':
		ttl+=1
		tte+=2
		continue
	if c==b'\n':
		# ~ ttl+=1
		tte+=2 #surrounding quotes to count
		# ~ print (ttl,tte)
		continue
	if c.decode()=='\\':
		ttl+=1
		tte+=2
	if c==b"":break
print(tte-ttl)
