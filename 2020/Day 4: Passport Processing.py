#!/usr/bin/env python
# -*- coding: utf-8 -*-
fn,part="d4.txt",1
data=open(fn).read().split("\n\n\n")[part]
pp=data.split("\n\n")
nk="byr,iyr,eyr,hgt,hcl,ecl,pid".split(",")
oks=0
for p in pp:
	K={}
	for line in p.splitlines():
		for part in line.split():
			k,v=part.split(":")
			K[k]=v
	if any(k not in K for k in nk):continue
	v=int(K["byr"])
	if v<1920 or v>2002:continue
	v=int(K["iyr"])
	if v<2010 or v>2020:continue
	v=int(K["eyr"])
	if v<2020 or v>2030:continue
	v=K["hgt"]
	if v.endswith("cm"):
		v=int(v[:-2])
		if v<150 or v>193:continue
	elif v.endswith("in"):
		v=int(v[:-2])
		if v<59 or v>76:continue
	else: continue
	v=K["hcl"]
	if not v.startswith("#"):continue
	if len(v)!=7:continue
	if any (s not in "abcdef0123456789" for s in v[1:]):continue
	if K["ecl"] not in "amb blu brn gry grn hzl oth".split():continue
	if len(K["pid"])!=9:continue
	oks+=1
print(oks)
