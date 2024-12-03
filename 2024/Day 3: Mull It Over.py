#!/usr/bin/env python3
#
fn,part="d3.txt",2
data=open(fn).read().split("\n\n")[part]
import re
er=re.compile("mul\\((\\d+,\\d+)\\)")

res=0
for block in er.findall(data):
	a,b=map(int,block.split(","))
	res+=a*b
print("part 1:",res)

print("=====================")
do=re.compile("do\\(\\)")
dont=re.compile("don't\\(\\)")
def domul(s):
	res=0
	for block in er.findall(s):
		a,b=map(int,block.split(","))
		res+=a*b
	return res

data="do()"+data+"don't()"

data="".join(data.splitlines())

P=dont.split(data)
print(len(P))
res=0

for p in P:
	if do.search(p):
		sf=p[do.search(p).span()[1]:]
		res+=domul(sf)
print(res)
