import std/os
import sequtils
import strutils
import math
import algorithm
import regex
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

let da=rex(1)
var rcps = initTable[string, seq[string]]()
for l in da.splitlines:
  let (tg,_,ing) = l.partition(":")
  rcps[tg]=ing.split(',')
dump(rcps)

