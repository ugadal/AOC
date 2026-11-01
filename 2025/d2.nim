import strutils
import sequtils

proc invalid(s: string): bool =
  let L = s.len
  if L mod 2 != 0: return false
  
  let half = L div 2
  if s[0 ..< half] == s[half .. ^1]: 
    return true
  return false

var count=0
for r in open("d2.txt").readline().split(","):
  let p=r.split("-").map(parseint)
  let d=p[0]
  let f=p[1]
  for x in d .. f:
    if invalid($x):count+=x
echo "p1 : ",count

proc invbis(s:string):bool=
  let L=s.len
  var c,sub=""
  for rl in countdown(L div 2, 1, 1):
    var ok = true
    if (L mod rl) != 0 : continue
    c = s[0..<rl]
    for p in countup(rl,L-1,rl):
      sub = s[p..<p+rl]
      if sub != c:
        ok=false
        break
    if ok: return true
  return false
    
count=0
for r in open("d2.txt").readline().split(","):
  let p=r.split("-").map(parseint)
  let d=p[0]
  let f=p[1]
  for x in d .. f:
    if invbis($x):count+=x
echo "p2 : ",count
