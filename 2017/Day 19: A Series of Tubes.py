#!/usr/bin/env python
# -*- coding: utf-8 -*-
grid=open("d19.txt").read().split("\n\n")[1].splitlines()
for rn,l in enumerate(grid) :print(rn,l)
start=(0,grid[0].index("|"))
maxrow=len(grid)-1
maxcol=len(grid[0])-1

print(start, maxrow, maxcol)
south=(1,0)
north=(-1,0)
east=(0,1)
west=(0,-1)
print(south,north,east,west)
dr,dc=south
cr,cc=start
go=True
path=""
step=1
symbols=set(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

while go:
	print(f"step {step} packet at row {cr} column {cc} curpath {path}")
	nr=cr+dr
	nc=cc+dc
	if 0<=nr<=maxrow and 0<=nc<=maxcol:
		ns=grid[nr][nc]
		if ns in symbols:path+=ns
		# ~ if ns!="+":
		cr,cc=nr,nc
		step+=1
		if ns=="+":
			if dr:
				if grid[cr][cc-1]==" ":dr,dc=east
				else:dr,dc=west
			elif grid[cr-1][cc]==" ":dr,dc=south
			else:dr,dc=north
	else:
		print(path,step)
		exit()
	# ~ input()
print("consider the step for appearance of L symbol")
