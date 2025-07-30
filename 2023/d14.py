#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
def rep(G):
	print(pd.DataFrame(G))
def cs(x,y=1):
	if y==1:return x*(x+1)/2
	return cs(x)-cs(y-1)
from copy import deepcopy as dc
exp="""O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#...."""

def roll(row,rev=False):
	w=list(row)
	if rev:w=list(reversed(w))
	R=[]
	D=[]
	T=[]
	for c in w:
		if c=="O":T.append(c)
		elif c==".":D.append(c)
		elif c=="#":
			R.extend(T)
			R.extend(D)
			R.append(c)
			T=[]
			D=[]
	R.extend(T)
	R.extend(D)
	if rev:R=list(reversed(R))
	return R
def west(G,rev=False):
	w=dc(G)
	N=[]
	for row in w:
		N.append(roll(row,rev))
	return N
	
def east(G):return west(G,True)
def north(G):return zip(*west(zip(*G)))
def south(G):return zip(*east(zip(*G)))

def cycle(G):
	return(east(south(west(north(G)))))

def statusquo(G):
	count=0
	P=dc(G)
	# ~ Known=[dc(P)]
	Known=[]
	while True:
		count+=1
		G=cycle(G)
		if Known.count(G):
			# ~ print(count,compute(G))
			index=Known.index(G)
			# ~ print (count,index)
			# ~ rep(G)
			# ~ rep(Known[index])
			print (G==Known[index])
			loop=count-index-1
			inx=(1000000000-index-1)%loop+index
			# ~ print(inx)
			return Known[inx]
		# ~ print(count,compute(P))
		Known.append(dc(G))
		P=dc(G)
def compute(G):
	W=list(G)
	t=0
	high=len(W)
	score=range(high,0,-1)
	for col in zip(*W):
		for c,v in zip(col,score):
			if c=="O":t+=v
	return t	

		
G=exp.strip().splitlines()
F=statusquo(G)
print(compute(F) )
G=open("d14.txt").read().strip().splitlines()
F=statusquo(G)
print(compute(F) )


exit()
# ~ 64

# ~ copy paste stuff goes under here

compute(north(G))
G=open("d14.txt").read().strip().splitlines()
compute(north(G))
F=statusquo(G)
compute(F)
compute(north(F))


		
G=exp.strip().splitlines()
G=open("d14.txt").read().strip().splitlines()
rep(G)
G=list(zip(*G))
wid=len(G[0])
rep(G)

	
	
G=exp.strip().splitlines()
compute(G)
compute(north(G))






	
