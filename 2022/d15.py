#!/usr/bin/env python
# -*- coding: utf-8 -*-
exp="""Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3"""
S=set()
B=set()
R=set()
pos=2000000
# ~ for line in exp.splitlines():
for line in open("d15.txt").read().strip().splitlines():
	sx=line.split("=")[1].split(",")[0]
	sy=line.split("=")[2].split(":")[0]
	bx=line.split("=")[3].split(",")[0]
	by=line.split("=")[4]
	sx,sy,bx,by=map(int,(sx,sy,bx,by))
	print(sx,sy,bx,by)
	S.add(sx+sy*1j)
	B.add(bx+by*1j)
	dsb=abs(bx-sx)+abs(by-sy)
	print(dsb)
	rest=dsb-abs(sy-pos)
	print(f"rest:{rest}")
	for dx in range(-rest,rest+1):
		R.add(sx+dx+pos*1j)
	# ~ for dx in range(-dsb,dsb+1):
		# ~ rest=dsb-abs(dx)
		# ~ for dy in range(-rest,rest+1):
			# ~ R.add(sx+dx+(sy+dy)*1j)

rocks=len([x for x in R if x.imag==pos])
beacons=len([x for x in B if x.imag==pos])
sensors=len([x for x in S if x.imag==pos])
print(rocks,beacons,sensors)
print(rocks-beacons-sensors)
