#!/usr/bin/env python
# -*- coding: utf-8 -*-
from mylib import *
mykey=2866
'''
Find the fuel cell's rack ID, which is its X coordinate plus 10.
Begin with a power level of the rack ID times the Y coordinate.
Increase the power level by the value of the grid serial number (your puzzle input).
Set the power level to itself multiplied by the rack ID.
Keep only the hundreds digit of the power level (so 12345 becomes 3; numbers with no hundreds digit become 0).
Subtract 5 from the power level.
For example, to find the power level of the fuel cell at 3,5 in a grid with serial number 8:

The rack ID is 3 + 10 = 13.
The power level starts at 13 * 5 = 65.
Adding the serial number produces 65 + 8 = 73.
Multiplying by the rack ID produces 73 * 13 = 949.
The hundreds digit of 949 is 9.
Subtracting 5 produces 9 - 5 = 4.
So, the power level of this fuel cell is 4.

Here are some more example power levels:

Fuel cell at  122,79, grid serial number 57: power level -5.
Fuel cell at 217,196, grid serial number 39: power level  0.
Fuel cell at 101,153, grid serial number 71: power level  4.'''
@memoize
def comp(x,y,g):
	rid=10+x
	pl=g+rid*y
	pl*=rid
	try:pl=int(str(pl)[-3])
	except:pl=0
	pl-=5
	return pl
# ~ print(comp(3,5,8))
# ~ print(comp(122,79,57))
# ~ print(comp(217,196,39))
# ~ print(comp(101,153,71))
'''
For grid serial number 18, the largest total 3x3 square has a top-left corner of 33,45 (with a total power of 29); these fuel cells appear in the middle of this 5x5 region:

-2  -4   4   4   4
-4   4   4   4  -5
 4   3   3   4  -4
 1   1   2   4  -3
-1   0   2  -5  -2'''
def sg(x,y,g,s=3):
	V=0
	for row in range(y,y+s):
		V+=sum(comp(col,row,g) for col in range(x,x+s))
	return V

print(sg(33,45,18))
print(sg(21,61,42))
rec=0
for s in range(1,301):
	for x in range(1,302-s):
		for y in range(1,302-s):
			tv=sg(x,y,mykey,s)
			if tv>rec:
				rec=tv
				print(x,y,s)
	
