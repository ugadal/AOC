b=57*100+100000
h=0
c=b+17000
while True:
	f=1
	d=2
	while True:
		e=2
		while True:
			if b%d:break
			g=d*e-b
			if g==0:f=0
			e+=1
			g=e-b
			# ~ print(f"loop 3 {b} {c} {d} {e} {f} {g} {h}")
			if g==0:break
		d+=1
		g=d-b
		if g==0:break
		# ~ print(f"loop 2 {b} {c} {d} {e} {f} {g} {h}")
		# ~ input()
	if f==0:h+=1
	g=b-c
	if g==0:break
	b+=17
	print(f"loop 1 {b} {c} {d} {e} {f} {g} {h}")
print(f" main {b} {c} {d} {e} {f} {g} {h}")
"""
set b 57
set c b
jnz a 2
jnz 1 5
mul b 100
sub b -100000
set c b
sub c -17000
	set f 1
	set d 2
		set e 2
			set g d
			mul g e
			sub g b
			jnz g 2
			set f 0
			sub e -1
			set g e
			sub g b
			jnz g -8
		sub d -1
		set g d
		sub g b
		jnz g -13
	jnz f 2
	sub h -1
	set g b
	sub g c
	jnz g 2
	jnz 1 3
	sub b -17
	jnz 1 -23
"""
