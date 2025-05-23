#!/usr/bin/env python
# -*- coding: utf-8 -*-
fn,part="d2.txt",1
data=open(fn).read().split("\n\n")[part].splitlines()
import re
extract=re.compile(r"(\d+)-(\d+) (\S): (\S+)")
okp1=0
okp2=0
for line in data:
	mi,ma,s,pw=extract.findall(line)[0]
	mi=int(mi)
	ma=int(ma)
	c=pw.count(s)
	if c>=mi and c<=ma:okp1+=1
	if pw[mi-1]==s and pw[ma-1]!=s:okp2+=1
	elif pw[mi-1]!=s and pw[ma-1]==s:okp2+=1
print(okp1)
print(okp2)
