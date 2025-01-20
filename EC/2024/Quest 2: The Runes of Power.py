#!/usr/bin/env python3
#
import re
fn="everybody_codes_e2024_q02_p1.txt"
wd,txt=open(fn).read().split("\n\n")
# ~ print(wd)
wd=wd.split(":")[1].split(",")
# ~ print(wd)
R=[re.compile(s) for s in wd]
tt=0
for r in R:
	tt+=len(r.findall(txt))
# ~ print(tt)
fn="everybody_codes_e2024_q02_p2.txt"
# ~ fn="t.txt"
wd,txt=open(fn).read().split("\n\n")
# ~ print(wd)
wd=wd.split(":")[1].split(",")
# ~ print(wd)
tt=0
# ~ print(txt)
R=[]
for s in wd:
	R.append(re.compile(s))
	t=list(s)
	t.reverse()
	t="".join(t)
	R.append(re.compile(t))
# ~ R=[re.compile(s) for s in wd]
for l in txt.splitlines():
	# ~ print(l)
	s=set()
	for r in R:
		# ~ print(r)
		pos=0
		sr=r.search(l,pos)
		while sr:
			# ~ print(sr)
			for x in range (sr.start(),sr.end()):s.add(x)
			pos=sr.start()+1
			sr=r.search(l,pos)
	# ~ print(s,len(s))
	tt+=len(s)
print(tt)
