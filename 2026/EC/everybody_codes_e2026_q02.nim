import std/os
import sequtils
import strutils
import math
import algorithm

let nomFichierSource = currentSourcePath().extractFilename()
let nomSansExtension = nomFichierSource.splitFile().name

let da1 = nomSansExtension & "_p1.txt"
var res=0
proc khansort(s:string): int =
  var p: char
  var P,G: set[char]
  var pairs : seq[tuple[a:char,b:char]]
  var lp : tuple[a:char,b:char]
  var kres: seq[char] = @[]
  for pair in s.split:
    var c=pair[1]
    if c=='<': pairs.add((pair[0],pair[2]))
    else: pairs.add((pair[2],pair[0]))
  while pairs.len>1:
    P={}
    G={}
    for pair in pairs:
      P.incl(pair.a)
      G.incl(pair.b)
    p=toseq(P-G)[0]
    kres.add(p)
    pairs.keepItIf(it.a != p)
  lp=pairs[0]
  kres.add(lp.a)
  kres.add(lp.b)
  return kres.reversed.join("").parseint

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
let da2 = nomSansExtension & "_p2.txt"
for l in open(da2).lines:
  res+=khansort(l)
echo "p2 : ",res

let da3 = nomSansExtension & "_p3.txt"
res=0
for l in open(da3).lines:
  res+=khansort(l)
echo "p3 : ",res
