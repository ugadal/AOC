#!/usr/bin/env python3
#
# ~ Program: 2,4,1,3,7,5,0,3,1,5,4,4,5,5,3,0
a=55593699
a=25160 # 6>0
b=c=0
# ~ print(a,b,c)
def doit(a):
	ori=a
	z=[]
	while True:  
		b = a % 8 #reste de a/8
		b = b ^ 3 # b : 0 1 2 3 4 5 6 7 
		#            => 3 2 1 0 7 6 5 4
		#            => 8 4 2 1 128 64 32 16
		c = a >> b #
		a = a // 8
		b = b ^ 5
		b = b ^ c
		z.append(b%8)
		if not a:break
	return (ori,z)
a=0
target=[2,4,1,3,7,5,0,3,1,5,4,4,5,5,3,0]
for p in range(1,1+len(target)):
	subt=target[-p:]
	print(subt)
	while True:
		seed,res=doit(a)
		if res==subt:
			print(seed,res)
			break
		a+=1
	a*=8
	
