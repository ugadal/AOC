import re
import sys
dim=int(sys.argv[1])
fn=sys.argv[2]
class facet():
	def __init__(self,x,y,z):
		self.val="?"
		self.neigh=[None,None,None,None]# right: 0 , bottom 1, left 2 top 3
		self.r=0 #should contain original row in puzzle
		self.c=0 #should contain original col in puzzle
		self.cx=x
		self.cy=y
		self.cz=z
		D[(self.cx,self.cy,self.cz)]=self
	def rotT(self): #around X
		self.cy,self.cz=self.cz,-self.cy
		if self.cx==-edge: #rblt -> bltr
			self.neigh.append(self.neigh.pop(0))
		if self.cx==edge: #rblt ->trbl
			self.neigh.insert(0,self.neigh.pop())
	def rotB(self):
		self.rotT()
		self.rotT()
		self.rotT()
	def rotL(self): #around z clockwise
		self.cx,self.cy=self.cy,-self.cx
		if self.cz==-edge: #rblt -> bltr
			self.neigh.append(self.neigh.pop(0))
		if self.cz==edge: # rblt -> trbl
			self.neigh.insert(0,self.neigh.pop())
	def rotR(self):
		self.rotL()
		self.rotL()
		self.rotL()
	def rotC(self):
		self.rotR()
		self.rotR()
		self.rotB()
		self.rotR()
		self.rotB()
	def rotCC(self):
		self.rotR()
		self.rotR()
		self.rotT()
		self.rotR()
		self.rotT()
	def upD(self):
		D[(self.cx,self.cy,self.cz)]=self
	def fullrep(self):
		if self.cx==edge:face="right"
		if self.cx==-edge:face="left"
		if self.cy==edge:face="front"
		if self.cy==-edge:face="hidden"
		if self.cz==edge:face="top"
		if self.cz==-edge:face="bottom"
		print (face,self.val,self.r,self.c,self.cx,self.cy,self.cz)
# ~ dim=4
D={}
if dim%2:
	edge=(dim-1)//2 #si 3 : -1 0 1  #edge=1
	coord=[(x,z)  for z in range(edge,-edge-1,-1) for x in range(-edge,edge+1)]
	edge=-edge-.5
else:
	edge=(dim+1)//2 #si 4: -1.5 -.5 .5 1.5   edge=2
	coord=[(x+.5,z+.5) for z in range(edge-1,-edge-1,-1) for x in range(-edge,edge) ]
	edge=-edge
print(coord)
	
class cube():
	global  D
	def __init__(self):
		self.F=[]
		for belt in range(4):
			self.F.extend([facet(x,edge,z) for x,z in coord])
			self.rotL()
		self.rotT()
		self.F.extend([facet(x,edge,z) for x,z in coord])
		self.rotT()
		self.rotT()
		self.F.extend([facet(x,edge,z) for x,z in coord])
		self.rotT()
	def fixrtbl(s):
		off=[x+.5 for x in range(edge,-edge)]
		print(off)
		for z in reversed(off):
			B=[]
			B.extend([D[a,edge,z]  for a in off])
			B.extend([D[-edge,a,z] for a in off])
			B.extend([D[a,-edge,z] for a in reversed(off)])
			B.extend([D[edge,a,z]  for a in reversed(off)])
			B.append(B[0])
			for a,b in zip(B,B[1:]):
				a.neigh[0]=b
				b.neigh[2]=a
		for x in off:
			B=[]
			B.extend([D[x,edge,a]  for a in off])
			B.extend([D[x,a,-edge] for a in off])
			B.extend([D[x,-edge,a] for a in reversed(off)])
			B.extend([D[x,a,edge]  for a in reversed(off)])
			B.append(B[0])
			for a,b in zip(B,B[1:]):
				a.neigh[3]=b
				b.neigh[1]=a
	def trf(self):
		tfr=self.F[0]
		print(tfr.cx,tfr.cy,tfr.cz)
		tfr=tfr.neigh[0]
		print(tfr.cx,tfr.cy,tfr.cz)

	def rotR(self):
		for fac in self.F:fac.rotR()
		for fac in self.F:fac.upD()
	def rotC(self):
		for fac in self.F:fac.rotC()
		for fac in self.F:fac.upD()
	def rotCC(self):
		for fac in self.F:fac.rotCC()
		for fac in self.F:fac.upD()
	def rotL(self):
		for fac in self.F:fac.rotL()
		for fac in self.F:fac.upD()
	def rotT(self):
		for fac in self.F:fac.rotT()
		for fac in self.F:fac.upD()
	def rotB(self):
		for fac in self.F:fac.rotB()
		for fac in self.F:fac.upD()
	def getfront(self):
		FT=list([D[(x,edge,z)] for (x,z) in coord ]) # ~ 
		for ft in FT:assert ft.cy==edge 
		return FT
	def rep(self):
		FT=self.getfront()
		for row in range(dim):
			print("".join([ft.val for ft in FT[row*dim:(row+1)*dim]]))
		for row in range(dim):
			print([(ft.val,ft.r,ft.c) for ft in FT[row*dim:(row+1)*dim]])
		fft=c.F[0]
		print(fft.val,fft.cx,fft.cy,fft.cz,fft.r,fft.c)
	def trep(self):
		self.rotB()
		TB=["-"*dim]
		FT=list(self.getfront())
		TB.extend(["".join([ft.val for ft in FT[row*dim:(row+1)*dim]]) for row in range(dim)])
		TB.append("-"*dim)
		self.rotT()
		MT=["|"]*dim
		for _ in range(4):
			FT=list(self.getfront())
			TM=["".join([ft.val for ft in FT[row*dim:(row+1)*dim]]) for row in range(dim)]
			MT=[a+b+"|" for a,b in zip(MT,TM)]
			self.rotL()
		TB.extend(MT)
		TB.append("-"*dim)
		self.rotT()
		FT=self.getfront()
		TB.extend(["".join([ft.val for ft in FT[row*dim:(row+1)*dim]]) for row in range(dim)])
		TB.append("-"*dim)
		self.rotB()
		for l in TB:print(l)
