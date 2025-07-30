exp="rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"

def hashthis(s):
	d=0
	for c in s:
		d+=ord(c)
		d*=17
		d%=256
	return d
	
l=open("d15.txt").readline().strip()
PARTS=l.split(",")
print (sum(hashthis(p) for p in PARTS ))
BOXES=[[] for _ in range(256)]

def equals(bname,focal):
	bnumber=hashthis(bname)
	box=BOXES[bnumber]
	lname=f"{bname} {focal}"
	torem=[i for i,p in enumerate(box) if p.startswith(bname)]
	print (torem)
	if torem:
		pos=torem[0]
		box[pos]=lname
	else:box.append(lname)
def minussign(bname):
	bnumber=hashthis(bname)
	box=BOXES[bnumber]
	torem=[i for i,p in enumerate(box) if p.startswith(bname)]
	torem.reverse()
	for p in torem:box.pop(p)
# ~ for p in exp.split(","):
for p in PARTS:
	print(p)
	if p.endswith("-"):
		bname=p[:-1]
		bnumber=hashthis(bname)
		minussign(bname)
	else:
		bname,lens=p.split("=")
		bnumber=hashthis(bname)
		lens=int(lens)
		equals(bname,lens)
	print(bnumber,BOXES[bnumber])
	# ~ input()
res=0
for bn,box in enumerate(BOXES):
	res+=(bn+1)*sum([(i+1)* int(v.split()[1]) for i,v in enumerate(box)])
print(res)
