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
    res +=  c * ($base[i]).parseint ^ exp
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
  var ls =s.split("-")[1]
  var parts=ls.split
  var base=parts[0]
  var coeff=parts[1]
  while base.len<coeff.len:
    base=base&base
  base=base[^coeff.len..^1]
  var lres=0
  for pos in countdown(coeff.len-1,0,1):
    var c=($coeff[pos]).parseint
    var b=($base[pos]).parseint
    lres+=c * b ^ (coeff.len-1-pos)
  return lres


let d2ex="""ISO-3210 7654
ISO-8742 2468
ISO-1 1111
ISO-13 777
ISO-34 140856
ISO-789 2465112
ISO-2341 945"""
let da2 = nomSansExtension & "_p2.txt"
ttl=0
for l in open(da2).lines:
#~ for l in d2ex.splitlines:
  #~ echo fanb(l)
  var res=fanb(l)
  ttl+=res
  echo res
echo "p2 : ",ttl

#~ proc smcf(v:int,c:string):int=
  #~ var lv=v
  #~ for pos in countdown(c.len-1,0,1):
    
proc fanc(s:string):bool=
  var ls =s.split("-")[1]
  var parts=ls.split
  var base=parts[0]
  var coeff=parts[1]
  while base.len<coeff.len:
    base=base&base
  base=base[^coeff.len..^1]
  var lres=0
  for pos in countdown(coeff.len-1,0,1):
    var c=($coeff[pos]).parseint
    var b=($base[pos]).parseint
    lres+=c * b ^ (coeff.len-1-pos)
  var value=lres
  var c=0
  while true:
    c+=1
    var nv=fanb("iso-" & base & " " & ($c))  
    if nv==value:
      echo "smallest ",c
      break
  if c == coeff.parseint: return true
  return false

let d3ex="""ISO2-3 23
ISO2-61 149
ISO2-978 99
ISO2-5887 5923
ISO2-76988 123749
ISO2-435657 929977
ISO2-3949 870737"""
let da3 = nomSansExtension & "_p3.txt"
res=0
var tv=0
#~ for l in d3ex.splitlines:
for l in open(da3).lines:
  tv = fanb(l)
  var valid = fanc(l)
  echo l," ",tv," ",valid
  if valid:
    res+=tv
    echo "adding ",tv
echo "p3 ",res
