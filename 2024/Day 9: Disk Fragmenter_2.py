#!/usr/bin/env python3
#
sep="\n\n"
fn,part="d9.txt",0
data=open(fn).read().split(sep)[part].strip()
data=[c for c in data]
caseid=0
class case():
	def __init__(self,fid,l):
		global caseid
		self.case=caseid
		self.file=fid
		self.l=l
		self.left=None
		self.right=None
		caseid+=1
	def __str__(self):
		txt=""
		if self.left:txt+=f"{self.left.case} <-"
		txt+=f" case#: {self.case} t:{self.file} l:{self.l}"
		if self.right:txt+=f" -> {self.right.case}"
		return txt
startp=case("root",0)
previous=startp
isfile=True
fid=0
while data:
	nv=int(data.pop(0))
	nc=case(fid if isfile else "space",nv)
	previous.right=nc
	nc.left=previous
	if isfile:
		fid+=1
	isfile=not isfile
	previous=nc
endp=case("end",0)
endp.left=nc
nc.right=endp
c=startp
while c.right:
	print(c)
	c=c.right
print(c)
cf=endp.left
while True: #break after file 0
	print("starting loop")
	print(cf)
	print()
	while cf.file=="space":
		cf=cf.left
		print("searching left",cf)
	print("cf:",cf)
	cs=startp
	while cs.file!="space" or cs.l<cf.l:
		print("searching right",cs)
		cs=cs.right
		if cs==None:
			cf=cf.left
			print("no valid space found")
			break
	else:
		print("current space",cs)
		a=cs.left
		c=cf.left
		d=cf.right
		cf.left=a
		a.right=cf
		cf.right=cs
		cs.left=cf
		cs.l-=cf.l
		c.right=d
		d.left=c
		print("updated space",cs)
		print("updated cf",cf)
		cf=c
		if cf.file=="root":break
		# ~ exit()
	
