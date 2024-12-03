#!/usr/bin/env python3
#
#  Day 5: A Maze of Twisty Trampolines, All Alike.py
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
V=list(map(int,open(0).read().splitlines()))
lv=len(V)
pos=0
step=0
while pos<lv:
	step+=1
	off=V[pos]
	V[pos]+=1
	pos+=off
print(step)
