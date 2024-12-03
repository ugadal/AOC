# ~ from mylib import memoize,debug
fr=open('d18.txt').readline().strip()
# ~ fr=".^^.^.^^^^"
# ~ @debug
# ~ @memoize
def nr(s):
	lr=len(s)
	s="."+s+"."
	nl=""
	for p in range(lr):
		match s[p:p+3]:
			case '^^.':nl+="^"
			case '.^^':nl+="^"
			case '^..':nl+="^"
			case '..^':nl+="^"
			case _:nl+="."
	return nl
tt=fr.count(".")
for _ in range(399999):
	fr=nr(fr)
	tt+=fr.count(".")
print(tt)
