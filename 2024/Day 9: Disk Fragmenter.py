#!/usr/bin/env python3
#
sep="\n\n"
fn,part="d9.txt",1
data=open(fn).read().split(sep)[part].strip()
data=[c for c in data]
r=sum(map(int,data))
print(r)
print(data[:10],"...")
fs=data.copy()
cm=[]
fid=0
while True:
	fl=int(fs.pop(0))
	cm.extend([fid]*fl)
	try:sl=int(fs.pop(0))
	except:break
	cm.extend([-1]*sl)
	fid+=1
print(len(cm),cm[:400],"...")
pos=0
while pos<len(cm):
	if cm[pos]!=-1:
		pos+=1
		continue
	lv=cm.pop()
	while lv==-1:lv=cm.pop()
	cm[pos]=lv
	pos+=1
print(cm)
res=sum(p*v for p,v in enumerate(cm))
print(res)
