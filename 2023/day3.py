#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ~ 467..114..
# ~ ...*......
# ~ ..35..633.
# ~ ......#...
# ~ 617*......
# ~ .....+.58.
# ~ ..592.....
# ~ ......755.
# ~ ...$.*....
# ~ .664.598..

dig=[str(x) for x in range(10)]
ns=dig+["."]

def indata():
	fn="day3.txt"
	with open(fn) as f:	return f.read().split("\n")
def wherein(s,what):
	return [p for p,s in enumerate(s) if s in what]
	
def notwherein(s,what):
	return [p for p,s in enumerate(s) if not s in what]
	
def getsymbol(s):return notwherein(s,ns)

def getdigit(s):return wherein(s,dig)

def getstars(s):return wherein(s,["*"])

def getnumaround(sp,A,B,C):
	print(sp)
	print(A)
	print(B)
	print(C)
	Z=[]
	# ~ top
	cl=[False]*len(A)
	try: 
		pos=sp
		while A[pos] in dig:
			cl[pos]=True
			pos-=1
	except:None	
	try: 
		pos=sp
		while A[pos-1] in dig:
			cl[pos-1]=True
			pos-=1
	except:None	
	try: 
		pos=sp
		while A[pos+1] in dig:
			cl[pos+1]=True
			pos+=1
	except:None	
	keep="".join(rep(s,b) for s,b in zip(A,cl))
	print(keep,"Akeep")
	Z.extend(keep.split())
	# ~ bottom
	cl=[False]*len(C)
	try: 
		pos=sp
		while C[pos] in dig:
			cl[pos]=True
			pos-=1
	except:None	
	try: 
		pos=sp
		while C[pos-1] in dig:
			cl[pos-1]=True
			pos-=1
	except:None	
	try: 
		pos=sp
		while C[pos+1] in dig:
			cl[pos+1]=True
			pos+=1
	except:None	
	keep="".join(rep(s,b) for s,b in zip(C,cl))
	print(keep,"Ckeep")
	Z.extend(keep.split())
	# ~ middle
	cl=[False]*len(B)
	try: 
		pos=sp
		while B[pos-1] in dig:
			cl[pos-1]=True
			pos-=1
	except:None	
	try: 
		pos=sp
		while B[pos+1] in dig:
			cl[pos+1]=True
			pos+=1
	except:None		
	keep="".join(rep(s,b) for s,b in zip(B,cl))
	print(keep,"Bkeep")
	Z.extend(keep.split())
	print (sp,Z)
	# ~ input()
	if len(Z)==2:
		print(Z)
		return int(Z[0])*int(Z[1])
	return 0
def rep(s,b):
	if b:return s
	return " "
def ana(B,SA,SB,SC):
	cl=[False]*len(B)
	for sp in SA+SC:
		try: 
			pos=sp
			while B[pos] in dig:
				cl[pos]=True
				pos-=1
		except:None
		try: 
			pos=sp
			while B[pos-1] in dig:
				cl[pos-1]=True
				pos-=1
		except:None
		try: 
			pos=sp
			while B[pos] in dig:
				cl[pos]=True
				pos+=1
		except:None
		try: 
			pos=sp
			while B[pos+1] in dig:
				cl[pos+1]=True
				pos+=1
		except:None
	for sp in SB:
		try: 
			pos=sp
			while B[pos-1] in dig:
				cl[pos-1]=True
				pos-=1
		except:None
		try: 
			pos=sp
			while B[pos+1] in dig:
				cl[pos+1]=True
				pos+=1
		except:None
	keep="".join(rep(s,b) for s,b in zip(B,cl))
	return (keep.split())	
def main(args):
	lines=[_.strip() for _ in indata()]
	V=[]
	SA=[]
	SB=getsymbol(lines[0])
	SC=getsymbol(lines[1])
	B=lines[0]
	SYMOK=[]
	res=ana(B,SA,SB,SC)
	print(B)
	print(res)
	V.extend(res)
	for B,nextline in zip(lines[1:],lines[2:]):
		SA=list(SB)
		SB=list(SC)
		SC=getsymbol(nextline)
		res=ana(B,SA,SB,SC)
		print (B)
		print(res)
		V.extend(res)
	print(sum(map(int,V)))
	V=[]
	A,B,C=lines[:3]
	for A,B,C in zip(lines,lines[1:],lines[2:]):
		for p in getstars(B):
			V.append(getnumaround(p,A,B,C))
			print(V)
		# ~ input()
	print(sum(V))
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
