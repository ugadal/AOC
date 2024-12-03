import itertools as it
G=open(0).read().splitlines()
NR=len(G)
NC=len(G[0])
offsets=((1,0),(0,1),(-1,0),(0,-1))
D={}
for r,row in enumerate(G):
	for c,s in enumerate(row):
		if s.isdigit():D[s]=(r,c)
print(D)
def dab(a):
	seen=[]
	step=-1
	todo=[D[a]]
	while todo:
		# ~ print(len(todo),todo)
		nxtodo=[]
		step+=1
		for cr,cc in todo:
			# ~ if (cr,cc) in seen:continue
			if (cr,cc) in D.values():yield G[cr][cc],step
			for dr,dc in offsets:
				nr=cr+dr
				nc=cc+dc
				if not 0<nr<NR:continue
				if not 0<nc<NC:continue
				if G[nr][nc]=="#":continue
				if (nr,nc) in seen:continue
				# ~ if (nr,nc) in nxtodo:continue
				nxtodo.append((nr,nc))
				seen.append((nr,nc))
		seen.append((cr,cc))
		todo=nxtodo
L={}
for z in D.keys():
	print(f"from  {z}")
	for k in dab(z):
		print(k)
		t,d=k
		L[z,t]=d
print(L)
spots=list(D.keys())
spots.remove("0")
print(spots)
best=float("inf")
for comb in it.permutations(spots):
	comb=list(comb)
	comb.insert(0,"0")
	td=0
	for a,b in zip (comb,comb[1:]):
		td+=L[a,b]
	if td<best:best=td
print(best)
				
		
