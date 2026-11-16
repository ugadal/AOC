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
proc nst(f,nf:deq):int=
  for p,v in f.pairs:
    result+=v
  #~ for p,v in nf.pairs:
    #~ result+= (p+1)*v
proc p2(p:plant):int=
  var forks=0
  let tg = (p.growth-3) div 2
  var F=initdeque[int]()
  var NF=initdeque[int]()
  for x in 0 ..< p.growth:
    F.addLast(0)
  NF=F
  F[0]=1
  while nst(F,NF) < p.limit:
    dump(F)
    dump(NF)
    dump(forks)
    F.addfirst(F.poplast())  
    NF.addfirst(NF.poplast())  
    dump(("pre",F))
    dump(("pre",NF))
    if F[^1]>0:
      F[tg]+=F[^1]
      NF[tg]+=F[^1]
      F[0]+=F[^1]
      forks+=1
      F[^1]=0
    dump(("curr",F))
    dump(("curr",NF))
    if NF[^1]>0:
      F[0]+=NF[^1]
      NF[tg]+=2*NF[^1]
      forks+=1
      NF[^1]=0
    dump(("post",F))
    dump(("post",NF))
    dump((nst(F,NF),forks))
  return nst(F,NF)
var P=readplants(dex1)
echo "exp1: ",P.mapit(it.analyse).sum
echo "p1: ",readplants(dp1).mapit(it.analyse).sum
#~ for p in P:
  #~ echo p.p2
echo P[2].p2
