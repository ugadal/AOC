#!/usr/bin/env python
# -*- coding: utf-8 -*-
cs="A"
pos=0
D={}
# ~ Perform a diagnostic checksum after 12523873 steps.
for s in range(12523873):
	match cs:
		case "A":
			if D.get(pos,0)==0:
				D[pos]=1
				pos+=1
				cs="B"
			else:
				D[pos]=1
				pos-=1
				cs="E"
		case "B":
			if D.get(pos,0)==0:
				D[pos]=1
				pos+=1
				cs="C"
			else:
				D[pos]=1
				pos+=1
				cs="F"
		case "C":
			if D.get(pos,0)==0:
				D[pos]=1
				pos-=1
				cs="D"
			else:
				D[pos]=0
				pos+=1
				cs="B"
		case "D":
			if D.get(pos,0)==0:
				D[pos]=1
				pos+=1
				cs="E"
			else:
				D[pos]=0
				pos-=1
				cs="C"
		case "E":
			if D.get(pos,0)==0:
				D[pos]=1
				pos-=1
				cs="A"
			else:
				D[pos]=0
				pos+=1
				cs="D"
		case "F":
			if D.get(pos,0)==0:
				D[pos]=1
				pos+=1
				cs="A"
			else:
				D[pos]=1
				pos+=1
				cs="C"

print(sum(D.values()))
