class facet():
	def __init__(s):
		s.val=""
		s.E=None
		s.N=None
		s.W=None
		s.S=None
		s.r=0
		s.c=0
class face():
	def __init__(s,n,i=""):
		s.n=i
		G=[[facet() for c in range(n)]for r in range(n)]
		for row in G:
			for a,b in zip(row,row[1:]):
				a.E=b
				b.W=a
			for ra,rb in zip(G,G[1:]):
				for a,b in zip(ra,rb):
					a.S=b
					b.N=a
		s.G=G
	def R(s):
		s.G=[c[::-1] for c in zip(*s.G)]
	def U(s):
		s.R()
		s.R()
	def L(s):
		s.R()
		s.R()
		s.R()
	def rep(s):
		print(f"=== {s.n} ====")
		for row in s.G:
			print("".join([c.val for c in row]))
class cube():
	def __init__(s,n):
		s.F,s.L,s.R,s.T,s.B,s.H=[face(n,i) for i in list("FLRTBH")]
		# ~ connect faces
		for _ in range(4):
			for ra,rb in zip (s.F.G,s.R.G):
				ra[n-1].E=rb[0]
				rb[0].W=ra
			for a,b in zip(s.F.G[0],s.T.G[n-1]):
				a.N=b
				b.S=a
			for a,b in zip(s.F.G[n-1],s.B.G[0]):
				a.S=b
				b.N=a
			s.rotR()
	def rotR(s):
		s.T.R()
		s.B.L()
		s.L.U()
		s.H.U()
		s.F,s.L,s.R,s.H=s.R,s.F,s.H,s.L
	def rotL(s):
		s.rotR()
		s.rotR()
		s.rotR()
	def rotT(s):
		s.L.L()
		s.R.R()
		s.F,s.T,s.B,s.H=s.B,s.F,s.H,s.T
	def rotB(s):
		s.rotT()
		s.rotT()
		s.rotT()
dim=50
c=cube(dim)
faces,*instructions=open("d22.txt").read().split("\n\n")
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
			for row,vals in zip(c.F.G,sublines):
				for fact,v in zip(row,vals):
					fact.val=v
		c.rotR()
	for _ in range(subblocks):c.rotL()
	c.rotT()
for _ in range(blocks):c.rotB()
# ~ exit()
c.F.rep()
while True:
	move=input()
	match move:
		case 't':c.rotT()
		case 'r':c.rotR()
		case 'l':c.rotL()
		case 'b':c.rotB()
	c.F.rep()

c=cube(2)
s=1
for _ in range(4):
	V=[[s,s+1],[s+2,s+3]]
	for row,rv in zip(c.F.G,V):
		for fact,v in zip(row,rv):fact.val=str(v)
	c.rotR()
	s+=4
V=[[s,s+1],[s+2,s+3]]
c.rotB()
for row,rv in zip(c.F.G,V):
	for fact,v in zip(row,rv):fact.val=str(v)
s+=4
V=[[s,s+1],[s+2,s+3]]
c.rotB()
c.rotB()
for row,rv in zip(c.F.G,V):
	for fact,v in zip(row,rv):fact.val=str(v)
c.rotB()
while True:
	move=input()
	match move:
		case 'N':c.rotT()
		case 'E':c.rotR()
		case 'W':c.rotL()
		case 'S':c.rotB()
	c.F.rep()
c.F.rep()
c.rotR()
c.F.rep()
c.rotR()
c.F.rep()
c.rotR()
c.F.rep()
c.rotR()
c.F.rep()
c.rotT()
c.rotL()
c.F.rep()

