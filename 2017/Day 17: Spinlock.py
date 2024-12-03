#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ~ (0), the initial state before any insertions.
# ~ 0 (1): the spinlock steps forward three times (0, 0, 0), and then inserts the first value, 1, after it. 1 becomes the current position.
# ~ 0 (2) 1: the spinlock steps forward three times (0, 1, 0), and then inserts the second value, 2, after it. 2 becomes the current position.
# ~ 0  2 (3) 1: the spinlock steps forward three times (1, 0, 2), and then inserts the third value, 3, after it. 3 becomes the current position.
# ~ And so on:

# ~ 0  2 (4) 3  1
# ~ 0 (5) 2  4  3  1
# ~ 0  5  2  4  3 (6) 1
# ~ 0  5 (7) 2  4  3  6  1
# ~ 0  5  7  2  4  3 (8) 6  1
# ~ 0 (9) 5  7  2  4  3  8  6  1

L=[0]
p=0
for x in range(1,2018):
	p+=344
	p%=len(L)
	L.insert(p+1,x)
	# ~ print(p+1,L)
	p+=1
v=L.index(2017)
print (L[v-5:v+6])
