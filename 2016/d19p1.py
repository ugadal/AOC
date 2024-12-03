def ring(n):
	p=[1]*n
	e=0
	while p.count(0)!=n-1:
		ne=(e+1)%n
		if p[e]:
			while p[ne]==0:ne=(ne+1)%n
			p[e]+=p[ne]
			p[ne]=0
			# ~ print(p)
		e=(e+1)%n
	print(n,next((i+1 for i,v in enumerate(p) if v!=0)))
e=2
# ~ ring(3004953)
while True:
	ring(e)
	e+=1
	input()
