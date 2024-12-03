#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ~ import sympy
import re
letters=[chr(c) for c in range(97,123)]
pairs=[re.compile(a+b) for a in letters for b in letters]
# ~ any([len(p.findall("xyxy"))>=2 for p in pairs])
rep=[re.compile(f"{c}.{c}") for c in letters]
# ~ any([r.search("qjhvhtzxzqqjkmpb") for r in rep])

count=0
for line in open(0).read().splitlines():
	if not any([len(p.findall(line))>=2 for p in pairs]):continue
	if not any([r.search(line) for r in rep]):continue
	count+=1
	print(line,"ok")
print(count)

	
