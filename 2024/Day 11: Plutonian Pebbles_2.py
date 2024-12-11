#!/usr/bin/env python3
#
from collections import deque
sep="\n\n"
fn,part="d11.txt",0
# ~ data=open(fn).read().split(sep)[part].splitlines()
# ~ data=deque(open(fn).readline().split())
data=open(fn).readline().split()
data=[(x,32) for x in data]

def blink(v):
	if v=="0":return ["1"]
	lv=len(v)
	if lv%2==0:return[str(int(v[:lv//2])),str(int(v[lv//2:]))]
	return [str(int(v)*2024)]
# ~ data=["125","17"]
# ~ data=[(x,25) for x in data]
data=deque(data)
count=0
# ~ out=deque()
while data:
	v,bn=data.pop()
	# ~ print(v,bn)
	if bn==0:
		# ~ out.appendleft(v)
		count+=1
	else:
		for nv in blink(v):
			data.append((nv,bn-1))
# ~ print(count,out)
print(count)
