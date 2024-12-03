#!/usr/bin/env python3
#
#  Day 6: Memory Reallocation.py
#  
#  Copyright 2024 System user; root <root@dcsysd>
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


import sys


def main(args):
	V=list(map(int,open(0).read().split()))
	lv=len(V)
	seen=[hash(str(V))]
	step=0
	while True:
		step+=1
		t=next(((i,v) for i,v in enumerate(V) if v==max(V)))
		V[t[0]]=0
		# ~ print(lv,t)
		ag=t[1]//lv
		if ag:V=[v+ag for v in V]
		if t[1]%lv:
			for pos in [(t[0]+x+1)%lv for x in range(t[1]%lv)]:
				V[pos]+=1
				
		# ~ print(V)
		nh=hash(str(V))
		if nh in seen:
			print(step)
			seen=[]
			step=0
			# ~ break
		seen.append(nh)
		# ~ print(seen)
	return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