c=cube()
print(edge)
print("----------------")
faces,instructions=open(fn).read().split("\n\n")
faces=faces.splitlines()
for l in faces:print(l)
for r in range(len(faces)):
	t=faces[r]
	while len(t)<4*dim:t+=" "
	faces[r]=t
nblsh=0
# ~ while faces[0][0]==" ":
	# ~ nblsh+=1
	# ~ for r in range(len(faces)):
		# ~ t=faces[r]
		# ~ t=t[dim:]+t[:dim]
		# ~ faces[r]=t
for l in faces:print(l)
blocks=len(faces)//dim
c.trep()
c.start=None
for block in range(blocks):
	lines=faces[block*dim:block*dim+dim]
	subblocks=len(lines[0])//dim
	cbc=0
	for subblock in range(4):
		sublines=[line[subblock*dim:subblock*dim+dim] for line in lines]
		if sublines[0][0]!=" ":
			# ~ for _ in range(subblock):c.rotR()
			# ~ for _ in range(block):c.rotT()
			FT=c.getfront()
			for ix,(ft,v) in enumerate(zip(FT,"".join(sublines))):
				assert ft.cy==edge
				if not c.start:c.start=ft
				ft.val=v
				ft.r=block*dim+ix//dim
				ft.c=subblock*dim+ix%dim
			# ~ for _ in range(block):c.rotB()
			# ~ for _ in range(subblock):c.rotL()
		c.rotL()
		cbc+=1
	if block <blocks-1:
		while sublines[0][0]==" ":
			cbc-=1
			sublines=[line[cbc*dim:cbc*dim+dim] for line in lines]
			c.rotR()
		while faces[dim*(block+1)][cbc*dim]==" ":cbc-=1
		c.rotT()
		while cbc:
			c.rotR()
			cbc-=1
c.trep()
c.rotR()
c.rotCC()
c.start.fullrep()
# ~ exit()
while True:
	move=input()
	match move:
		case 't':c.rotT()
		case 'r':c.rotR()
		case 'l':c.rotL()
		case 'b':c.rotB()
		case 'c':c.rotC()
		case 'C':c.rotCC()
		case 'g':
			c.trep()
			break
	c.trep()
c.fixrtbl()
c.trep()
c.start.fullrep()
c.start.neigh[0].fullrep()
I=[10,"R",5,"L",5,"R",10,"L",4,"R",5,"L",5,None]
cd=0
cp=c.start
pc=cp
cp.val="X"
rd=0
def fixfront(cp):
	rotated=False
	if cp.cz==edge:
		c.rotT()
		rotated=True
	if cp.cz==-edge:
		c.rotB()
		rotated=True
	if cp.cx==edge:
		c.rotR()
		rotated=True
	if cp.cx==-edge:
		c.rotL()
		rotated=True
	if rotated:c.fixrtbl()
print (instructions)
s=re.compile("R|L")
V=list(map(int,s.split(instructions)))
Dirs=s.findall(instructions)
Dirs.append("None")
print(V,Dirs)
# ~ print(I)
# ~ input()
# ~ exit()
# ~ while I:
for std,ndtd in zip(V,Dirs):
	# ~ std=I.pop(0)
	# ~ ndtd=I.pop(0)
	sd=0	
	while cp.neigh[cd].val!="#" and sd<std:
		# ~ print(f"dir {cd} of curr pos is not rock, moving {cd}")
		pc=cp
		cp=cp.neigh[cd]
		fixfront(cp)
		cp.val="X"
		sd+=1
		# ~ c.trep()
	if ndtd=="R":
		cd=(cd+1)%4
		rd+=1
	if ndtd=="L":
		cd=(cd-1)%4
		rd-=1
	print(f"cd: {cd}")
print(cp.r+1,cp.c-dim*nblsh+1,rd,cp.c%dim)
print(1000*(cp.r+1)+4*(cp.c-dim*nblsh+1))
pc.fullrep()
cp.fullrep()
# ~ exit()
while True:
	move=input()
	match move:
		case 't':c.rotT()
		case 'r':c.rotR()
		case 'l':c.rotL()
		case 'b':c.rotB()
		case 'c':c.rotC()
		case 'C':c.rotCC()
	c.trep()
	c.start.fullrep()
	c.start.neigh[0].fullrep()
# ~ TP
"""
right on front d=1,0,0 continue on right becomes 0,1,0, -1,0,0, 0,-1,0
n=3
-1,E,1 -> 0,E,1 -> 1,E,1 ==> -E,-1, 1 -> -E,0,1 -> -E,1,1
"""
