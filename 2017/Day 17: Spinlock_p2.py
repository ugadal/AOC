#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ~ L=[0]
# ~ p=0
# ~ cyc=0
# ~ pv=None
# ~ for r in range(51):
	# ~ for x in range(100000):
		# ~ cyc+=1
		# ~ p+=344
		# ~ p%=len(L)
		# ~ L.insert(p+1,cyc)
		# ~ p+=1
		# ~ v=L.index(0)
		# ~ cv=L[1]
		# ~ if cv!=pv:
			# ~ print(cyc,cv)
			# ~ pv=cv
		# ~ print(cyc,cv)
	# ~ v=L.index(0)
	# ~ cv=L[v+1]
	# ~ print(v,cyc,cv)
# ~ 1 1
# ~ 7 7
# ~ 14 14
# ~ 15 15
# ~ 89 89
# ~ 246 246
# ~ 2344 2344
# ~ 2726 2726
# ~ 5935 5935
# ~ 10545 10545
# ~ 41867 41867
# ~ 45544 45544
# ~ 187773 187773
# ~ 474004 474004

ll=1
p=0
while True:
	p+=344
	p%=ll
	p+=1
	p%=(ll+1)
	ll+=1
	if p==1: print (ll-1)
# ~ 187773
# ~ 474004
# ~ 1898341
# ~ 111771339   <- yuck pypy in a few seconds.. over 50e6	
