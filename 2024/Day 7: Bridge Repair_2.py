#!/usr/bin/env python3
#
sep="\n\n"
fn,part="d7.txt",1
data=open(fn).read().split(sep)[part].splitlines()

def possible(target,status,elements):
	# ~ print(f"entered with {target} {status} {elements}")
	if elements:
		for z in possible(target,status+elements[0],elements[1:]):yield z
		for z in possible(target,status*elements[0],elements[1:]):yield z
		ns=int(str(status)+str(elements[0]))
		for z in possible(target,ns,elements[1:]):yield z
	else:
		if status==target:yield True
		else:yield False
ok=0
for line in data:
	target,elements=line.split(": ")
	target=int(target)
	elements=[int(x) for x in elements.split()]
	if any(possible(target,elements[0],elements[1:])):ok+=target
print(ok)
