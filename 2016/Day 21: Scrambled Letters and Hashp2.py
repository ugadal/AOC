import itertools as it
pw="abcde"
pw="abcdefgh"
pw=list(pw)
target=list("fbgdceah")
source="abcdefgh"
for comb in  it.permutations(source):
	pw=list(comb)
	# ~ print(pw)
	for inst in open("d21.txt").read().splitlines():
		match inst.split():
			case ["swap", "position", *arg]:
				a=int(arg[0])
				b=int(arg[3])
				pw[a],pw[b]=pw[b],pw[a]
			case ["swap", "letter",*arg]:
				a=arg[0]
				b=arg[3]
				pa=pw.index(a)
				pb=pw.index(b)
				pw[pa],pw[pb]=b,a
			case ["reverse", "positions", *arg]:
				a=int(arg[0])
				b=int(arg[2])
				if a:pw[a:b+1]=pw[b:a-1:-1]
				else:pw[a:b+1]=pw[b::-1]
			case ["rotate", "left", *arg]:
				a=int(arg[0])
				pw=pw[a:]+pw[:a]
			case ["rotate", "right", *arg]:
				a=int(arg[0])
				pw=pw[-a:]+pw[:-a]
			case ["move", "position", *arg]:
				a=int(arg[0])
				b=int(arg[3])
				s=pw.pop(a)
				pw.insert(b,s)
			case ["rotate", "based", "on", "position", "of", "letter", *arg]:
				s=arg[0]
				ps=pw.index(s)
				if ps>=4:ps+=2
				else:ps+=1
				# ~ print(ps)
				ps%=len(pw)
				# ~ print(ps)
				pw=pw[-ps:]+pw[:-ps]
	if pw==target:print(comb)
			
	
