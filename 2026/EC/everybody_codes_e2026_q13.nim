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
type Aiguille = object
  angle: int
  move: int
  speed: int

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

proc initAiguilles(t: string): seq[Aiguille] =
  for l in t.splitlines:
    let parts = l.split(" ")
    let items = parts[1].split(":")
    case parts[0]:
    of "hands":
      result = items.mapit(Aiguille(speed: 360 div it.parseint))
    of "direction":
      for i, d in items:
        if d == "CCW": result[i].speed *= -1
    of "current":
      for i, v in items:
        result[i].angle = v.parseint * result[i].speed.abs
    of "move":
      for i, v in items:
        result[i].move = v.parseint
    else: discard

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
