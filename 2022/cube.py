class facet():
	def __init__(s,x,y,z):
		s.val=""
		s.E=None
		s.N=None
		s.W=None
		s.S=None
		s.r=0 #should contain original row in puzzle
		s.c=0 #should contain original col in puzzle
		s.cx=x
		s.cy=y
		s.cz=z
	def rep(s):
		return str((s.val,s.cx,s.cy,s.cz))
class face():
	def __init__(s,n,i=""):
		if n%2:
			edge=(n-1)//2
			coord=[[(x,z) for x in range(-edge,edge+1)] for z in range(edge,-edge-1,-1)]
			edge=-edge-.5
		else:
			edge=(n+1)//2
			coord=[[(x+.5,z+.5) for x in range(-edge,edge)] for z in range(edge-1,-edge-1,-1)]
			edge=-edge
		F=[]
		for row in coord:
			F.append([facet(x,edge,z) for x,z in row])
		# ~ for row in F:
			# ~ for a,b in zip(row,row[1:]):
				# ~ a.E=b
				# ~ b.W=a
		# ~ for ra,rb in zip(F,F[1:]):
			# ~ for a,b in zip(ra,rb):
				# ~ a.S=b
				# ~ b.N=a
		s.F=F
		s.edge=edge
		s.coord=coord
		s.orient=0
	def rotR(s): #around z counter clockwise
		for row in s.F:
			for ft in row:
				ft.cx,ft.cy=-ft.cy,ft.cx
		if s.F[0][0].cz==s.edge:
			s.orient-=1
			s.orient%=4
		if s.F[0][0].cz==-s.edge:
			s.orient+=1
			s.orient%=4
	def rotL(s): #around z clockwise
		for row in s.F:
			for ft in row:
				ft.cx,ft.cy=ft.cy,-ft.cx
		if s.F[0][0].cz==s.edge:
			s.orient+=1
			s.orient%=4
		if s.F[0][0].cz==-s.edge:
			s.orient-=1
			s.orient%=4
	def rotT(s): #around X clockwise
		for row in s.F:
			for ft in row:
				ft.cy,ft.cz=ft.cz,-ft.cy
		if s.F[0][0].cx==s.edge:
			s.orient+=1
			s.orient%=4
		if s.F[0][0].cx==-s.edge:
			s.orient-=1
			s.orient%=4
	def rotB(s): #around X counterclockwise
		for row in s.F:
			for ft in row:
				ft.cy,ft.cz=-ft.cz,ft.cy
		if s.F[0][0].cx==s.edge:
			s.orient-=1
			s.orient%=4
		if s.F[0][0].cx==-s.edge:
			s.orient+=1
			s.orient%=4
	def rep(s):
		print(f"===={s.orient} ====")
		for row in s.F:
			print("".join([c.val for c in row]))
class cube():
	def __init__(s,n):
		s.F=[]
		if n%2:
			edge=(n-1)//2
			coord=[[(x,z) for x in range(-edge,edge+1)] for z in range(edge,-edge-1,-1)]
			edge=-edge-.5
		else:
			edge=(n+1)//2
			coord=[[(x+.5,z+.5) for x in range(-edge,edge)] for z in range(edge-1,-edge-1,-1)]
			edge=-edge
		s.edge=edge
		for belt in range(4):
			s.F.append(face(n))
			s.rotL()
		# ~ for g,d in zip(s.F,s.F[1:]):
			# ~ for rowa,rowb in zip(g.F,d.F):
				# ~ rowa[-1].E=rowb[0]
				# ~ rowb[0].W=rowb[-1]
		# ~ for rowa,rowb in zip(s.F[-1].F,s.F[0].F):
			# ~ rowa[-1].E=rowb[0]
			# ~ rowb[0].W=rowb[-1]
		s.rotT()
		s.F.append(face(n))
		s.rotT()
		s.rotT()
		s.F.append(face(n))
		s.rotT()
		# ~ for _ in range(4):
			# ~ for belt in range(4):
				# ~ s.mkTB()
				# ~ s.rotL()
			# ~ s.rotT()
	# ~ def mkTB(s):
	# ~ for _ in range(4):
		# ~ FF=s.getfront()
		# ~ TF=s.gettop()
		# ~ BF=s.getbot()
		# ~ LF=s.getleft()
		# ~ RF=s.getright()
		# ~ for ca,cb in zip(FF.F[0],TF.F[-1]): #totop
			# ~ ca.N=cb
			# ~ cb.S=ca
		# ~ for ca,cb in zip(FF.F[-1],BF.F[0]): #tobottom
			# ~ ca.S=cb
			# ~ cb.N=ca
		# ~ for rowa,rowb in zip(FF.F,RF.F): #toright
			# ~ rowa[-1].E=rowb[0]
			# ~ rowb[0].W=rowb[-1]
		# ~ for row,rowb in zip(FF.F,LF.F): #toright
			# ~ rowa[0].W=rowb[-1]
			# ~ rowb[-1].E=rowa[0]
		# ~ s.rotR()
		
	def rotR(s):
		for fac in s.F:fac.rotR()
	def rotL(s):
		for fac in s.F:fac.rotL()
	def rotT(s):
		for fac in s.F:fac.rotT()
	def rotB(s):
		for fac in s.F:fac.rotB()
	def getfront(s):
		# ~ return next(F for F in s.F if F.F[0][0].cy==s.edge)
		cf=next(F for F in s.F if F.F[0][0].cy==s.edge)
		# ~ order correctly
		rotneeded=0
		while cf.F[0][0].cx!=s.edge and cf.F[0][0].cz!=s.edge:
			cf.rotR()
			rotneeded+=1
		VV=cf
		for _ in range(rotneeded):cf.rotL()
		return VV
	def gettop(s):
		s.rotB()
		V=s.getfront()
		s.rotT()
		return V
	def getbot(s):
		s.rotT()
		V=s.getfront()
		s.rotB()
		return V
	def getleft(s):
		s.rotR()
		V=s.getfront()
		s.rotL()
		return V
	def getright(s):
		s.rotL()
		V=s.getfront()
		s.rotR()
		return V
