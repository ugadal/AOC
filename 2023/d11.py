#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ~ import numpy as np
# ~ import pandas as pd
import itertools as it
fn="d11.txt"
ex="""...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""
# ~ G=np.array([[c for c in row] for row in ex.strip().splitlines()])
# ~ G=np.array([[c for c in row] for row in open(fn).read().strip().splitlines()])
# ~ df=pd.DataFrame(G)
# ~ print(df)
# ~ EXP=[]
# ~ for r,row in enumerate(G):
	# ~ EXP.append(row)
	# ~ if np.sum(row=="#")==0:EXP.append(row)
# ~ G=np.array(EXP)
# ~ df=pd.DataFrame(G)
# ~ print(df)
# ~ G=G.transpose()
# ~ EXP=[]
# ~ for r,row in enumerate(G):
	# ~ EXP.append(row)
	# ~ if np.sum(row=="#")==0:EXP.append(row)
# ~ G=np.array(EXP)
# ~ G=G.transpose()
# ~ df=pd.DataFrame(G)
# ~ GAL=[(r,c) for r,row in enumerate(G) for c,s in enumerate(row) if s=="#"]
# ~ D=0
# ~ for a,b in it.combinations(GAL,2):
	# ~ print(a,b)
	# ~ i,j=a
	# ~ k,l=b
	# ~ D+=abs(k-i)+abs(l-j)
# ~ print(D)



# ~ p2
# ~ G=np.array([[c for c in row] for row in ex.strip().splitlines()])
G=[[c for c in row] for row in open(fn).read().strip().splitlines()]
LineFrontiers=[a for a,L in enumerate(G) if all(s=="." for s in L)]
ColFrontiers=[a for a,L in enumerate(zip(*G)) if all(s=="." for s in L)]
print(LineFrontiers,ColFrontiers)

GAL=[(r,c) for r,row in enumerate(G) for c,s in enumerate(row) if s=="#"]
D=0
for a,b in it.combinations(GAL,2):
	i,j=a
	k,l=b
	lr=(min(i,k),max(i,k))
	cr=(min(j,l),max(j,l))
	td=abs(k-i)+abs(l-j)
	chf=len([True for x in range(*lr) if x in LineFrontiers])
	cvf=len([True for x in range(*cr) if x in ColFrontiers])
	td+=999999*(chf+cvf)
	D+=td
print(D)
