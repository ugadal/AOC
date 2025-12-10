#!/usr/bin/env python3
#
from malib import *
part=0
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
		a,c=sorted((a,c))
		b,d=sorted((b,d))
		self.p=a,b,c,d
		self.a=a
		self.b=b
		self.c=c
		self.d=d
		self.colored=False
		self.gx=(a+c)/2
		self.gy=(b+d)/2
		rect.all.append(self)
	# ~ def getside(self,dp):
		# ~ print("rec:",self.p,"getside",dp)
		# ~ if dp.real:
			# ~ if dp.real>0:return self.r
			# ~ else:return self.l
		# ~ elif dp.imag<0:return self.t
		# ~ else:return self.d
	def area(self):
		return (1+self.b-self.a) * (1+self.d-self.c)

Rec=[]
for a,b in zip (C,C[1:]):
	for c,d in zip(R,R[1:]):
		rect((a,b,c-1,d-1))
for rec in rect.all:print(rec,rec.p,rec.gx,rec.gy,rec.area())
exit()
V=[(a,b-a) for a,b in zip(rs,rs[1:])]
a=rs[-1]
b=rs[0]
V.append((a,b-a))
print(V)
def within(s,v):
	# ~ print("is",v,"within",s,"?")
	dc=s[1]-s[0]
	dc=dc.real
	if dc:#horizontal
		if v[0].imag!=s[0].imag:return False
		if dc>0:#right
			return (s[0].real<=v[0].real and s[1].real>=v[1].real )
		else:#left
			return (s[0].real>=v[0].real and s[1].real<=v[1].real )
	else:#vertical
		if v[0].real!=s[0].real:return False
		dr=s[1]-s[0]
		dr=dr.imag
		if dr>0:#down
			return (s[0].imag<=v[0].imag and s[1].imag>=v[1].imag )
		else:#up
			return (s[0].imag>=v[0].imag and s[1].imag<=v[1].imag )
def rectcover(a,b):
	ga,ha,da,ba=a.p
	SA=set((r,c) for r in range(ha,ba) for c in range(ga,da))
	gb,hb,db,bb=b.p
	SB=set((r,c) for r in range(hb,bb) for c in range(gb,db))
	if SA&SB:return True
	return False
	if da<gb:return False
	if ga>=db:return False
	if ha>=bb:return False
	if ba<hb:return False
	return True
for v in V:
	o,d=v
	print(o,d)
	s,t=o,o+d
	print ("working on segment",s,t)
	for rec in Rec:
		so,st=rec.getside(d)
		r=within((s,t),(so,st))
		if r:
			rec.colored=True
			# ~ print("ok",rec,(so,st))
	# ~ exit()
for rec in Rec:
	print(rec.colored,rec.p)
colored=tuple(rec for rec in Rec if rec.colored)
print(len(colored))
for rec in (r for r in Rec if not r.colored):
	print(rec.p,rec.gx,rec.gy)
R=set(rec.gy for rec in Rec)
R=list(R)
R.sort()
print(R)
G=[]
for row in R:
	tr=[r for r in Rec if r.gy==row]
	tr=sorted(tr,key=lambda rec:rec.gx)
	G.append(tr)
for T,M,B in zip(G,G[1:],G[2:]):
	for t,l,m,r,d in zip(T[1:],M,M[1:],M[2:],B[1:]):
		if m.colored:continue
		# ~ print("examining",m)
		if all(x.colored for x in (t,l,r,d)):
			print("changed color",m)
z=rect((0,0,8,8))
for rec in Rec:
	print(rec.p,rectcover(z,rec))
for a,b in it.combinations(rs,2):
	print("combo",a,b)
	mic,mac=sorted([a.real,b.real])
	mir,mar=sorted([a.imag,b.imag])
	z=(mic,mir,mac+1,mar+1)
	z=[int(v) for v in z]
	z=rect(z)
	print("rect considered",z.gx,z.gy,z.p)
	covering=[r for r in Rec if rectcover(z,r)]
	print([(r.gx,r.gy,r.p) for r in covering])
	if all(r.colored for r in covering):
		print("ok",a,b,len(covering))
	else:print("rejected")
