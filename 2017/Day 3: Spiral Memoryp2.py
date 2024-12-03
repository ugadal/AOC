#!/usr/bin/env python3
G={}
G[0,0]=1
G[0,1]=1

cr=0
cc=1
n=2
t=0
while t<265149:
	for top in range(n-1):
		cr-=1
		t=sum([G.get((cr+dr,cc+dc),0) for dr in range(-1,2) for dc in range(-1,2)])
		G[cr,cc]=t
		# ~ print(G)
		# ~ input()
		if t>265149:print(t)
	for left in range(n):
		cc-=1
		t=sum([G.get((cr+dr,cc+dc),0) for dr in range(-1,2) for dc in range(-1,2)])
		G[cr,cc]=t
		# ~ print(G)
		# ~ input()		
		if t>265149:print(t)
	for down in range(n):
		cr+=1
		t=sum([G.get((cr+dr,cc+dc),0) for dr in range(-1,2) for dc in range(-1,2)])
		G[cr,cc]=t
		# ~ print(G)
		# ~ input()		
		if t>265149:print(t)
	for right in range(n+1):
		cc+=1
		t=sum([G.get((cr+dr,cc+dc),0) for dr in range(-1,2) for dc in range(-1,2)])
		G[cr,cc]=t
		# ~ print(G)
		# ~ input()		
		if t>265149:print(t)
	n+=2
print (G)
