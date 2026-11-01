#~ Quest 1: The Coneservation
import std/os
import sequtils
import strutils
import math
let nomFichierSource = currentSourcePath().extractFilename()
let nomSansExtension = nomFichierSource.splitFile().name

let da1 = nomSansExtension & "_p1.txt"
var res=0.0
for v in open(da1).readline.strip.split(",").map(parsefloat):
  let s=v.sqrt
  let f=s.floor
  if f == s: continue
  let n=f+1
  res+=n*n-v
echo res

let da2 = nomSansExtension & "_p2.txt"
var r=0
var ss=0
var req=0
for v in open(da2).readline.strip.split(",").map(parseint):
  if v < 8:
    r+=8-v
    continue
  if v mod 4 == 0 : continue
  ss=4*(1+(v/4).floor.toint)  
  r+=ss-v
echo r

r=0
var tg=0
let da3 = nomSansExtension & "_p3.txt"
#~ for v in open(da3).readline.strip.split(",").map(parseint)[0..20]:
for v in open(da3).readline.strip.split(",").map(parseint):
#~ for v in @[3,11,12,16,24,25]:
  tg=max(3,(1+v).float.sqrt.ceil.int)
  if tg mod 2==0: tg+=1
  #~ echo v," ",tg," ",tg*tg-1-v," required"
  r+=tg*tg-1-v
echo r
