#!/usr/bin/env python3
#
import re
fn="everybody_codes_e2024_q02_p1.txt"
wd,txt=open(fn).read().split("\n\n")
wd=wd.split(":")[1].split(",")
R=[re.compile(s) for s in wd]
tt=0
for r in R:
	tt+=len(r.findall(txt))
# ~ P2
fn="everybody_codes_e2024_q02_p2.txt"
wd,txt=open(fn).read().split("\n\n")
wd=wd.split(":")[1].split(",")
tt=0
R=[]
for s in wd:
	R.append(re.compile(s))
	t=list(s)
	t.reverse()
	t="".join(t)
	R.append(re.compile(t))
for l in txt.splitlines():
	s=set()
	for r in R:
		pos=0
		sr=r.search(l,pos)
		while sr:
			for x in range (sr.start(),sr.end()):s.add(x)
			pos=sr.start()+1
			sr=r.search(l,pos)
	tt+=len(s)
print(tt)
# ~ P3
fn="everybody_codes_e2024_q02_p3.txt"
fn="t.txt"
wd,txt=open(fn).read().split("\n\n")
wd=wd.split(":")[1].split(",")
R=[]
for s in wd:
	R.append(re.compile(s))
	t=list(s)
	t.reverse()
	t="".join(t)
	R.append(re.compile(t))
txt=txt.splitlines()
NR=len(txt)
NC=len(txt[0])
tt=0
for l in txt:
	s=set()
	print(l)
	for r in R:
		print(r)
		pos=0
		tl=l+l[:len(r.pattern)-1]
		sr=r.search(tl,pos)
		while sr:
			print(sr)
			for x in range (sr.start(),sr.end()):s.add(x)
			pos=sr.start()+1
			sr=r.search(tl,pos)
	tt+=len(s)
for r in txt:print(r)
txt=list(map(lambda x:"".join(x),zip(*txt)))
