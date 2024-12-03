#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ~ import sympy
import re
NOT=re.compile("^NOT (\w+)")
OR=re.compile("(\w+) OR (\w+)")
fixed=re.compile("^(\d+)$")
AND=re.compile("(\w+) AND (\w+)")
RS=re.compile("(\w+) RSHIFT (\d+)")
LS=re.compile("(\w+) LSHIFT (\d+)")
K={}
K['1']=1
I={}
instructions=open(0).read().splitlines()
for inst in instructions:
	what,target=inst.split(" -> ")
	if NOT.match(what):I[target]=f"65535 ^ K['{NOT.search(what).groups()[0]}']"
	elif OR.match(what):
		a,b=OR.search(what).groups()
		I[target]=f"K['{a}'] | K['{b}']"
	elif fixed.match(what):
		a=fixed.search(what).groups()[0]
		I[target]=a
	elif AND.match(what):
		a,b=AND.search(what).groups()
		I[target]=f"K['{a}'] & K['{b}']"
	elif RS.match(what):
		a,b=RS.search(what).groups()
		I[target]=f"K['{a}']>>{b}"
	elif LS.match(what):
		a,b=LS.search(what).groups()
		I[target]=f"K['{a}']<<{b}"
	else:
		print(inst)
for k,v in I.items():
	print (v,":",k)
print(len(I))
while "lx" not in K:
	print("iter")
	changed=False
	for k in I.keys():
		if k in K:continue
		print("trying",k,I[k])
		try:
			v=eval(I[k])
			K[k]=v
			changed=True
			print(I[k],"ok",k)
		except:
			print(I[k],"failed")
			continue
	if not changed:break
print(K)
	
