#!/usr/bin/env python
# -*- coding: utf-8 -*-
def calc(n,ne,se):
	r=float("inf")
	if n<0:n,ne,se=-n,-ne,-se
	if [n,ne,se].count(0)>=2:r=n+ne+se
	elif n*se>0:r=n+ne+se-min(n,se)
	elif n*se<0:r=n+ne-se-min(n,-se)
	elif n*ne<0:r=n-ne+se-min(n,-ne)
	print(n,ne,se,abs(r))

# ~ p1:

n=ne=se=0
V=open("d11.txt").read().strip().split(",")
for v in V:
	match v:
		case 'ne':ne+=1
		case 'se':se+=1
		case 'nw':se-=1
		case 'sw':ne-=1
		case 'n':n+=1
		case 's':n-=1
	calc(n,ne,se)
print(f"N:{n} NE:{ne}  SE:{se}")
# ~ N:-403 NE:-405  SE:-79
# ~ <=>
# ~ N 403 NE 405 SE 79  -79 N,SE +79 NE
  # ~ 324    484    0
# ~ n-se+n+ne
# ~ p2:
n=ne=se=0
" | sort -nk 4"
