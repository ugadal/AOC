#!/usr/bin/env python
# -*- coding: utf-8 -*-
Boxes=open("d2.txt").read().splitlines()
# ~ qysdgimlcaghpfozuwejmhrbvx
two=three=0
for bid in Boxes:
	alpha=set(list(bid))
	dec=[bid.count(s) for s in alpha]
	if dec.count(2):two+=1
	if dec.count(3):three+=1
print (two*three)
