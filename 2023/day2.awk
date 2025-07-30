BEGIN {sum=0}
/^A X/ {	sum+=4}
/^A Y/ {	sum+=6}
/^A Z/ {	sum+=3}
/^B X/ {	sum+=7}
/^B Y/ {	sum+=5}
/^B Z/ {	sum+=3}
/^C X/ {	sum+=7}
/^C Y/ {	sum+=2}
/^C Z/ {	sum+=6}
END {print sum}
