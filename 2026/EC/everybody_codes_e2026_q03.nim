import std/os
import sequtils
import strutils
import math
import algorithm

let nomFichierSource = currentSourcePath().extractFilename()
let nomSansExtension = nomFichierSource.splitFile().name
proc fana(s:string):int=
  var base=s[4..7]
  var coeff=s[9..12]
  var res=0
  for exp in countdown(3,0,1):
    var i=3-exp
    var c=parseint($coeff[i])
    res+=($coeff[i]).parseint * ($base[i]).parseint ^ exp
  return res
let da1 = nomSansExtension & "_p1.txt"
var res=0
let exdata="""ISO-3210 7654
ISO-8742 2468
ISO-1111 1111"""
var ttl=0
for l in open(da1).lines:
#~ for l in exdata.splitlines:
  var res=fana(l)
  ttl+=res
  echo res
echo "p1 : ",ttl

proc fanb(s:string):int=
  var ls=s[4..^1]
  var parts=ls.split
  var base=parts[0]
  var coeff=parts[1]
  #~ var res=0
  #~ for exp in countdown(3,0,1):
    #~ var i=3-exp
    #~ var c=parseint($coeff[i])
    #~ res+=($coeff[i]).parseint * ($base[i]).parseint ^ exp
  return 1


let d2ex="""ISO-3210 7654
ISO-8742 2468
ISO-1 1111
ISO-13 777
ISO-34 140856
ISO-789 2465112
ISO-2341 945"""
let da2 = nomSansExtension & "_p2.txt"
ttl=0
#~ for l in open(da1).lines:
for l in d2ex.splitlines:
  echo fanb(l)
  #~ var res=fanb(l)
  ttl+=res
  echo res
echo "p2 : ",ttl

  #~ var tl=l[4..^1]
