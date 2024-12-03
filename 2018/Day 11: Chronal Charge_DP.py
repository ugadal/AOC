#!/usr/bin/env python
# -*- coding: utf-8 -*-
mykey=2866
def comp(x,y):
	if x*y == 0:return 0
	rid=10+x
	pl=mykey+rid*y
	pl*=rid
	try:pl=int(str(pl)[-3])
	except:pl=0
	pl-=5
	return pl
SUMS=[]
R=[0]*301
SUMS.append(R)
for row in range(1,301):
	PR=SUMS[-1]
	R=[0]
	for diag,top,col in zip(PR,PR[1:],range(1,301)):
		R.append(R[-1]+top-diag+comp(col,row))
	SUMS.append(R)
rec=0
for ss in range(1,301):
	for col in range(1,301-ss):
		for row in range(1,301-ss):
			tl=SUMS[row-1][col-1]
			bl=SUMS[row+ss-1][col-1]
			tr=SUMS[row-1][col+ss-1]
			br=SUMS[row+ss-1][col+ss-1]
			V=br-tr-bl+tl
			if V>rec:
				rec=V
				print(col,row,ss,rec)
