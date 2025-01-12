#!/usr/bin/env python3
#
# ~ from functools import cache
from collections import deque
from functools import cache
import itertools as it


tbt=[complex(col,-row) for row in range(2) for col in range(3)]
dip={s:k for s,k in zip(list("XTALDR"),tbt)}
dipdip={}
    # ~ +---+---+
    # ~ | ^ | A |
# ~ +---+---+---+
# ~ | < | v | > |
# ~ +---+---+---+
def alterdp(a,b):
	sa=list("TADR")
	sb=list("LDR")
	sp=dip[a]
	tp=dip[b]
	if (a in sa and b in sa) or (a in sb and b in sb):
		pool=[]
		vd=int(tp.imag-sp.imag)
		sym="D" if vd<0 else "T"
		pool.extend([sym]*abs(vd))
		vc=int(tp.real-sp.real)
		sym="R" if vc>0 else "L"
		pool.extend([sym]*abs(vc))
		if len(pool)==1:
			print(pool,a,b)
			print(pool[0]+"A")
			np=pool[0]+"A"
			v=set([np])
			print(v)
			# ~ exit()
		else:v=set("".join(k)+"A" for k in it.permutations(pool))
		dipdip[sk,tk]=v
for sk in list("TALDR"):
	for tk in list("TALDR"):
		alterdp(sk,tk)
dipdip["T","L"]=set("D"+k for k in dipdip["D","L"])
dipdip["A","L"]=set("L"+k for k in dipdip["T","L"])|set("D"+k for k in dipdip["R","L"])
dipdip["L","T"]=set("R"+k for k in dipdip["D","T"])
dipdip["L","A"]=set("R"+k for k in dipdip["D","A"])

for k,v in dipdip.items():
	print(k,v)
