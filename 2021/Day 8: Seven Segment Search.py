#!/usr/bin/env python
# -*- coding: utf-8 -*-
part=2
import re
import sys
import itertools as it
from functools import cache
import uuid
cp=str(sys.argv[0])
dre=re.compile(r"^Day (\d+):")
day=dre.findall(cp)[0]
fn=f"d{day}.txt"
# ~ block=open(fn).read().split("\n\n\n")[part]
block=open(fn).read().split("\n\n")[part]

ttl=0
for line in block.splitlines():
	a,b=line.split(" | ")
	L=tuple(map(len,b.split()))
	# ~ print(L)
	for z in (2,3,4,7):
		ttl+=L.count(z)
print("p1:",ttl)
	# ~ 1:2 cf
	# ~ 7:3 acf
	# ~ 4:4 bcdf
# ~ 2:5 acdeg
# ~ 3:5 acdfg includes [1]
# ~ 5:5 abdfg

# ~ 0:6 abcefg 
# ~ 6:6 abdefg includes(5)
# ~ 9:6 abcdfg includes(4,7)
	# ~ 8:7 abcdefg
Rev={"cf":"1","acf":"7","bcdf":"4","acdeg":"2","acdfg":"3","abdfg":"5","abcefg":"0","abdefg":"6","abcdfg":"9","abcdefg":"8"}
	
valid=list(Rev.keys())
source=list("abcdefg")
# ~ ttl=0
# ~ S={}
# ~ for d in block.splitlines():
	# ~ break
	# ~ print(d)
	# ~ line,digit=d.split(" | ")
	# ~ line=line.split()
	# ~ digit=digit.split()
	# ~ for p in it.permutations(source):
		# ~ k={a:b for a,b in zip(source,p)}
		# ~ R=[]
		# ~ for word in line:
			# ~ neword="".join(sorted(k[x] for x in word))
			# ~ R.append(neword)
		# ~ if all(x in valid for x in R):
			# ~ target=["".join(sorted(k[x] for x in word)) for word in digit]
			# ~ res="".join(Rev[x] for x in target)
			# ~ S[d]=res
			# ~ ttl+=int(res)
			# ~ print(k)
	# ~ break
# ~ print("p2:",ttl)
# ~ smarter
ttl=0
for d in block.splitlines():
	# ~ print(d)
	V={}
	line,digit=d.split(" | ")
	line=line.split()
	digit=digit.split()
	V["1"]=one=next(set(w) for w in line if len(w)==2)
	V["7"]=seven=next(set(w) for w in line if len(w)==3)
	V["4"]=four=next(set(w) for w in line if len(w)==4)
	V["8"]=eight=next(set(w) for w in line if len(w)==7)
	a=seven-one
	s235=[set(w) for w in line if len(w)==5]
	s069=[set(w) for w in line if len(w)==6]
	V["3"]=three=next(s for s in s235 if s&one==one)
	s25=s235
	s25.remove(three)
	V["9"]=nine=next(s for s in s069 if s&three==three)
	s06=s069
	s06.remove(nine)
	b=nine-three
	e=eight-nine
	V["5"]=five=next(s for s in s25 if b&s==b)
	s25.remove(five)
	V["2"]=two=s25.pop()
	c=nine-five
	V["6"]=six=next(s for s in s06 if s&c!=c)
	s06.remove(six)
	V["0"]=zero=s06.pop()
	t=int("".join([next(k for k,v in V.items() if v==set(dig) ) for dig in digit]))
	# ~ print(d,S[d],t)
	ttl+=t
print("p2:",ttl)
