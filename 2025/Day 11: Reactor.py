#!/usr/bin/env python3
#
from malib import *
data=open(fn).read().split(sep)[part]
# ~ nodes=set()
R={}
for line in data.splitlines():
	f,t=line.split(":")
	R[f]=[]
	for n in t.split():
		R[n]=[]
for line in data.splitlines():
	f,t=line.split(": ")
	for n in t.split():
		R[f].append(n)
# ~ print(R)
def solve(path,out="out"):
	lp=path[-1]
	if lp==out:yield path
	else:
		# ~ print("branch",path,R[lp])
		for target in R[lp]:
			yield from solve(path+[target],out)
class node():
	all={}
	def __init__(self,name):
		self.name=name
		self.left=[]
		self.right=[]
		self.tofft=False
		self.todac=False
		node.all[name]=self
		self.toout=0
	def TO(self):
		if self.toout:return self.toout
		self.toout=sum(n.TO() for n in self.right)
		return self.toout
for line in data.splitlines():
	f,t=line.split(": ")
	node(f)
	for n in t.split():
		node(n)
for line in data.splitlines():
	f,t=line.split(": ")
	f=node.all[f]
	for n in t.split():
		n=node.all[n]
		n.left.append(f)
		f.right.append(n)
fft=node.all["fft"]
todo=[fft]
while todo:
	cn=todo.pop()
	for nx in cn.left:
		if nx.tofft:continue
		nx.tofft=True
		todo.append(nx)
todo=[fft]
while todo:
	cn=todo.pop()
	for nx in cn.right:
		if nx.tofft:continue
		nx.tofft=True
		todo.append(nx)
dac=node.all["dac"]
todo=[dac]
while todo:
	cn=todo.pop()
	for nx in cn.left:
		if nx.todac:continue
		nx.todac=True
		todo.append(nx)
todo=[dac]
while todo:
	cn=todo.pop()
	for nx in cn.right:
		if nx.todac:continue
		nx.todac=True
		todo.append(nx)
keep=[n for n in node.all.values() if n.tofft and n.todac]
keep.append(fft)
keep.append(dac)
drop=[n for n in node.all.values() if n not in keep]
print(len(keep),len(node.all),len(drop))
for n in keep:print(n.name)
drop=set(drop)
for n in keep:
	n.left=set(n.left)-drop
	n.right=set(n.right)-drop
node.all["out"].toout=1
print(node.all["svr"].TO())
