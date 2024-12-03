from copy import deepcopy as deec
import re
extractor=re.compile("/dev/grid/node-x(\d+)-y(\d+)\s+(\d+)T\s+(\d+)T\s+(\d+)T\s+(\d+)%")
O=[]
for line in open("d22.txt").read().splitlines()[2:]:
	v=list(map(int,extractor.match(line).groups()))
	O.append(v)
# ~ part 1
r=0
for a in O:
	if a[3]==0:continue
	for b in O:
		if b==a:continue
		if a[3]<=b[4]:r+=1
print(r)

# ~ part 2
# ~ 200 by thinking only
