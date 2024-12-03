#!/usr/bin/env python
# -*- coding: utf-8 -*-
S=list("1321131112")
print(S)
for _ in range(40):
	NS=[]
	p=0
	while p<=len(S)-1:
		sym=S[p]
		tp=p+1
		while tp<len(S)-1 and S[tp]==sym:tp+=1
		count=tp-p
		# ~ print(f"{count}{sym}")
		NS.append(str(count))
		NS.append(sym)
		p=tp
	print("".join(NS))
	S=NS
print(len(S))
