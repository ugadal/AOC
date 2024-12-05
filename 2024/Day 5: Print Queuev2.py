#!/usr/bin/env python3
#
sep="\n\n"
fn,part="d5.txt",0
rules,updates=open(fn).read().split("\n\n")[2:4]
R={}
for rule in rules.splitlines():
	a,b=rule.split("|")
	R[a,b]=True
	R[b,a]=False
res=[]
def validate(update):
	for p,x in enumerate(update[:-1]):
		for y in update[p+1:]:
			if R.get((x,y),True):continue
			else:return False
	return True
def getmid(update):
	pos=len(update)//2
	v=int(update[pos])
	return v
INVALID=[]
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
			if R.get((x,y),True):
				py+=1
				continue
			else:
				invalid[px],invalid[py]=invalid[py],invalid[px]
				break
		else:px+=1
	v=getmid(invalid)
	return v
p2=[]
for invalid in INVALID:
	p2.append(fixit(invalid))
print(sum(p2))
# ~ part2 using sorted
class val():
	def __init__(self,x):
		self.v=x
	def __lt__(self,other):
		return R.get((self.v,other.v),True)	
def correct(invalid):
	invalid=[val(x) for x in invalid]
	return sorted(invalid)
p2=[]
for invalid in INVALID:
	c=correct(invalid)
	p2.append(int(c[len(invalid)//2].v))
print(sum(p2))
