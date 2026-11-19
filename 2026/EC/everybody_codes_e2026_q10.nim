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
proc uponce(R : map, G : var seq[ghost],limit=10000) =
    for g in G.mitems:
      let np=g.p+g.d
      if np in R.keys.toseq:
        g.d*=down
        g.col+=1
      else:
        g.p+=g.d
    let GP=G.mapit(it.p).toseq
    for k,v in toCountTable(GP):
      if v!=1:
        for g in G.mitems:
          if g.p==k:
            g.d*=up*up
            g.col+=1
    G.keepItIf(it.col<limit)
proc rep(G:seq[ghost])=
  echo ""
  for k in G: echo k
  echo ""
proc p2(R : map, G : seq[ghost]):int=
  var LG=G
  #~ var vus = initHashSet[seq[GhostSig]]()
  #~ var vus = initTable[seq[GhostSig], int]()
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
    #~ let sig = getSignature(LG)
    #~ if vus.containsOrIncl(sig):
    #~ if vus.hasKeyOrPut(sig, result):
      #~ echo "Cycle détecté à l'étape : ", result," fts ",vus[sig]
      #~ break
proc nextvanish(R : map, G : seq[ghost], limit : int = 10000): (seq[ghost],int)=
  var vus = initTable[seq[GhostSig], int]()
  var LG=G
  var iter=0
  while LG.len>0:
    var sig=getSignature(LG)
    while true:
      sig = getSignature(LG)
      if  vus.hasKeyOrPut(sig, iter):
        echo "Cycle détecté à l'étape : ", iter," fts ",vus[sig]
        break
      iter+=1
      uponce(R,LG,limit)
      #~ echo vus.len
    #~ echo sig
    #~ echo vus[sig]
    #~ echo iter
    var looptime=iter-vus[sig]
    #~ echo looptime
    #~ LG.rep #situation at loop end
    var EL=LG
    #~ replay
    LG=G
    #~ echo "starting replay"  
    for z in 1..vus[sig]:uponce(R,LG,limit)
    #~ echo "Done"
    #~ LG.rep # situation at loop start
    var SL=LG
    var cyc=Inf
    for (sl,el) in zip(SL,EL):
      let delta=el.col-sl.col
      let ctv=(limit-el.col) div delta
      cyc=min(cyc,ctv.float)
      #~ echo el.col," ",ctv," cycles to vanish ",cyc
    cyc-=1
    for i in 0 ..< EL.len:
      var sl=SL[i]
      var el=EL[i]
      EL[i].col+=(el.col-sl.col)*cyc.int
    iter+=looptime*cyc.int
    #~ EL.rep
    var ori=EL.len
    while EL.len==ori:
      uponce(R,EL,limit)
      iter+=1
    #~ EL.rep
    return (EL,iter)
var x:int
#~ var Grid=getmap(dex1)
#~ var Ghosts=getghosts(dex1)
#~ echo "exp1: ",p1(Grid,Ghosts)
#~ echo "exp2: ",p2(Grid,Ghosts)
#~ echo "test: ",nextvanish(Grid,Ghosts)
#~ while Ghosts.len>0:
  #~ Ghosts.rep
  #~ (Ghosts,x)=nextvanish(Grid,Ghosts)
  #~ echo x
#~ Grid=getmap(dp2)
#~ Ghosts=getghosts(dp2)
var ttl=0
#~ while Ghosts.len>0:
  #~ Ghosts.rep
  #~ (Ghosts,x)=nextvanish(Grid,Ghosts)
  #~ echo x
  #~ ttl+=x
#~ echo ttl

Grid=getmap(dp3)
Ghosts=getghosts(dp3)
ttl=0
while Ghosts.len>0:
  Ghosts.rep
  (Ghosts,x)=nextvanish(Grid,Ghosts,1000000000000)
  echo x
  ttl+=x
echo "p3: ",ttl


#~ echo "ex2p1: ",p1(Grid,Ghosts)
#~ echo "ex2p2: ",p2(Grid,Ghosts)
#~ echo "test: ",p3(Grid,Ghosts,1000000000000)
#~ exit


#~ Grid=getmap(dp1)
#~ Ghosts=getghosts(dp1)
#~ echo "p1: ",p1(Grid,Ghosts)
#~ Grid=getmap(dp2)
#~ Ghosts=getghosts(dp2)
#~ echo "p2: ",p2(Grid,Ghosts)
