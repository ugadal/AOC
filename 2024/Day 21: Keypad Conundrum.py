#!/usr/bin/env python3
#
from functools import cache
from collections import deque
import itertools as it
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
kpkp={}
for sk in list("0A235689"):
	for tk in list("0A235689"):
		sp=kp[sk]
		tp=kp[tk]
		pool=[]
		vd=int(tp.imag-sp.imag)
		sym="v" if vd>0 else "^"
		pool.extend([sym]*abs(vd))
		vc=int(tp.real-sp.real)
		sym=">" if vc>0 else "<"
		pool.extend([sym]*abs(vc))
		if len(pool)==1:v=set(pool)
		else:v=set("".join(k) for k in it.permutations(pool))
		kpkp[sk,tk]=v
for sk in list("235689"):
	for tk in list("741"):
		sp=kp[sk]
		tp=kp[tk]
		pool=[]
		vd=int(tp.imag-sp.imag)
		sym="v" if vd>0 else "^"
		pool.extend([sym]*abs(vd))
		vc=int(tp.real-sp.real)
		sym=">" if vc>0 else "<"
		pool.extend([sym]*abs(vc))
		if len(pool)==1:v=set(pool)
		else:v=set("".join(k) for k in it.permutations(pool))
		kpkp[sk,tk]=v
for sk in list("741"):
	for tk in list("235689"):
		sp=kp[sk]
		tp=kp[tk]
		pool=[]
		vd=int(tp.imag-sp.imag)
		sym="v" if vd>0 else "^"
		pool.extend([sym]*abs(vd))
		vc=int(tp.real-sp.real)
		sym=">" if vc>0 else "<"
		pool.extend([sym]*abs(vc))
		if len(pool)==1:
			v=set(pool)
		else:
			v=set("".join(k) for k in it.permutations(pool))
		kpkp[sk,tk]=v
# ~ for k,p in kpkp.items():
	# ~ print(k,p)
# ~ print(kpkp["2","0"])
kpkp["1","0"]=set(">"+k for k in kpkp["2","0"])
kpkp["1","A"]=set(">"+k for k in kpkp["2","A"])
kpkp["4","0"]=set(">"+k for k in kpkp["5","0"])|set("v"+k for k in kpkp["1","0"])
kpkp["4","A"]=set(">"+k for k in kpkp["5","A"])|set("v"+k for k in kpkp["1","A"])
kpkp["7","0"]=set(">"+k for k in kpkp["8","0"])|set("v"+k for k in kpkp["4","0"])
kpkp["7","A"]=set(">"+k for k in kpkp["8","A"])|set("v"+k for k in kpkp["4","A"])
kpkp["0","1"]=set("^"+k for k in kpkp["2","1"])
kpkp["0","4"]=set("^"+k for k in kpkp["2","4"])
kpkp["0","7"]=set("^"+k for k in kpkp["2","7"])
kpkp["A","1"]=set("^"+k for k in kpkp["3","1"])|set("<"+k for k in kpkp["0","1"])
kpkp["A","4"]=set("^"+k for k in kpkp["3","4"])|set("<"+k for k in kpkp["0","4"])
kpkp["A","7"]=set("^"+k for k in kpkp["3","7"])|set("<"+k for k in kpkp["0","7"])
for k,p in kpkp.items():
	print(k,p)


# ~ print(kpkp)
exit()
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
s=0
for p in ["029A","980A","179A","456A","379A"]:
# ~ for p in open(fn).read().splitlines():
	f=int(p[:-1])
	p=genkppath(p)
	print(len(p),p)
	p=gendippath(p)
	print(len(p),p)
	p=gendippath(p)
	print(len(p),p)
	s+=len(p)*f
	print()
print(s)
# ~ 179982 too high 
# ~ <v<A >>^A vA ^A <vA <AA >>^AA vA <^A >AA vA ^A <vA >^AA <A >A <v<A >A >^AAA vA <^A >A
# ~ <    A    >  A  v   <<  AA    >  ^   AA  >  A  v   AA   ^  A  <    v  AAA   >  ^   A
# ~ <A  >A  v<<AA >^AA >A vAA ^A <vAAA >^A
# ~ ^   A   <<    ^^   A  >>  A  vvv   A
# ~ 3       7             9            A  

# ~ ^A^^<<A>>AvvvA
# ~ ^A<<^^A>>AvvvA

# ~ <A>A<AAv<AA>>^AvAA^Av<AAA^>A
# ~ <A>Av<<AA>^AA>AvAA^A<vAAA>^A ! better to reencode

# ~ v<<A>>^AvA^Av<<A>>^AAv<A<A>>^AAvAA^<A>Av<A^>AA<A>Av<A<A>>^AAA<Av>A^A
# ~ <v<A>>^AvA^A<vA<AA>>^AAvA<^A>AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A