dim=4
c=cube(dim)
print("----------------")
c.getfront().rep()
faces,*instructions=open("exp22.txt").read().split("\n\n")
faces=faces.splitlines()
blocks=len(faces)//dim
print(f"blocks: {blocks}")
for block in range(blocks):
	lines=faces[block*dim:block*dim+dim]
	for l in lines:print("l",l)
	subblocks=len(lines[0])//dim
	print(f"subblocks {subblocks}")
	for subblock in range(subblocks):
		sublines=[line[subblock*dim:subblock*dim+dim] for line in lines]
		for l in sublines:print("subl",l)
		if sublines[0][0]!=" ":
			for row,vals in zip(c.getfront().F,sublines):
				for fact,v in zip(row,vals):
					fact.val=v
		c.rotL()
	for _ in range(subblocks):c.rotR()
	c.rotT()
for _ in range(blocks):c.rotB()
c.getfront().rep()
c.rotB()
c.getfront().rep()
c.rotB()
c.getfront().rep()
# ~ c.rotT()
F=c.getfront()
F.rep()
while True:
	move=input()
	match move:
		case 't':c.rotB()
		case 'r':c.rotL()
		case 'l':c.rotR()
		case 'b':c.rotT()
	c.getfront().rep()
# ~ for row in F.F:
    # ~ for ft in row:
            # ~ print(ft,"r",ft.E,"t",ft.N,"l",ft.W,"b",ft.S)
# ~ c.rotT()
# ~ F=c.getfront()
# ~ F.rep()
# ~ for row in F.F:
    # ~ for ft in row:
            # ~ print(ft,"r",ft.E,"t",ft.N,"l",ft.W,"b",ft.S)


# ~ exit()
# ~ c.F.rep()
# ~ while True:
	# ~ move=input()
	# ~ match move:
		# ~ case 't':c.rotT()
		# ~ case 'r':c.rotR()
		# ~ case 'l':c.rotL()
		# ~ case 'b':c.rotB()
	# ~ c.F.rep()

# ~ c=cube(2)
# ~ s=1
# ~ for _ in range(4):
	# ~ V=[[s,s+1],[s+2,s+3]]
	# ~ for row,rv in zip(c.F.G,V):
		# ~ for fact,v in zip(row,rv):fact.val=str(v)
	# ~ c.rotR()
	# ~ s+=4
# ~ V=[[s,s+1],[s+2,s+3]]
# ~ c.rotB()
# ~ for row,rv in zip(c.F.G,V):
	# ~ for fact,v in zip(row,rv):fact.val=str(v)
# ~ s+=4
# ~ V=[[s,s+1],[s+2,s+3]]
# ~ c.rotB()
# ~ c.rotB()
# ~ for row,rv in zip(c.F.G,V):
	# ~ for fact,v in zip(row,rv):fact.val=str(v)
# ~ c.rotB()
# ~ while True:
	# ~ move=input()
	# ~ match move:
		# ~ case 'N':c.rotT()
		# ~ case 'E':c.rotR()
		# ~ case 'W':c.rotL()
		# ~ case 'S':c.rotB()
	# ~ c.F.rep()
# ~ c.F.rep()
# ~ c.rotR()
# ~ c.F.rep()
# ~ c.rotR()
# ~ c.F.rep()
# ~ c.rotR()
# ~ c.F.rep()
# ~ c.rotR()
# ~ c.F.rep()
# ~ c.rotT()
# ~ c.rotL()
# ~ c.F.rep()

