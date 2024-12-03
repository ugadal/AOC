#!/usr/bin/env python3
#
fn,part="d3.txt",1
data=open(fn).read().split("\n\n")[part]
print(data)
import re
er=re.compile("mul\\((\\d+,\\d+)\\)")
res=0
for block in er.findall(data):
	a,b=map(int,block.split(","))
	res+=a*b
print(res)
