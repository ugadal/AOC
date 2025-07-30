BEGIN {elf=1}
/^$/ {	print sum,elf
		sum=0
		elf++}
/^./ {sum=sum + $1}
END {print sum,elf,"last"}
