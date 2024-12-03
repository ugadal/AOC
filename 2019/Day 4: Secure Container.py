#!/usr/bin/env python
# -*- coding: utf-8 -*-
a,b=307237,769058
# ~ fn,part="d3.txt",3
solc=0
def valid(x):
	L=[int(c) for c in str(x)]
	if any(x>y for x,y in zip(L,L[1:])):return 0
	if not any(x==y for x,y in zip(L,L[1:])):return 0
	duet=0
	while L:
		cs=L.pop()
		cc=1
		while L and L[-1]==cs:
			L.pop()
			cc+=1
		if cc==2:return True
	return False
print(valid(112233))
print(valid(123444))
print(valid(111122))
print(valid(113333))
print(valid(3333444455556666))
print(valid(333344445555666677))
print (sum(1 if valid(x) else 0 for x in range(a,b+1)))
