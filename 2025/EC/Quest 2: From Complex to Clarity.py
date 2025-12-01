#!/usr/bin/env python3
#
A=complex(156,56)

R=complex(0,0)
for x in range(3):
	R=R*R
	R=complex(R.real//10,R.imag//10)
	R+=A
print(R,f"[{int(R.real)},{int(R.imag)}]")
count=0
A=complex(-79057,-15068)
# ~ A=complex(35300,-64910)
def validate(c,r):
	p=complex(0,0)
	for C in range(100):
		p=p*p
		p=complex(int(p.real/100000),int(p.imag/100000))
		p+=complex(c,r)
		if p.real < -1000000:return False,C,p
		if p.real >  1000000:return False,C,p
		if p.imag < -1000000:return False,C,p
		if p.imag >  1000000:return False,C,p
	return True,C+1,p
for c in range(int(A.real),int(A.real)+1001,10):
	for r in range(int(A.imag),int(A.imag)+1001,10):	
		p=complex(0,0)
		for C in range(100):
			p=p*p
			p=complex(int(p.real/100000),int(p.imag/100000))
			p+=complex(c,r)
			if p.real < -1000000:break
			if p.real >  1000000:break
			if p.imag < -1000000:break
			if p.imag >  1000000:break
		else:
			count+=1
print("p2 :",c,r,count)
count=0
for c in range(int(A.real),int(A.real)+1001):
	for r in range(int(A.imag),int(A.imag)+1001):	
		b,_,_=validate(c,r)
		if b:count+=1
print("p3 :",count)

# ~ print(validate(35630,-64880))
# ~ print(validate(35630,-64870))
# ~ print(validate(35640,-64860))
# ~ print(validate(36230,-64270))
# ~ print(validate(36250,-64270))
# ~ print(validate(35460, -64910))
# ~ print(validate(35470, -64910))
# ~ print(validate(35480, -64910))
# ~ print(validate(35680, -64850))
# ~ print(validate(35630, -64830))
