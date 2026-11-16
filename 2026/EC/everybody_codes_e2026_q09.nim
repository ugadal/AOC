import std/os
import sequtils
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
import utils
import deques
var dex1 = rex(nfs, 1)
var dp1 = rp(nfs, 1)
var dp2 = rp(nfs, 2)
var dp3 = rp(nfs, 3)
type
  plant = tuple [id: int, growth: int, limit: int]
  plants = seq[plant]
  deq = Deque[int]
proc mkd(t:string):plant=
  let vals = t.split(", ").mapit(it.split("=")[1].parseint)
  result = (id: vals[0], growth: vals[1], limit: vals[2])

proc readplants(t:string):plants=
  for line in t.splitlines:
    result.add(mkd(line))
proc sumthem(q:deq):int=
  for p,v in q.pairs:
    if p==0:
      result=v
    else:
      result+=p*v
proc analyse(p:plant):int=
  var q = initdeque[int]()
  var tg = (p.growth-1) div 2
  for x in 0 .. p.growth:
    q.addLast(0)
  q[1]=1
  result=1
  while q.sumthem<p.limit:
    result+=1
    let first=q.popFirst()
    q.addfirst(q.poplast())
    q.addfirst(first)
    let last=q[^1]
    if last>0:
      q[0]+=last
      q[1]=last
      q[tg]+=2*last
      q[^1]=0
    
var P=readplants(dex1)
echo "exp1: ",P.mapit(it.analyse).sum
echo "p1: ",readplants(dp1).mapit(it.analyse).sum
