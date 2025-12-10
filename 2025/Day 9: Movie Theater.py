#!/usr/bin/env python3
#
from malib import *
# ~ part=0
data=open(fn).read().split(sep)[part]
rs=[]
for line in data.splitlines():
	c,r=map(int,line.split(","))
	rs.append((c,r))
def area(a,b):
	x,y=a
	i,j=b
	gx=abs(x-i)+1
	gy=abs(y-j)+1
	return gx*gy
res=max(area(a,b) for a,b in it.combinations(rs,2))
print("p1 :",res)
Rot=[]
# ~ for a,b,c in zip(rs,rs[1:],rs[2:]):
	# ~ u,v=b[0]-a[0],b[1]-a[1]
	# ~ s,t=c[0]-b[0],c[1]-b[1]
	# ~ if u*t-s*v >0:Rot.append("R")
	# ~ else:Rot.append("L")
# ~ print (f"R: {Rot.count("R")} L: {Rot.count("L")}")
# ~ print(sum([ox*dy-dx*oy for (ox,oy),(dx,dy) in zip(rs,rs[1:]+[rs[0]])]))
# ~ exit()
	
C=[c for c,r in rs]
C.extend([c+1 for c in C])
C=set(C)
C=list(C)
C.sort()
print(C)
R=[r for c,r in rs]
R.sort()
R.extend([r+1 for r in R])
R=set(R)
R=list(R)
R.sort()
print(R)
class rect():
	all=[]
	def __init__(self,p):
		a,b,c,d=p
		self.p=a,b,c,d
		self.a=a
		self.b=b
		self.tl=a,c
		self.br=b,d
		self.c=c
		self.d=d
		self.colored=0
		self.gx=(a+b)/2
		self.gy=(c+d)/2
		rect.all.append(self)
	def area(self):
		return (1+self.b-self.a) * (1+self.d-self.c)
	def isin(self,T):
		if not T.a<=self.a<=T.b:return False
		if not T.a<=self.b<=T.b:return False
		if not T.c<=self.c<=T.d:return False
		if not T.c<=self.d<=T.d:return False
		return True
Rec=[]
for a,b in zip (C,C[1:]):
	for c,d in zip(R,R[1:]):
		rect((a,b-1,c,d-1))
def rfv(o,d):
	ox,oy=o
	dx,dy=d
	a,b=sorted((ox,dx))
	c,d=sorted((oy,dy))
	rect((a,b,c,d))
	return rect.all.pop()
G=[]
rows=list(set(r.gy for r in rect.all))
rows.sort()
for row in rows:
	G.append(sorted([r for r in rect.all if r.gy==row],key=lambda s:s.gx))
z=1
for ox,oy in rs[::-1]:
# ~ for ox,oy in rs:
	for r in rect.all:
		if r.b<ox and r.d<oy:r.colored+=z
	z=-z
	# ~ for row in G:
		# ~ print("".join(["x" if r.colored>0 else "." for r in row]))
	# ~ input()
print("==")
for o,d in zip(rs,rs[1:]+[rs[0]]):
	V=rfv(o,d)
	for rec in rect.all:
		if rec.isin(V):rec.colored=True
for row in G:
	print("".join(["x" if r.colored>0 else "." for r in row]))
rec=-inf
for a,b in it.combinations(rs,2):
	V=rfv(a,b)
	if V.area()<rec:continue
	incl=[r for r in rect.all if r.isin(V)]
	if all(r.colored>0 for r in incl):
		if V.area()>rec:
			print("ok",a,b,V.area())
			rec=V.area()
# ~ 1410501884
