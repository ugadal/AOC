z=str.maketrans("01","10")
def pairs(s):
	p=0
	while p<len(s):
		yield "1" if s[p]==s[p+1] else "0"
		p+=2
def chks(a,ms):
	r=ext(a,ms)
	cs="".join([*pairs(r)])
	while len(cs)%2==0:
		cs="".join([*pairs(cs)])
	return cs
def ext(a,ms):
	while len(a)<ms:
		b=a[::-1].translate(z)
		a=a+"0"+b
	return(a[:ms])
print(chks("10000",20))
print(chks("11011110011011101",272))
print(chks("11011110011011101",35651584))
