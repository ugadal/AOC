
// {
# ~ print $0
split($0,E,",")
pa=E[1]
pb=E[2]
split(pa,x,"-")
split(pb,y,"-")
a=x[1]
b=x[2]
c=y[1]
d=y[2]
delete symbol
for (i=a;i<=b;i++) {symbol[i]++}
for (i=c;i<=d;i++) {symbol[i]++}
for (key in symbol) {
	if (symbol[key] >1) {count++
						print $0
						break}
	}
}
END {print count}
