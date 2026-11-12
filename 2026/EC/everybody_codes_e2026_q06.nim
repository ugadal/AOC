import std/os
import sequtils
import strutils
import math
import algorithm
#~ import regex
import tables
import sugar
import strscans
import sets
import complex
import hashes
import strmisc
let nfs = currentSourcePath.extractFilename.splitFile.name

proc rp(p:int):string=
  let fn= nfs & "_p" & $p & ".txt"
  readfile(fn).strip

proc rex(p:int):string=
  let fn= nfs & "_ex.txt"
  readfile(fn).strip.split("\n\n")[p-1]

#~ let da=rex(1)
let da=rp(1)
var rcps = initTable[string, seq[string]]()
for l in da.splitlines:
  let (tg,_,ing) = l.partition(":")
  rcps[tg]=ing.split(',')
dump(rcps)
var Ing = initHashSet[string]()
var totreat: seq[string] = @[]
for v in rcps["NULL"]: totreat.add(v)
while totreat.len>0:
  var v=totreat.pop()
  if v in Ing:continue
  Ing.incl(v)
  if v in rcps:
    for k in rcps[v]:
     if k in Ing:continue
     totreat.add(k)
if "NULL" in Ing:Ing.excl("NULL")
echo Ing.len  


