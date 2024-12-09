#!/usr/bin/env python3
#
sep="\n\n"
fn,part="d9.txt",1
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
# ~ while c.right:
	# ~ print(c)
	# ~ c=c.right
# ~ print(c)

def canmove(case):
	# ~ print("in test movable :",case)
	AS=[]
	cp=case.left
	while cp.case!=0:
		# ~ print("testing :",cp)
		if cp.t!="space":
			cp=cp.left
			continue
		if cp.l>=case.l:
			AS.append(cp)
		cp=cp.left
	return AS
		
	

cp=endp
while cp.left.case!=0: 
	# ~ print("current right pointer",cp)
	if cp.left.t!="file":
		cp=cp.left
		continue
	s=cp.left
	AS=canmove(s)
	if AS:
		# ~ for avs in AS:print(avs)
		t=AS.pop()
		a=t.left
		c=s.left
		ns=space(s.l)
		# ~ print("A:",a)
		# ~ print("S:",s)
		# ~ print("T:",t)
		# ~ print("C:",c)
		# ~ print("CP:",cp)
		a.right=s
		s.left=a
		s.right=t
		t.left=s
		t.l-=s.l
		c.right=ns
		cp.left=ns
		ns.left=c
		ns.right=cp
		if t.l==0:
			t.left.right,t.right.left=t.right,t.left
		# ~ print("A:",a)
		# ~ print("S:",s)
		# ~ print("T:",t)
		# ~ print("C:",c)
		# ~ print("CP:",cp)
	else:cp=cp.left
	# ~ exit() 
	# ~ break
print("done")
c=startp
# ~ while c.right:
	# ~ print(c)
	# ~ c=c.right
# ~ print(c)
def ss(a,b):return (b**2-a**2+b+a)/2
c=startp
pos=0
total=0
while c.right:
	cc=c.right
	if cc.t=="file":
		total+=ss(pos,pos+cc.l-1)*cc.fid
		print(total)
	pos+=cc.l
	c=cc
print(total)
exit()
