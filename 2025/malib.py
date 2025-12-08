#!/usr/bin/env python3
#
import itertools as it
sep="\n\n"
inf=float("Inf")
def readG(data):
	G={}
	for row,line in enumerate(data.splitlines()):
		for col,s in enumerate(line):
			pos=complex(col,row)
			G[pos]=s
	return G,row+1,col+1
# ~ G,R,C=readG(data)
def pmap(G):
	for row in range(R):
		print("".join([G[complex(col,row)] for col in range(C)]))
def around(pos):
	for dc in (-1,0,1):
		for dr in (-1j,0,1j):
			if dc+dr:yield pos+dc+dr
def news(pos):
	yield pos+1
	yield pos-1
	yield pos+1j
	yield pos-1j
def reduce(L,p=1):
	for v in L:p=p*v
	return p
