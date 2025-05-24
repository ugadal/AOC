#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import sys
cp=str(sys.argv[0])
dre=re.compile(r"^Day (\d+):")
day=dre.findall(cp)[0]
fn,part=f"d{day}.txt",1
data=list(map(int,open(fn).read().split("\n\n")[part].splitlines()))
data.sort()
data.insert(0,0)
data.append(data[-1]+3)
delta=[b-a for a,b in zip(data,data[1:])]
print("p1:",delta.count(1)*delta.count(3))
