#!/usr/bin/env python
# -*- coding: utf-8 -*-
import functools
exp="""[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]"""
expected="""
[]
[[]]
[[[]]]
[1,1,3,1,1]
[1,1,5,1,1]
[[1],[2,3,4]]
[1,[2,[3,[4,[5,6,0]]]],8,9]
[1,[2,[3,[4,[5,6,7]]]],8,9]
[[1],4]
[[2]]
[3]
[[4,4],4,4]
[[4,4],4,4,4]
[[6]]
[7,7,7]
[7,7,7,7]
[[8,7,6]]
[9]"""
# ~ def HNsort()
def newcmp(a,b):
	print(f"=> {a} <-> {b}")
	if type(a)==type(b)==int:return a-b
	if type(a)==type(b)==list:
		for i,j in zip(a,b):
			if i==j:continue
			i=newcmp(i,j)
			if i:return i
		print("comparing lists")
		return len(a)-len(b)
	if type(a)==list:return newcmp(a,[b])
	return newcmp([a],b)
bn=0
R=0
blocks=open("d13.txt").read().split("\n\n")
Z=[]
for block in blocks:Z.extend(map(eval,block.splitlines()))
Z.append([[2]])
Z.append([[6]])
Z.sort(key=functools.cmp_to_key(newcmp))
for l in Z:print(l)
a=Z.index([[2]])+1
b=Z.index([[6]])+1
print(a*b)

