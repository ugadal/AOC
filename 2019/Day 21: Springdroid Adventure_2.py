#!/usr/bin/env python
# -*- coding: utf-8 -*-
fn,part="d21.txt",0
from functools import cache
from intcodegen import computer
import itertools as it
pgm=open(fn).readline().strip()
c=computer(pgm)
c.inp.extend([*map(ord,"""OR A J
AND B J
AND C J
NOT J J
AND D J
OR E T
OR H T
AND T J
""")])
c.inp.extend([*map(ord,"RUN\n")])
for v in c.flow:
	try:print(chr(v),end="")
	except:print(v)
