#!/usr/bin/env python3
#
sep="\n\n"
fn,part="d5.txt",0
rules,updates=open(fn).read().split("\n\n")[2:4]
def rulegen(a,b):
	def fun(x,y):
		if x==a and y==b:return True
		if y==a and x==b:return False
		return True
	return fun
R=[]
for rule in rules.splitlines():
	a,b=rule.split("|")
	R.append(rulegen(a,b))
res=[]
INVALID=[]
def validate(update):
	tocompare=[]
	for p,x in enumerate(update[:-1]):
		for y in update[p+1:]:
			tocompare.append((x,y))
	for x,y in tocompare:
		if all(f(x,y) for f in R):continue
		return False
	return True
def getmid(update):
	pos=(len(update)-1)//2
	v=int(update[pos])
	return v
for update in updates.splitlines():
	update=update.split(",")
	if validate(update):res.append(getmid(update))
	else:INVALID.append(update)

print(sum(res))
# ~ part2
def fixit(inv):
	invalid=list(inv)
	px=0
	while px<len(invalid)-1:
		x=invalid[px]
		py=px+1
		while py<len(invalid):
			y=invalid[py]
			if all(f(x,y) for f in R):
				py+=1
				continue
			else:
				invalid[px],invalid[py]=invalid[py],invalid[px]
				break
		else:px+=1
	v=getmid(invalid)
	return v
		
p2=[]
while INVALID:
	invalid=INVALID.pop()
	p2.append(fixit(invalid))
print(sum(p2))
