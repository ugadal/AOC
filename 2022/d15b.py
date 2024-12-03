#!/usr/bin/env python
# -*- coding: utf-8 -*-
from shapely import Polygon
dim=4000000
M=Polygon([(-.5,-.5),(dim+.5,-.5),(dim+.5,dim+.5),(-.5,dim+.5)])
for line in open("d15.txt").read().strip().splitlines():
	sx=line.split("=")[1].split(",")[0]
	sy=line.split("=")[2].split(":")[0]
	bx=line.split("=")[3].split(",")[0]
	by=line.split("=")[4]
	sx,sy,bx,by=map(int,(sx,sy,bx,by))
	dsb=abs(bx-sx)+abs(by-sy)
	dsb+=.5
	M=M-Polygon([(sx-dsb,sy),(sx,sy-dsb),(sx+dsb,sy),(sx,sy+dsb)])
print (M.centroid.x*4000000+M.centroid.y)
