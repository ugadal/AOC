#!/usr/bin/env python3
#
import re
fn="everybody_codes_e2024_q02_p1.txt"
wd,txt=open(fn).read().split("\n\n")
print(wd)
wd=wd.split(":")[1].split(",")
print(wd)
R=[re.compile(s) for s in wd]
tt=0
for r in R:
	tt+=len(r.findall(txt))
print(tt)
fn="everybody_codes_e2024_q02_p2.txt"
wd,txt=open(fn).read().split("\n\n")
print(wd)
wd=wd.split(":")[1].split(",")
print(wd)
tt=0
print(txt)
R=[re.compile(s) for s in wd]
for r in R:
	tt+=print(r.findall(txt))
