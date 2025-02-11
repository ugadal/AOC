#!/usr/bin/env python
# -*- coding: utf-8 -*-
fn,part="d22.txt",0
from functools import cache
from intcodegen import computer
import itertools as it
pgm=open(fn).read().splitlines()
ld=10007
sp=2019
for line in pgm:
	match line.split():
		case ['deal','with','increment',*arg]:
			inc=int(arg[0])
			sp=(sp*inc)%ld
		case ["deal","into","new","stack"]:
			sp=ld-sp-1
		case ["cut",*arg]:
			cp=int(arg[0])
			sp-=cp
			sp=sp%ld
print (sp)
