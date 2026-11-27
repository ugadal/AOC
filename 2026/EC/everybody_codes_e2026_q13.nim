import std/[enumerate, math, os, sequtils, sets, strutils, tables]
import utils
import sugar
import memo
import algorithm
import strscans
#~ type
  #~ pos = (int, int)
  #~ stack = (pos, pos)
  #~ pack = HashSet[pos]
type aiguille = object
  angle: int
  move: int
  speed:int= 360

let nfs = currentSourcePath.extractFilename.splitFile.name
var dex1 = rex(nfs, 1)
var dex2 = rex(nfs, 2)
var dex3 = rex(nfs, 3)
#~ var dex4 = rex(nfs, 4)
#~ var dex5 = rex(nfs, 5)
#~ var dex6 = rex(nfs, 6)
#~ var dex7 = rex(nfs, 7)
var dp1 = rp(nfs, 1)
#~ var dp2 = rp(nfs, 2)
#~ var dp3 = rp(nfs, 3)

proc initaiguilles(t:string):seq[aiguille]=
  let tl=t.splitlines
  var a,b,c:aiguille
  var i,j,k:int
  var ca,cb,cc:string
  for l in tl:
    if l.scanf("hands $i:$i:$i",i,j,k):
      a.speed = 360 div i
      b.speed = 360 div j
      c.speed = 360 div k
    elif l.scanf("direction $w:$w:$w",ca,cb,cc):
      dump((ca,cb,cc))
      if ca=="CCW":a.speed *= -1
      if cb=="CCW":b.speed *= -1
      if cc=="CCW":c.speed *= -1
    elif l.scanf("current $i:$i:$i",i,j,k):
      a.angle=(i*a.speed).floormod 360
      b.angle=(j*b.speed).floormod 360
      c.angle=(k*c.speed).floormod 360
    elif l.scanf("move $i:$i:$i",i,j,k):
      a.move=i
      b.move=j
      c.move=k
  result = @[a,b,c]

when isMainModule:
  echo "examples\n"
  echo initaiguilles(dex1)
  #~ echo "exp1: ", p1(dex1)
  #~ echo "exp2_1: ",p2(dex2)
  #~ echo "exp2_2: ",p2(dex3)
  #~ echo "exp3_1: ",p2(dex4)
  #~ echo "exp3_2: ",p2(dex5)
  #~ echo "exp3_3: ",p2(dex6)
  #~ echo "exp3_t: ",p2(dex7)

  echo "Main:\n"
  #~ echo "p1: ", p1(dp1)
  #~ echo "p2: ", p2(dp2)
  #~ echo "p3: ", p2(dp3)
