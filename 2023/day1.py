#!/usr/bin/env python
# -*- coding: utf-8 -*-
def indata():
	fn="day1.txt"
	with open(fn) as f:
		return f.read().split("\n")
def treat(line):
	if not line:return 0
	D=[]
	# ~ print (line)
	for c in line:
		try:D.append(int(c))
		except:continue
	# ~ print(D)
	x=int(str(D[0])+str(D[-1]))
	# ~ print(x)
	return x
def treatb(line):
	if not line:return 0
	print (line)
	words=["one","two","three","four","five","six","seven","eight","nine"]
	dig=[str(x) for x in range(1,10)]
	last=(0,0)
	first=(len(line),0)
	for word,d in zip(words,dig):
		pos=0
		found=[]
		while line.find(word,pos)>=0:
			pos=line.find(word,pos)
			found.append(pos)
			pos+=1
		if found:
			p=found[0]
			if p<first[0]:
				first=(p,d)
			p=found[-1]
			if p<last[0]:
				last=(p,d)
	p,d=last
	print (p,d)
	L=list(line)
	L.insert(p,d)		
	p,d=first
	print(p,d)
	L.insert(p,d)		
	line="".join(L)
	
	D=[]
	print (line)
	for c in line:
		try:D.append(int(c))
		except:continue
	print(D)
	x=int(str(D[0])+str(D[-1]))
	print(x)
	return x
def main(args):
	lines=indata()
	sol=sum([treat(line) for line in lines])
	print(sol)
	sol=sum([treatb(line) for line in lines])
	print(sol)
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
