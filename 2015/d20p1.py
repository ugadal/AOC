#!/usr/bin/env python
# -*- coding: utf-8 -*-
lim=2900000
house=737100
# ~ R=[]
g=0
def sd(n):
	g=0
	for m in range(1,n+1):
		if n%m==0:g+=m
	return g,g>lim
# ~ 665280/2/2/2/2/2/2/3/3/3/5/7/11
