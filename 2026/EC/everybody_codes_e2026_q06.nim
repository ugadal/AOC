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
for v in rcps["NULL"]:
  Ing.incl(v)
echo Ing.len
#~ var pl=Ing.len
var justadded = Ing
var toadd = Ing
while justadded.len>1:
  dump(justadded)
  echo justadded.len
  toadd.clear()
  for k in justadded:
    dump(k)
    if k in rcps:
      dump((k,rcps[k]))
      for v in rcps[k]:
        dump(v)
        toadd.incl(v)
        dump(toadd)
    else: 
      toadd.incl(k)
      echo k," basic ingred"
  dump(toadd)
  justadded=toadd-Ing
  dump(justadded)
  Ing=Ing+toadd
  dump(Ing)
if "NULL" in Ing:Ing.excl("NULL")
dump(Ing)
echo Ing.len  


