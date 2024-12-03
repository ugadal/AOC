z=open("step")
a,b=map(float,z.readline().split())
for l in z:
	c,d=map(float,l.split())
	print (c-a,d-b)
	a,b=c,d
