#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
fe="exp20.txt"
fr="day20.txt"
D={}
high="high"
low="low"
count={low:0,high:0}
totreat=[]
class fliflop():
	def __init__(self,name):
		self.name=name
		self.state=False
		self.outcontacts=[]
		self.signal=""
		D[name]=self
		
	def receives(self,parent,signal):
		if signal==high:return False
		self.state=not self.state
		self.signal=high if self.state else low
		return True
	def addcontact(self,contact):
		self.outcontacts.append(contact)
		if contact.__class__!=self.__class__:
			contact.addparent(self)
	def fire(self):
		for contact in self.outcontacts:
			print(f"{self.name} sends {self.signal} -> {contact.name} {pushed}")
			# ~ count[self.signal]+=1
			if contact.receives(self,self.signal):totreat.append(contact)
class broadcaster(fliflop):
	def fire(self):
		for contact in self.outcontacts:
			print(f"{self.name} sends {low} -> {contact.name} {pushed}")
			# ~ count[low]+=1
			if contact.receives(self,low):totreat.append(contact)
	def addcontact(self,contact):
		self.outcontacts.append(contact)
	
class conjun():
	def __init__(self,name):
		self.name=name
		self.outcontacts=[]
		self.incontacts={}
		D[name]=self
	def receives(self,parent,signal):
		self.incontacts[parent]=signal
		self.signal=high if list(self.incontacts.values()).count(low) else low
		return True
	def addparent(self,parent):
		self.incontacts[parent]=low
	def addcontact(self,contact):
		self.outcontacts.append(contact)
		if contact.__class__==self.__class__:
			contact.addparent(self)
	def fire(self):
		for contact in self.outcontacts:
			print(f"{self.name} sends {self.signal} -> {contact.name} {pushed}")
			# ~ count[self.signal]+=1
			if contact.receives(self,self.signal):totreat.append(contact)
rx=conjun("rx")
def special(parent,signal):
	if signal=="low":
		print ("found",pushed)
		exit()
rx.receives=special
	
conn=open(fr).read().splitlines()
for line in conn:
	name,cont=line.split(" -> ")
	if name.startswith("%"):
		fliflop(name[1:])
	elif name.startswith("&"):
		conjun(name[1:])
	else:broadcaster(name)
for line in conn:
	# ~ print (line)
	name,cont=line.split(" -> ")
	if name=="broadcaster":me=D["broadcaster"]
	else:me=D[name[1:]]
	cont=[D[contact] for contact in cont.split(", ")]
	for contact in cont:me.addcontact(contact)
		
# ~ print(D)
pushed=0
while True:
	pushed+=1
	print(pushed)
# ~ for _ in range(1000):
	s=D["broadcaster"]
	s.fire()
	while totreat:
		s=totreat.pop(0)
		s.fire()
	# ~ print(count)
	# ~ input()
print(count)
print(count[high]*(1000+count[low]))
