import std/os
import sequtils
import strutils
import math
import algorithm

let nomFichierSource = currentSourcePath().extractFilename()
let nomSansExtension = nomFichierSource.splitFile().name
proc 
let da1 = nomSansExtension & "_p1.txt"
var res=0
for l in open(da1).lines:
  echo l
  var tl=l[4..^1]
  tl=tl.split
  
  #~ elements.sort(proc (x, y: char): int = comparerRegles(x, y, l))
  #~ res+=elements.reversed.join("").parseint

#~ echo "p1 : ",res

#~ res=0
#~ let da2 = nomSansExtension & "_p2.txt"
#~ for l in open(da2).lines:
  #~ res+=khansort(l)
#~ echo "p2 : ",res

#~ let da3 = nomSansExtension & "_p3.txt"
#~ res=0
#~ for l in open(da3).lines:
  #~ res+=khansort(l)
#~ echo "p3 : ",res
