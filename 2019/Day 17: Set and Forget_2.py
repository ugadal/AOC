#!/usr/bin/env python
# -*- coding: utf-8 -*-
fn,part="d17.txt",0
from intcodegen import computer
pgm=open(fn).readline().strip()
pgm="2"+pgm[1:]
c=computer(pgm)
M={}
row=0
col=0
dirs={"^":-1j,"<":-1,"v":1j,">":1}
tl=-1j
tr=1j
c.inp.extend([*map(ord,"A,C,A,C,B,A,C,B,A,B\n")])
c.inp.extend([*map(ord,"R,6,L,6,L,10\n")]) #A
c.inp.extend([*map(ord,"R,6,L,8,L,10,R,6\n")]) #B
c.inp.extend([*map(ord,"L,8,L,6,L,10,L,6\n")]) #C
c.inp.extend([*map(ord,"n\n")]) #B
for v in c.flow: print(chr(v),end="")
print("==>",v)
