#!/usr/bin/env python3
#
# ~ from functools import cache
from collections import deque
sep="\n\n"
fn,part="d21.txt",0

# ~ +---+---+---+
# ~ | 7 | 8 | 9 |
# ~ +---+---+---+
# ~ | 4 | 5 | 6 |
# ~ +---+---+---+
# ~ | 1 | 2 | 3 |
# ~ +---+---+---+
    # ~ | 0 | A |
    # ~ +---+---+
tbt=[complex(col,-row) for row in range(4) for col in range(3)]
kp={s:k for s,k in zip(list("X0A123456789"),tbt)}
for s,k in zip(list("X0A123456789"),tbt):kp[k]=s
print(kp)
tbt=[complex(col,-row) for row in range(2) for col in range(3)]
# ~ dip={s:k for s,k in zip(list("<v>X^A"),tbt)}
dip={s:k for s,k in zip(list("LDRXTA"),tbt)}
for s,k in zip(list("LDRXTA"),tbt):dip[k]=s
print(dip)
# ~ for p in ["029A","980A","179A","456A","379A"]:
ndp=2
todo=[(["A"]*(ndp+1),"","","029A","",0)]
visited={}
while todo:
	cv=todo.pop(0)
	fp,cip,ctar,toemit,emitted,sd=cv
	print(f"working on fingerpositions {fp} current input {cip} current target {ctar} toemit:{toemit} emitted:{emitted} stepsdone:{sd}")
	if sd>=visited.get(str(cv),float("inf")):
		print("skipping")
		continue
	if cip:
		tarkp=dip if ctar else kp
		cpos=tarkp[fp[ctar]]
		print(f"cpos {cpos} {type(cpos)}")
		if cip=="A":
			if ctar==0:
				print(f"keypad emits {fp[0]}")
				if emitted+fp[0] == toemit:
					print(f"stepdone {sd}")
					input()
				if toemit.startswith(emitted+fp[0]):
					print(f"stepdone {sd}")
					todo.append((fp.copy(),"",None,toemit,emitted+fp[0],sd+1))
					visited[str(cv)]=sd
				continue
			todo.append((fp.copy(),fp[ctar],ctar-1,toemit,emitted,sd+1))
			visited[str(cv)]=sd
			continue
		match cip:
			case 'T':
				np=tarkp.get(cpos-1j,"X")
				if np=="X":continue
				nfp=fp.copy()
				nfp[ctar]=np
				todo.append((nfp,"",None,toemit,emitted,sd+1))
				visited[str(cv)]=sd
			case 'L':
				np=tarkp.get(cpos-1,"X")
				if np=="X":continue
				nfp=fp.copy()
				nfp[ctar]=np
				todo.append((nfp,"",None,toemit,emitted,sd+1))
				visited[str(cv)]=sd
			case 'D':
				np=tarkp.get(cpos+1j,"X")
				if np=="X":continue
				nfp=fp.copy()
				nfp[ctar]=np
				todo.append((nfp,"",None,toemit,emitted,sd+1))
				visited[str(cv)]=sd
			case 'R':
				np=tarkp.get(cpos+1,"X")
				if np=="X":continue
				nfp=fp.copy()
				nfp[ctar]=np
				todo.append((nfp,"",None,toemit,emitted,sd+1))
				visited[str(cv)]=sd
		continue
	for s in list("LDRTA"):
		todo.append((fp,s,ndp,toemit,emitted,sd))
	visited[str(cv)]=sd
print(visited)
