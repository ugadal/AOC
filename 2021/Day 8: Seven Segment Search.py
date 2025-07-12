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
# ~ 0:6 abcefg
	# ~ 1:2 cf
# ~ 2:5 acdeg
# ~ 3:5 acdfg
	# ~ 4:4 bcdf
# ~ 5:5 abdfg
# ~ 6:6 abdefg
	# ~ 7:3 acf
	# ~ 8:7 abcdefg
# ~ 9:6 abcdfg

	# ~ 1:2 cf
	# ~ 7:3 acf
	# ~ 4:4 bcdf
# ~ 2:5 acdeg
# ~ 3:5 acdfg
# ~ 5:5 abdfg

# ~ 0:6 abcefg
# ~ 6:6 abdefg
# ~ 9:6 abcdfg
	# ~ 8:7 abcdefg
Rev={"cf":"1","acf":"7","bcdf":"4","acdeg":"2","acdfg":"3","abdfg":"5","abcefg":"0","abdefg":"6","abcdfg":"9","abcdefg":"8"}
	
# ~ acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf
# ~ 7: dab -> acf
# ~ 4: eafb -> bcdf
# ~ ab->cf
# ~ {ab} -> {cf}
# ~ acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf
# ~ abcdefg bcdef acdfg abcdf abd abcdef bcdefg abef abcdef ab | bcdef abcdf bcdef abcdf
# ~ 8                         7                 4           1
# ~ 7 & 1 : abd & ab => d==>a
# ~ bcdef acdfg abcdf // 2 3 5 coded by acdeg acdfg abdfg
# ~ cf // ag in all: 
valid=list(Rev.keys())
source=list("abcdefg")
# ~ line="abcdefg bcdef acdfg abcdf abd abcdef bcdefg abef abcdef ab".split()
# ~ digit="cdfeb fcadb cdfeb cdbaf".split()
ttl=0
for d in block.splitlines():
	line,digit=d.split(" | ")
	line=line.split()
	digit=digit.split()
	for p in it.permutations(source):
		k={a:b for a,b in zip(source,p)}
		R=[]
		for word in line:
			neword="".join(sorted(k[x] for x in word))
			R.append(neword)
		if all(x in valid for x in R):
			target=["".join(sorted(k[x] for x in word)) for word in digit]
			res="".join(Rev[x] for x in target)
			ttl+=int(res)
print("p2:",ttl)
