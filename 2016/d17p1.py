from hashlib import md5
def go(s):
	h=md5(s.encode()).hexdigest()[:4]
	AccD=[(p,d) for s,p,d in zip(h,"UDLR",((0,-1),(0,1),(-1,0),(1,0))) if s in "bcdef"]
	return AccD
def bfs(sp):
	r=c=0
	goal=(3,3)
	todo=[(r,c,sp)]
	best=0
	while todo:
		nxttodo=[]
		for cr,cc,cp in todo:
			if cr==cc==3:
				if len(cp)>best:
					best=len(cp)
				continue
					
			for tp,(dr,dc) in go(cp):
				if not 0<=cr+dr<=3 :continue
				if not 0<=cc+dc<=3 :continue
				nxttodo.append((cr+dr,cc+dc,cp+tp))
		todo=nxttodo
	print(best-len(sp))
	
bfs("ihgpwlah")
bfs("kglvqrro")
bfs("ulqzkmiv")
bfs("dmypynyp")
