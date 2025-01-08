#!/usr/bin/env python3
#
# ~ from functools import cache
from collections import deque
from functools import cache
import itertools as it
sep="\n\n"
fn,part="d21.txt",0

tbt=[complex(col,-row) for row in range(4) for col in range(3)]
NKsp={s:k for s,k in zip(list("X0A123456789"),tbt)}
NKps={k:s for s,k in zip(list("X0A123456789"),tbt)}
NKpaths={}
		
def alterkpkp(a,b):
	sa=list("789456123")
	sb=list("8956230A")
	if (a in sa and b in sa) or (a in sb and b in sb):
		sp=NKsp[a]
		tp=NKsp[b]
		pool=[]
		vd=int(tp.imag-sp.imag)
		if vd:
			sym="D" if vd>0 else "T"
			pool.extend([sym]*abs(vd))
		vc=int(tp.real-sp.real)
		if vc:
			sym="R" if vc>0 else "L"
			pool.extend([sym]*abs(vc))
		if len(pool)==1:v=set(pool)
		else:v=set("".join(k) for k in it.permutations(pool))
		NKpaths[sk,tk]=v
		# ~ if a==b:kpkp[sk,tk]=["A"]
for sk in list("0A123456789"):
	for tk in list("0A123456789"):
		alterkpkp(sk,tk)
NKpaths["1","0"]=set("R"+k for k in NKpaths["2","0"])
NKpaths["1","A"]=set("R"+k for k in NKpaths["2","A"])
NKpaths["4","0"]=set("R"+k for k in NKpaths["5","0"])|set("D"+k for k in NKpaths["1","0"])
NKpaths["4","A"]=set("R"+k for k in NKpaths["5","A"])|set("D"+k for k in NKpaths["1","A"])
NKpaths["7","0"]=set("R"+k for k in NKpaths["8","0"])|set("D"+k for k in NKpaths["4","0"])
NKpaths["7","A"]=set("R"+k for k in NKpaths["8","A"])|set("D"+k for k in NKpaths["4","A"])
NKpaths["0","1"]=set("T"+k for k in NKpaths["2","1"])
NKpaths["0","4"]=set("T"+k for k in NKpaths["2","4"])
NKpaths["0","7"]=set("T"+k for k in NKpaths["2","7"])
NKpaths["A","1"]=set("T"+k for k in NKpaths["3","1"])|set("L"+k for k in NKpaths["0","1"])
NKpaths["A","4"]=set("T"+k for k in NKpaths["3","4"])|set("L"+k for k in NKpaths["0","4"])
NKpaths["A","7"]=set("T"+k for k in NKpaths["3","7"])|set("L"+k for k in NKpaths["0","7"])


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
		if len(pool)==1:v=set(pool)
		else:v=set("".join(k) for k in it.permutations(pool))
		dipdip[sk,tk]=v
for sk in list("TALDR"):
	for tk in list("TALDR"):
		alterdp(sk,tk)
dipdip["T","L"]=set("D"+k for k in dipdip["D","L"])
dipdip["A","L"]=set("L"+k for k in dipdip["T","L"])|set("D"+k for k in dipdip["R","L"])
dipdip["L","T"]=set("R"+k for k in dipdip["D","T"])
dipdip["L","A"]=set("R"+k for k in dipdip["D","A"])


def genkppath(code):
	fc=[]
	sp="A"
	for t in code:
		fc.append(NKpaths[sp,t])
		fc.append(["A"])
		sp=t
	return list("".join(p) for p in it.product(*fc))
    # ~ +---+---+
    # ~ | ^ | A |
# ~ +---+---+---+
# ~ | < | v | > |
# ~ +---+---+---+
# ~ print(genkppath("083A"))


# ~ exit()
# ~ I=[("LATATTRADDDA",29),("TTTALADDDARA",980),("TLLATTARRADDDA",179),("TTLLARARADDA",456),("TALLTTARRADDDA",379)]
# ~ I=[("TTLLARATRADDDA",459),("TTALLTADDARRDA",671),("LTTTADLARRADDA",846),("LTATTADARDA",285),("LATTTADDRADA",83)]
d={}
d[("AT")]="LA"
d[("AR")]="DA"
d[("AD")]="DLA"
d[("AL")]="DLLA"
d[("TA")]="RA"
d[("TR")]="DRA"
d[("TD")]="DA"
d[("TL")]="DLA"
d[("RA")]="TA"
d[("RT")]="TLA"
d[("RD")]="LA"
d[("RL")]="LLA"
d[("DA")]="TRA"
d[("DT")]="TA"
d[("DR")]="RA"
d[("DL")]="LA"
d[("LA")]="RRTA"
d[("LT")]="RTA"
d[("LR")]="RRA"
d[("LD")]="RA"
d[("LL")]="A"
d[("TT")]="A"
d[("RR")]="A"
d[("AA")]="A"
d[("DD")]="A"
@cache
def solve(path,inter):
	if inter==0:return len(path)
	T=[d[a+b] for a,b in zip("A"+path,path)]
	return sum(solve(t,inter-1) for t in T)
# ~ print(solve("LATATTRADDDA",2))
tot=0
# ~ for tt in ["029A","980A","179A","456A","379A"]:
for tt in ["459A","671A","846A","285A","083A"]:
	tmi=min(solve(i,25) for i in genkppath(tt))
	print(tt,tmi,tmi*int(tt[:-1]))
	tot+=tmi*int(tt[:-1])
		# ~ p=solve(i,2)
		# ~ tt+=p*v
		# ~ print(i,p)
print(tot)
print (solve.cache_info())
# ~ 386161112405476 too high
