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
blocks=open(fn).read().split("\n\n")[part]
def tr(i,l):
	return (i%20201227)**l%20201227
cp=tr(7,8)
dp=tr(7,11)
print(tr(dp,8))
print(tr(cp,11))
# ~ 18356117
i=1
c=0
while True:
	i=i*7%20201227
	c+=1
	if i==5909654:break

# ~ 18356117>3974372
# ~ 5909654>8623737


print(c)
print(tr(5909654,3974372))
