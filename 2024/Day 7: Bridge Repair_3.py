#!/usr/bin/env python3
#
sep="\n\n"
fn,part="d7.txt",1
data=open(fn).read().split(sep)[part].splitlines()

def possible(target,status,elements):
	# ~ print(f"entered with {target} {status} {elements}")
	if elements:
		added=status+elements[0]
		a=possible(target,status+elements[0],elements[1:])
		m=possible(target,status*elements[0],elements[1:])
		ns=int(str(status)+str(elements[0]))
		c=possible(target,ns,elements[1:])
		return a or m or c
	else:
		if status==target:return True
		return  False
ok=0
for line in data:
	target,elements=line.split(": ")
	target=int(target)
	elements=[int(x) for x in elements.split()]
	if possible(target,elements[0],elements[1:]):ok+=target
print(ok)
