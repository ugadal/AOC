import strutils,math

let 
  fn = "d1.txt"
  part = 1
  data = readFile(fn).split("\n\n")[part]
var res = 50
var count = 0
var v = 0
for l in data.strip.splitlines :
  v = parseInt(l[1..^1])
  case l[0]
  of 'L': res-=v
  of 'R': res+=v
  else: echo "wrong"  
  res = res mod 100
  if res==0 : count+=1
echo "p1 : ",count

var oldres=50
res=50
count=0

for l in data.strip.splitlines:
  v=parseint(l[1..^1])
  count+=v div 100
  v=v mod 100
  case l[0]
  of 'L': res-=v
  of 'R': res+=v
  else: echo "wrong"  
  if res==0:count+=1
  elif oldres!=0 and res!= floormod(res,100) :count+=1
  res=floormod(res,100)
  oldres=res  
echo "p2 : ",count
