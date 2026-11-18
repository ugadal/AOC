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
  branch = tuple [size: int, count: int]
  branches = seq[branch]
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
    
proc p2(p:plant):int=
  if p.limit==1:return 1
  let tg=(p.growth-1) div 2
  var NF,F = inittable[int,int]()
  var time=p.growth
  if tg!=1:
    F[tg]=1  
    NF[tg]=1  
    F[1]=1
  else:
    F[1]=2
    NF[1]=1
  while F.values.toseq.sum < p.limit :
    let nt= @[p.growth - F.keys.toseq.max,p.growth-NF.keys.toseq.max].min
    time+=nt
    F=collect(inittable()):
      for k,v in F:
        {k+nt : v}
    NF=collect(inittable()):
      for k,v in NF:
        {k+nt : v}
    if p.growth in F:  
      var g=F[p.growth]
      F.mgetOrPut(tg, 0)+=g
      F.mgetOrPut(1, 0)+=g
      NF.mgetOrPut(tg, 0)+=g
      F.del(p.growth)
    if p.growth in NF:
      var g=NF[p.growth]
      F.mgetOrPut(1, 0)+=g
      NF.mgetOrPut(tg, 0)+=2*g
    NF.del(p.growth)
  time
var P=readplants(dex1)
echo "exp1: ",P.mapit(it.analyse).sum
echo "p1: ",readplants(dp1).mapit(it.analyse).sum
echo "exp2: ",readplants(dex1).mapit(it.p2).sum
echo "p2: ",readplants(dp2).mapit(it.p2).sum
echo "p3: ",readplants(dp3).mapit(it.p2).sum
