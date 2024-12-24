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
tbt=[complex(col,-row) for row in range(2) for col in range(3)]
dip={s:k for s,k in zip(list("X^A<v>"),tbt)}
kpkp={}
def alterkpkp(a,b):
	sa=list("789456123")
	sb=list("8956230A")
	if (a in sa and b in sa) or (a in sb and b in sb):
		sp=kp[a]
		tp=kp[b]
		pool=[]
		vd=int(tp.imag-sp.imag)
		if vd:
			sym="v" if vd>0 else "^"
			pool.extend([sym]*abs(vd))
		vc=int(tp.real-sp.real)
		if vc:
			sym=">" if vc>0 else "<"
			pool.extend([sym]*abs(vc))
		if len(pool)==1:v=set(pool)
		else:v=set("".join(k) for k in it.permutations(pool))
		kpkp[sk,tk]=v
		# ~ if a==b:kpkp[sk,tk]=["A"]
for sk in list("0A123456789"):
	for tk in list("0A123456789"):
		alterkpkp(sk,tk)
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
# ~ for k,v in kpkp.items():print(k,v)
# ~ exit()
dipdip={}
    # ~ +---+---+
    # ~ | ^ | A |
# ~ +---+---+---+
# ~ | < | v | > |
# ~ +---+---+---+
def alterdp(a,b):
	sa=list("^Av>")
	sb=list("<v>")
	sp=dip[a]
	tp=dip[b]
	if (a in sa and b in sa) or (a in sb and b in sb):
		pool=[]
		vd=int(tp.imag-sp.imag)
		sym="v" if vd<0 else "^"
		pool.extend([sym]*abs(vd))
		vc=int(tp.real-sp.real)
		sym=">" if vc>0 else "<"
		pool.extend([sym]*abs(vc))
		if len(pool)==1:v=set(pool)
		else:v=set("".join(k) for k in it.permutations(pool))
		dipdip[sk,tk]=v
for sk in list("^A<v>"):
	for tk in list("^A<v>"):
		alterdp(sk,tk)
dipdip["^","<"]=set("v"+k for k in dipdip["v","<"])
dipdip["A","<"]=set("<"+k for k in dipdip["^","<"])|set("v"+k for k in dipdip[">","<"])
dipdip["<","^"]=set(">"+k for k in dipdip["v","^"])
dipdip["<","A"]=set(">"+k for k in dipdip["v","A"])
# ~ for k,v in dipdip.items():print(k,v)
def genkppath(code):
	fc=[]
	sp="A"
	for t in code:
		fc.append(kpkp[sp,t])
		fc.append(["A"])
		sp=t
	return list("".join(p) for p in it.product(*fc))
    # ~ +---+---+
    # ~ | ^ | A |
# ~ +---+---+---+
# ~ | < | v | > |
# ~ +---+---+---+
print(genkppath("029A"))
# ~ exit()
def gendippath(path):
	fc=[]
	sp="A"
	for t in path:
		fc.append(dipdip[sp,t])
		fc.append(["A"])
		sp=t
	return list("".join(p) for p in it.product(*fc))

# ~ print(gendippath("<A>"))
# ~ exit()

s=0
for p in ["0","029A","980A","179A","456A","379A"]:
# ~ for p in open(fn).read().splitlines():
	# ~ f=int(p[:-1])
	kp=genkppath(p)
	print(len(kp),kp)
	for doloop in range(4):
		dp=set()
		for p in kp: 
			for z in gendippath(p):
				dp.add(z)
		rec=float("inf")
		for p in dp:
			lp=len(p)
			if lp<rec:
				rec=lp
				kept=[]
			if lp==rec:
				kept.append(p)
		kp=kept
	# ~ ndp=set()
	# ~ for p in dp: 
		# ~ for z in gendippath(p):
			# ~ ndp.add(z)
	# ~ print(ndp)
	rec=float("inf")
	for p in kp:
		if len(p)<rec:
			rec=len(p)
	print(rec,p)
	# ~ s+=f*rec
	exit()
print(s)
# ~ 179982 too high 
# ~ <v<A >>^A vA ^A <vA <AA >>^AA vA <^A >AA vA ^A <vA >^AA <A >A <v<A >A >^AAA vA <^A >A
# ~ <    A    >  A  v   <<  AA    >  ^   AA  >  A  v   AA   ^  A  <    v  AAA   >  ^   A
# ~ <A  >A  v<<AA >^AA >A vAA ^A <vAAA >^A
# ~ ^   A   <<    ^^   A  >>  A  vvv   A
# ~ 3       7             9            A  

# ~ ^A^^<<A>>AvvvA
# ~ <A>A<AAv<AA>>^AvAA^Av<AAA^>A
# ~ v<<A>>^AvA^Av<<A>>^AAv<A<A>>^AAvAA^<A>Av<A^>AA<A>Av<A<A>>^AAA<Av>A^A

# ~ ^A<<^^A>>AvvvA
# ~ <A>Av<<AA>^AA>AvAA^A<vAAA>^A ! better to reencode
# ~ <v<A>>^AvA^A<vA<AA>>^AAvA<^A>AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A
