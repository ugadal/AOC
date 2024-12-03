
exp="""5-8
0-2
4-7"""
# ~ rules=exp.splitlines()
rules=[tuple(map(int,rule.split("-"))) for rule in open("d20.txt").read().splitlines()]
print (rules)
valid=[(0,4294967295)]
safe=[]
while True:
	nv=[]
	for a,b in valid:
		print(a,b)
		for c,d in rules:
			# ~ print(a,b,c,d,valid,nv)
			if c>b:continue
			if d<a:continue
			if c<=a and b<=d:break
			if a==c and d==b:break
			# ~ 1
			if a<c and d<b:
				nv.append((a,c-1))
				nv.append((d+1,b))
				break
			if a==c and d<b:
				nv.append((d+1,b))
				break
			if a<c and d==b:
				nv.append((a,c-1))
				break
			# ~ 2
			if c<a<=d<b:
				nv.append((d+1,b))
				break
			# ~ 3
			if a<c<=b<d:
				nv.append((a,c-1))
				break
		else:
			safe.append((a,b))
		# ~ print(nv)
	if nv==valid:break
	valid=nv
# ~ print(safe)
print("p1 :",min([a[0] for a in safe]))	
print("p2 :",sum([1+a[1]-a[0] for a in safe]))	
		
			
		
		
			
		
