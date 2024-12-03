def ring(n):
	p=[1]*n
	names=list(range(1,n+1))
	e=0
	# ~ print(p,names)
	while len(p)>1:
		cl=len(p)
		tg=(e+cl//2)%cl
		# ~ print(f"elf at pos {e} named {names[e]} steals from elf named {names[tg]} at pos {tg}")
		p[e]+=p[tg]
		p.pop(tg)
		names.pop(tg)
		# ~ print(e,p,names)
		if tg<e:e%=(cl-1)
		else:e=(e+1)%(cl-1)
		# ~ print(f"new e {e}",p,names)
	return names[0]
# ~ print(ring(5))
# ~ exit()

e=2
print(ring(5))
# ~ exit()
# ~ print(ring(3004953))
ev=[]
ones=[]
while True:
	v=ring(e)
	print(e,v)
	# ~ if v==e:ev.append(e)
	# ~ if v==1:ones.append(e)
	# ~ if v==e or v==1:
		# ~ print(ev)
		# ~ print(ones)
	input()
	e+=1

# ~ >>> l-3**13
# ~ 1410630
