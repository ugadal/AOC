import std/os
import sequtils
import strutils
import math
import algorithm

let nomFichierSource = currentSourcePath().extractFilename()
let nomSansExtension = nomFichierSource.splitFile().name

let da1 = nomSansExtension & "_p1.txt"
#~ let d="""4<3 2<5 3>1 1>2 1<5 4<1 3>2 4<2 3>5 4<5
#~ 4>1 2>1 3>2 1<5 4>5 2<5 3>1 4>3 2<4 5<3
#~ 5>1 5>2 4>1 2<4 3>2 3<4 1>2 3>5 1<3 4>5"""
var res=0
var kres: seq[char]
proc khansort(s:string): int =
  var p: char
  var P,G: set[char]
  var pairs : seq[tuple[a:char,b:char]]
  var lp : tuple[a:char,b:char]
  for pair in s.split:
    var c=pair[1]
    if c=='<': pairs.add((pair[0],pair[2]))
    else: pairs.add((pair[2],pair[0]))
  while pairs.len>1:
    P={}
    G={}
    for pair in pairs:
      echo pair
      P.incl(pair.a)
      G.incl(pair.b)
    echo P
    echo G
    echo P-G
    p=toseq(P-G)[0]
    kres.add(p)
    echo kres
    pairs.keepItIf(it.a != p)
    echo pairs
    lp=pairs[0]
    kres.add(lp.a)
    kres.add(lp.b)
    echo "res ",kres
  return kres.reversed.join("").parseint


###var p,c : char
###var P,G: set[char]
###var pairs : seq[tuple[a:char,b:char]]
###var lp : tuple[a:char,b:char]
###var res : seq[char]
###for l in d.splitlines:
###  echo "line ",l
###  res = @[]
###  pairs = @[]
###  for pair in l.split:
###    #~ echo pair
###    c=pair[1]
###    if c=='<': pairs.add((pair[0],pair[2]))
###    else: pairs.add((pair[2],pair[0]))
###  echo pairs
###  while pairs.len>1:
###    P={}
###    G={}
###    for pair in pairs:
###      echo pair
###      P.incl(pair.a)
###      G.incl(pair.b)
###    echo P
###    echo G
###    echo P-G
###    p=toseq(P-G)[0]
###    res.add(p)
###    echo res
###    pairs.keepItIf(it.a != p)
###    echo pairs
###  lp=pairs[0]
###  res.add(lp.a)
###  res.add(lp.b)
###  echo "res ",res

proc comparerRegles(x, y: char, regles: string): int =
  if ($x & "<" & $y) in regles or ($y & ">" & $x) in regles: return -1
  elif ($y & "<" & $x) in regles or ($x & ">" & $y) in regles: return 1
  else: return 0

var elements = @['1', '2', '3', '4', '5']

for l in open(da1).lines:
  elements.sort(proc (x, y: char): int = comparerRegles(x, y, l))
  res+=elements.reversed.join("").parseint

echo "p1 : ",res
res=0
#~ let d="""4<3 2<5 3>1 1>2 1<5 4<1 3>2 4<2 3>5 4<5
#~ 4>1 2>1 3>2 1<5 4>5 2<5 3>1 4>3 2<4 5<3
#~ 5>1 5>2 4>1 2<4 3>2 3<4 1>2 3>5 1<3 4>5"""
let d="""2<5 3>1 1>2 1<5 4<1 3>2 4<2 3>5 4<5
2>1 3>2 1<5 4>5 2<5 3>1 4>3 2<4 5<3
5>1 5>2 4>1 3>2 3<4 1>2 3>5 1<3 4>5"""
for l in d.splitlines:
  elements.sort(proc (x, y: char): int = comparerRegles(x, y, l))
  echo elements
  echo l," ",khansort(l)
  res+=elements.reversed.join("").parseint
echo "p2 : ",res
