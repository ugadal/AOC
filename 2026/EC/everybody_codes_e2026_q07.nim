import std/os
#~ import sequtils
import strutils
import math
#~ import algorithm
#~ import regex
import tables
import sugar
#~ import strscans
import sets
#~ import complex
import hashes
import strmisc
let nfs = currentSourcePath.extractFilename.splitFile.name

proc rp(p: int): string =
  let fn = nfs & "_p" & $p & ".txt"
  readfile(fn).strip

proc rex(p: int): string =
  let fn = nfs & "_ex.txt"
  readfile(fn).strip.split("\n\n")[p-1]

proc mkdic (intxt : string) : Table[string, seq[string]] =
  for l in intxt.splitlines:
    let (tg, _, ing) = l.partition(":")
    result[tg] = ing.split(',')

proc reachables(g: Table[string, seq[string]], start: string): HashSet[string] =
  var stack = @[start]
  while stack.len > 0:
    let v = stack.pop
    if v in result: continue
    result.incl v
    for k in g.getordefault(v):
      #~ if k notin result: stack.add k
      stack.add k

var rcps=mkdic(rp(1))    
echo "p1: ",reachables(rcps, "NULL").len - 1

#~ proc involved(g: Table[string, seq[string]], start: string): HashSet[string] =
  #~ var stack = @[start]
  #~ while stack.len>0:
    #~ let ti = stack.pop
    #~ for k,v in g:
      #~ if ti in v:
        #~ if k notin result:stack.add k
    #~ result.incl ti 

rcps=mkdic(rp(2))
#~ echo "p2: ",involved(rcps,"NULL").len-1
proc reversed(g: Table[string, seq[string]]): Table[string, seq[string]] =
  for k, vs in g:
    for v in vs:
      result.mgetOrPut(v, @[]).add k

echo "p2: ", reachables(reversed(rcps), "NULL").len - 1




rcps=mkdic(rp(3))
#~ var sa=involved(rcps,"NULLv1")
#~ var sb=involved(rcps,"NULLv2")
#~ var sc=involved(rcps,"NULLv3")
#~ echo "p3: ",((sa*sb)+(sa*sc)+(sb*sc)).len
rcps=reversed(rcps)
var sa=reachables(rcps,"NULLv1")
var sb=reachables(rcps,"NULLv2")
var sc=reachables(rcps,"NULLv3")
echo "p3: ",((sa*sb)+(sa*sc)+(sb*sc)).len
