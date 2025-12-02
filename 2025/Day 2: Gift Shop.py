#!/usr/bin/env python3
#
data="11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"

def invalid(s): #P1
	l=len(s)
	if l%2:	return False
	l=l//2
	if s[:l]==s[l:]:return True
	return False

count=0
# ~ for r in data.split(","):
for r in open("d2.txt").readline().split(","):
	d,f=r.split("-")
	for x in range(int(d),1+int(f)):
		if invalid(str(x)):count+=x
print("p1 :",count)

def invalid(s): #P2
	l=len(s)
	for rl in range(l//2,0,-1):
		if l%rl:continue
		c=s
		p=[]
		while c:
			p.append(c[:rl])
			c=c[rl:]
		if all(x==p[0] for x in p[1:]):return True
	return False

count=0
# ~ for r in data.split(","):
for r in open("d2.txt").readline().split(","):
	d,f=r.split("-")
	for x in range(int(d),1+int(f)):
		if invalid(str(x)):count+=x
print("p2 :",count)
