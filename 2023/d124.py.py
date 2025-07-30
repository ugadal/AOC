import sympy
x,y,z,dx,dy,dz=sympy.symbols(list("xyzabc"))
T=(x,y,z,dx,dy,dz)
t=sympy.symbols("t")
def ad_bc(A,B):
	na,da=sympy.fraction(A)
	nb,db=sympy.fraction(B)
	return na*db-nb*da
def z(p,q):
	P=p
	Sp=[]
	for v,dv,u,du in zip(T,T[3:],P,P[3:]):
		lp=v+dv*t
		rp=u+du*t
		# ~ print("left:",lp)
		# ~ print("right:",rp)
		e=lp-rp
		# ~ print("e:",e)
		Sp.append(sympy.solve(e,t)[0])
	# ~ for s in Sp:print("tp=",s)
	SSp=[]
	for ls,fs in enumerate(Sp[:-1]):
		for rs in Sp[ls+1:]:
			SSp.append(ad_bc(fs,rs))
	# ~ for s in SSp:print(s.expand())
	P=q
	Sq=[]
	for i,j,k,l in zip(T,T[3:],P,P[3:]):
		e=i+j*t-(k+l*t)
		Sq.append(sympy.solve(e,t)[0])
	# ~ for s in Sq:print("tq=",s)
	SSq=[]
	for ls,fs in enumerate(Sq[:-1]):
		for rs in Sq[ls+1:]:
			SSq.append(ad_bc(fs,rs))
	# ~ for s in SSq:print(s.expand())
	for s,q in zip(SSp,SSq):
		v=s-q
		v=v.simplify()
		# ~ print(v,v.simplify())
		yield [v.coeff(s) for s in T]+[-(v.as_coefficients_dict()[1])]
for row in z((19,13,30,-2,1,2),(18,19,22,-1,-1,-2)):
	print (row)
for row in z((19,13,30,-2,1,2),(20,25,34,-2,-2,-4)):
	print (row)
for row in z((19,13,30,-2,1,2),(12,31,28,-1,-2,-1)):
	print (row)
