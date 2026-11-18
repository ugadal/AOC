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
import complex
import hashes
import strmisc
let nfs = currentSourcePath.extractFilename.splitFile.name
import utils
import deques
var dex1 = rex(nfs, 1)
var dex2 = rex(nfs, 2)
var dp1 = rp(nfs, 1)
var dp2 = rp(nfs, 2)
var dp3 = rp(nfs, 3)
type 
  map = Table[Complex64, char]
  pos = Complex64
  ghost = tuple [p:pos,d:pos,col:int]
  GhostSig = tuple[px, py, dx, dy: int]
proc mkghost(p,d:pos;col: int=0):ghost=
  (p:p,d:d,col:col)
proc getSignature(LG: seq[ghost]): seq[GhostSig] =
  LG.mapIt((
    it.p.re.round.int,
    it.p.im.round.int,
    it.d.re.round.int,
    it.d.im.round.int
  ))

const 
  left =  complex(-1.0, 0.0)
  right =  complex(1.0, 0.0)
  down =  complex(0.0, 1.0)
  up =  complex(0.0, -1.0)
  stag =  complex(0.0, 0.0)
proc `*=`(a: var Complex[float], b: Complex[float]) =
  a = a * b  
proc getmap(txt: string): map =
  for row,line in txt.splitlines.toseq:
    for c,s in line:
      if s!='#':
        continue
      let pos=complex(c.float, row.float)
      result[pos]=s
proc getghosts(txt: string): seq[ghost] =
  for row,line in txt.splitlines.toseq:
    for c,s in line:
      let pos=complex(c.float, row.float)
      case s
        of '<': result.add(mkghost(pos,left))
        of '>': result.add(mkghost(pos,right))
        of 'v': result.add(mkghost(pos,down))
        of '^': result.add(mkghost(pos,up))
        else: continue
proc p1(R : map, G : seq[ghost]):int=
  var LG=G
  for rep in 1..10:
    for g in LG.mitems:
      let np=g.p+g.d
      if np in R.keys.toseq:
        g.d*=down
        result+=1
      else:
        g.p+=g.d
    let GP=LG.mapit(it.p).toseq
    for k,v in toCountTable(GP):
      if v!=1:
        result+=v
        for g in LG.mitems:
          if g.p==k:
            g.d*=up*up
proc p2(R : map, G : seq[ghost]):int=
  var LG=G
  #~ var vus = initHashSet[seq[GhostSig]]()
  var vus = initTable[seq[GhostSig], int]()
  while LG.len>0:
    result+=1
    for g in LG.mitems:
      let np=g.p+g.d
      if np in R.keys.toseq:
        g.d*=down
        g.col+=1
      else:
        g.p+=g.d
    let GP=LG.mapit(it.p).toseq
    for k,v in toCountTable(GP):
      if v!=1:
        for g in LG.mitems:
          if g.p==k:
            g.d*=up*up
            g.col+=1
    LG.keepItIf(it.col<10000)
    let sig = getSignature(LG)
    #~ if vus.containsOrIncl(sig):
    if vus.hasKeyOrPut(sig, result):
      echo "Cycle détecté à l'étape : ", result," fts ",vus[sig]
      #~ break
var Grid=getmap(dex1)
var Ghosts=getghosts(dex1)
echo "exp1: ",p1(Grid,Ghosts)
echo "exp2: ",p2(Grid,Ghosts)
Grid=getmap(dex2)
Ghosts=getghosts(dex2)
echo "ex2p1: ",p1(Grid,Ghosts)
echo "ex2p2: ",p2(Grid,Ghosts)



Grid=getmap(dp1)
Ghosts=getghosts(dp1)
echo "p1: ",p1(Grid,Ghosts)
Grid=getmap(dp2)
Ghosts=getghosts(dp2)
echo "p2: ",p2(Grid,Ghosts)
