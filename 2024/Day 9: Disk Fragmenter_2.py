#!/usr/bin/env python3
#
sep="\n\n"
fn,part="d9.txt",0
data=open(fn).read().split(sep)[part].strip()
data=[c for c in data]
caseid=0
class case():
	def __init__(self):
		global caseid
		self.case=caseid
		self.left=None
		self.right=None
		caseid+=1
	def __str__(self):return f"{self.left.case if self.left else "Void"} -> {self.case} -> {self.right.case if self.right else "Void"} "
class file(case):
	def __init__(self,l):
		global fid
		super().__init__()
		self.t="file"
		self.l=l
		self.fid=fid
		fid+=1
	def __str__(self):return f"{self.left.case} -> ({self.case}) fichier:{self.fid} {self.l} -> {self.right.case} "
class space(case):
	def __init__(self,l):
		super().__init__()
		self.t="space"
		self.l=l
	def __str__(self):return f"{self.left.case} -> ({self.case}) Space {self.l} -> {self.right.case} "
startp=case()
previous=startp
isfile=True
fid=0
while data:
	nv=int(data.pop(0))
	if isfile:nc=file(nv)
	else:nc=space(nv)
	previous.right=nc
	nc.left=previous
	isfile=not isfile
	previous=nc

endp=case()
endp.left=nc
nc.right=endp
c=startp
while c.right:
	print(c)
	c=c.right
print(c)
exit()
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
	
