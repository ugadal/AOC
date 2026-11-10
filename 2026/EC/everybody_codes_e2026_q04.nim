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

let nfs = currentSourcePath.extractFilename.splitFile.name

let da1 = nfs & "_p1.txt"
let d = """id=1 quest=1 part=1 time=187
id=3 quest=1 part=1 time=413
id=5 quest=1 part=3 time=744
id=2 quest=1 part=3 time=745
id=4 quest=1 part=2 time=558
id=1 quest=1 part=2 time=299
id=1 quest=1 part=3 time=362
id=4 quest=1 part=3 time=1268
id=4 quest=1 part=1 time=457
id=5 quest=1 part=1 time=257
id=2 quest=1 part=1 time=192
id=3 quest=1 part=3 time=1168
id=5 quest=1 part=2 time=346
id=3 quest=1 part=2 time=455
id=2 quest=1 part=2 time=562"""
var m = RegexMatch2()
var score =  inittable[int,int]()
for l in open(da1).lines:
  var values = l.split(" ").mapit(it.split("=")[1].parseint)
  var id=values[0]
  var time=values[3]
  score.mgetOrPut(id, 0) += time

var res=0
var f=0
for v in toseq(score.pairs).sorted((x,y) => cmp(x[1],y[1])).mapit(it[1]):
  f+=1
  res+=f*v
echo "p1 : ",res

let d2="""id=2 quest=1 part=1 time=100
id=4 quest=2 part=1 time=150
id=1 quest=2 part=1 time=140
id=1 quest=1 part=2 time=180
id=2 quest=2 part=1 time=130
id=4 quest=1 part=1 time=110
id=1 quest=2 part=2 time=210
id=2 quest=2 part=2 time=240
id=1 quest=2 part=3 time=330
id=2 quest=1 part=2 time=170
id=3 quest=1 part=1 time=90
id=4 quest=1 part=2 time=175
id=3 quest=2 part=1 time=120
id=1 quest=1 part=1 time=120
id=3 quest=2 part=2 time=220
id=2 quest=2 part=3 time=350
id=3 quest=1 part=2 time=160"""
let da2 = nfs & "_p2.txt"
proc compar(x,y:(int,seq[int])):int=
  let lc=cmp(y[1].len,x[1].len)
  if lc!=0:return lc
  return cmp(x[1].sum, y[1].sum)
var sc2=inittable[int,seq[int]]()
#~ for l in d2.splitlines:
for l in open(da2).lines:
  var values = l.split(" ").mapit(it.split("=")[1].parseint)
  var id=values[0]
  var time=values[3]
  sc2.mgetOrPut(id,@[]).add(time)
res=0
for f,pair in toseq(sc2.pairs).sorted(compar):
  res+=(f+1)*pair[1].sum
echo "p2 : ",res

#~ let d3="""id=2 quest=1 part=1 time=100
#~ id=4 quest=2 part=1 time=150
#~ id=1 quest=2 part=1 time=140
#~ id=1 quest=1 part=2 time=180
#~ id=2 quest=2 part=1 time=130
#~ id=4 quest=1 part=1 time=110
#~ id=1 quest=2 part=2 time=210
#~ id=2 quest=2 part=2 time=240
#~ id=1 quest=2 part=3 time=330
#~ id=2 quest=1 part=2 time=170
#~ id=3 quest=1 part=1 time=90
#~ id=4 quest=1 part=2 time=175
#~ id=3 quest=2 part=1 time=120
#~ id=1 quest=1 part=1 time=120
#~ id=3 quest=2 part=2 time=220
#~ id=2 quest=2 part=3 time=350
#~ id=3 quest=1 part=2 time=160"""

let d3="""id=2 quest=1 part=1 time=90
id=4 quest=2 part=1 time=150
id=1 quest=2 part=1 time=130
id=1 quest=1 part=2 time=180
id=2 quest=2 part=1 time=130
id=4 quest=1 part=1 time=110
id=1 quest=2 part=2 time=210
id=2 quest=2 part=2 time=220
id=1 quest=2 part=3 time=330
id=2 quest=1 part=2 time=170
id=3 quest=1 part=1 time=90
id=4 quest=1 part=2 time=170
id=3 quest=2 part=1 time=120
id=1 quest=1 part=1 time=120
id=3 quest=2 part=2 time=220
id=2 quest=2 part=3 time=350
id=3 quest=1 part=2 time=170"""

let da3 = nfs & "_p3.txt"
type record = tuple [id: int, quest: int, part: int, time:int,cumtime:int]
var allrec: seq[record] = @[]

#~ for l in d3.splitlines:
for l in open(da3).lines:
  var i, q, p, t: int
  if l.scanf("id=$i quest=$i part=$i time=$i", i, q, p, t):
    allrec.add((id: i, quest: q, part: p, time: t,cumtime: 0))
var mid=max(allrec.mapit(it.id))
var tabscore = newSeqWith(mid + 1, 0)
var mq=max(allrec.mapit(it.quest))

for q in 1..mq:
  for p in 1..mid:
    var ct=0
    var ind: seq[int] = @[]
    for idx in 0 ..< allrec.len:
      if allrec[idx].quest == q and allrec[idx].id == p :
        ind.add(idx)
    ind.sort((x,y)=>cmp(allrec[x].part,allrec[y].part))
    for idx in ind:
      ct+=allrec[idx].time
      allrec[idx].cumtime=ct

var sc4=newSeqWith(mid + 1, 0)
for q in 1..mq:
  let subrec=allrec.filterit(it.quest==q)
  var mp=max(subrec.mapit(it.part))
  for p in 1..mp:
    var basescore=50*p
    var pv=0
    var consecdraw=0
    for z in  subrec.filterit(it.part==p).sorted((x,y)=>cmp(x.cumtime,y.cumtime)):
      var who=z.id
      if pv==0: 
        pv=z.cumtime
      else:
        if z.cumtime==pv:
          consecdraw+=1
        else:
          basescore-=1+consecdraw
          basescore=max(0,basescore)
          consecdraw=0
          pv=z.cumtime
      sc4[who]+=basescore

sc4=sc4.sorted
var fr:int=0
var pv=0
var cd=0
fr=0
for i,v in sc4.reversed:
  if pv==0:
    pv=v
    fr+=v*(i+1)
  else:
    if v==pv:
      cd+=1
      fr+=v*(1+i-cd)
    else:
      fr+=v*(i+1)
      pv=v
      cd=0
echo "p3 : ",fr
