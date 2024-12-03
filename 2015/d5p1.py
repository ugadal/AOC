#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ~ import sympy
import re
letters=[chr(c) for c in range(97,123)]
tv=re.compile("a|e|i|o|u")
dd=[re.compile(s+s) for s in letters]
fbn=[re.compile(s) for s in "ab, cd, pq, xy".split(", ")]
count=0
for line in open(0).read().splitlines():
	# ~ print(line)
	# ~ print("vowels",len(tv.findall(line)))
	# ~ print("double letters",[d.search(line) for d in dd])
	# ~ print("forbidden",[d.search(line) for d in fbn])
	if len(tv.findall(line))<3:continue
	if not any([d.search(line) for d in dd]):continue
	if any ([d.search(line) for d in fbn]):continue
	count+=1
	print(line,"ok")
print(count)

	
