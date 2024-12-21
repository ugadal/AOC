#!/usr/bin/env python3
#
# ~ from functools import cache
from collections import deque
sep="\n\n"
fn,part="d21.txt",0

# ~ +---+---+---+
# ~ | 7 | 8 | 9 |
# ~ +---+---+---+
# ~ | 4 | 5 | 6 |
# ~ +---+---+---+
# ~ | 1 | 2 | 3 |
# ~ +---+---+---+
    # ~ | 0 | A |
    # ~ +---+---+
tbt=[complex(col,-row) for row in range(4) for col in range(3)]
kp={s:k for s,k in zip(list("X0A123456789"),tbt)}
print(kp)
tbt=[complex(col,-row) for row in range(2) for col in range(3)]
dip={s:k for s,k in zip(list("<v>X^A"),tbt)}
print(dip)
def genkppath(code):
	fc=[]
	sp=kp["A"]
	for t in code:
		tk=kp[t]
		if sp.real==0:
			vc=tk.real-sp.real
			if vc:
				s=">"# if vc>0 else "<"
				fc.extend([s]*int(abs(vc)))		
			vd=tk.imag-sp.imag
			if vd:
				s="^" if vd<0 else "v"
				fc.extend([s]*int(abs(vd)))
		elif tk.real==0:
			vd=tk.imag-sp.imag
			if vd:
				s="^" if vd<0 else "v"
				fc.extend([s]*int(abs(vd)))
			vc=tk.real-sp.real
			if vc:
				s=">" if vc>0 else "<"
				fc.extend([s]*int(abs(vc)))		
		else:
			vd=tk.imag-sp.imag
			if vd:
				s="^" if vd<0 else "v"
				fc.extend([s]*int(abs(vd)))
			vc=tk.real-sp.real
			if vc:
				s=">" if vc>0 else "<"
				fc.extend([s]*int(abs(vc)))		
		fc.append("A")
		sp=tk
	res="".join(fc)
	return res
    # ~ +---+---+
    # ~ | ^ | A |
# ~ +---+---+---+
# ~ | < | v | > |
# ~ +---+---+---+
def gendippath(code):
	fc=[]
	sp=dip["A"]
	for t in code:
		tk=dip[t]
		if sp.real==0:
			vc=tk.real-sp.real
			# ~ if vc:
			s=">" # if vc>0 else "<"
			if vc:fc.extend([s]*int(abs(vc)))		
			vd=tk.imag-sp.imag
			if vd:
				s="^" if vd<0 else "v"
				fc.extend([s]*int(abs(vd)))
		elif tk.real==0:
			vd=tk.imag-sp.imag
			if vd:
				s="^" if vd<0 else "v"
				fc.extend([s]*int(abs(vd)))
			vc=tk.real-sp.real
			if vc:
				s=">" if vc>0 else "<"
				fc.extend([s]*int(abs(vc)))		
		else:
			vd=tk.imag-sp.imag
			if vd:
				s="^" if vd<0 else "v"
				fc.extend([s]*int(abs(vd)))
			vc=tk.real-sp.real
			if vc:
				s=">" if vc>0 else "<"
				fc.extend([s]*int(abs(vc)))		
		fc.append("A")
		sp=tk
	res="".join(fc)
	return res

# ~ for p in ["029A","980A","179A","456A","379A"]:
s=0
for p in open(fn).read().splitlines():
	f=int(p[:-1])
	p=genkppath(p)
	p=gendippath(p)
	p=gendippath(p)
	s+=len(p)*f
print(s)
# ~ 179982 too high 
