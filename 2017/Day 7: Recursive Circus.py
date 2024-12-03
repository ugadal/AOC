#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Day 7: Recursive Circus.py
#  
#  Copyright 2024 cecile <cecile@cecile-iMac>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
from mylib import manager

class disk():
	def __init__(self,key):
		# ~ print("created",key)
		self.name=key
		self.parents=None
		self.kids=[]
		self.weight=None
	def wei(self):
		return self.weight+sum([k.wei() for k in self.kids])
		

def main(args):
	dp=manager(disk)
	for line in open("d7.txt").read().splitlines():
		key=line.split()[0]
		to=dp.get(key)
		if len(line.split(" -> "))==2:
			kw,kids=line.split(" -> ")
			# ~ to.weight=weight
			for k in kids.split(", "):
				tk=dp.get(k)
				tk.parents=to
				to.kids.append(tk)
			line=kw
		weight=int(line.split("(")[1][:-1])
		to.weight=weight
	for ad in dp.data.values():
		if ad.kids and not ad.parents:
			print(ad.name) 
			root=ad
	print(root.wei())
	current=root
	while True:
		for kid in current.kids:print(kid.name,kid.wei())
		lw=[kid.wei() for kid in current.kids]
		if 0<len(lw)<=2:
			print("not easilly decidable")
			exit()
		if len(set(lw))==2:
			minseen=min(lw.count(k) for k in set(lw))
			weighttocorrect=next(k for k in set(lw) if lw.count(k)==1)
			nc=next(kid for kid in current.kids if kid.wei()==weighttocorrect)
			print(nc.name)
			current=nc
			input()
	print (1571-66)
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
