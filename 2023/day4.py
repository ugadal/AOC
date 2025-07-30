#!/usr/bin/env python
# -*- coding: utf-8 -*-

dig=[str(x) for x in range(10)]
ns=dig+["."]
CIDC={}
def indata():
	fn="day4.txt"
	with open(fn) as f:	return f.read().split("\n")
def analine(l):
	if not l:return 0
	cid,remn=l.split(":")
	WinningTxt,MyCardsTxt=remn.split("|")
	WinningNumbers=list(map(int,WinningTxt.split()))
	MyCards=list(map(int,MyCardsTxt.split()))
	winners=[card in WinningNumbers for card in MyCards].count(True)
	if winners:return 2**(winners-1)
	return 0
def secondpart(l):
	if not l:return
	cid,remn=l.split(":")
	thiscid=int(cid.split()[1])
	CIDC[thiscid]=CIDC.get(thiscid,0)+1
	WinningTxt,MyCardsTxt=remn.split("|")
	WinningNumbers=list(map(int,WinningTxt.split()))
	MyCards=list(map(int,MyCardsTxt.split()))
	winners=[card in WinningNumbers for card in MyCards].count(True)
	if winners:
		for c in range(thiscid+1,thiscid+1+winners):
			CIDC[c]=CIDC.get(c,0)+CIDC[thiscid]


def main(args):
	lines=[_.strip() for _ in indata()]
	V=[analine(line) for line in lines]
	print(sum(V))
	for line in lines:secondpart(line)
	print(sum(CIDC.values()))
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
