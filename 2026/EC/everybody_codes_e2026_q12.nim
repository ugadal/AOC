import std/[enumerate, math, os, sequtils, sets, strutils, tables]
import utils
import sugar
import memo
import algorithm
type
  pos = (int, int)
  stack = (pos, pos)
  pack = HashSet[pos]
type Grille = object
  map: pack
  R, C: int
  stacks: seq[stack]
  blocks: seq[pack]

let nfs = currentSourcePath.extractFilename.splitFile.name
var dex1 = rex(nfs, 1)
var dex2 = rex(nfs, 2)
var dex3 = rex(nfs, 3)
var dp1 = rp(nfs, 1)
var dp2 = rp(nfs, 2)
var dp3 = rp(nfs, 3)
proc right(p: pos): pos = (p[0], 1+p[1])
proc down(p: pos): pos = (1+p[0], p[1])
proc up(p: pos): pos = (p[0] - 1, p[1])
proc left(p: pos): pos = (p[0], p[1] - 1)

proc readmap(t: string): Grille =
  var AL = t.splitlines()
  result.R = AL.len
  result.C = AL[0].len
  for r, row in AL:
    for c, s in row:
      if s == '#':
        result.map.incl (r, c)
proc locatestack(G: var Grille) =
  for p in G.map:
    if p.up notin G.map and p.left notin G.map:
      var bottomright = p
      while bottomright.right in G.map: bottomright = bottomright.right
      while bottomright.down in G.map: bottomright = bottomright.down
      G.stacks.add (p, bottomright)
proc p1(txt: string): int =
  var M = readmap(txt)
  M.locatestack
  for (tl, br) in M.stacks:
    result+=1+min(br[0]-tl[0], br[1]-tl[1])
iterator around(p: pos): pos =
  yield (p[0]-1, p[1])
  yield (p[0]+1, p[1])
  yield (p[0], p[1]-1)
  yield (p[0], p[1]+1)
proc locateblocks(G: var Grille) =
  var unvisited = G.map
  while unvisited.len > 0:
    let start = unvisited.pop()
    var thisblock=[start].toHashSet
    var stack = @[start]
    while stack.len>0:
      let curr=stack.pop()
      for nxt in curr.around:
        if nxt in unvisited:
          unvisited.excl(nxt)
          thisblock.incl(nxt)
          stack.add(nxt)
    G.blocks.add thisblock      
proc isrect(b:pack):int=
  let top=b.mapit(it[0]).min
  let bot=b.mapit(it[0]).max
  let lef=b.mapit(it[1]).min
  let rig=b.mapit(it[1]).max
  if (bot-top+1)*(rig-lef+1)==b.len:
    return min(bot-top+1,rig-lef+1)
  0
proc rotateright(b:pack):pack=
  for x in b:
    result.incl((x[1],-x[0]))
    
proc lshaped(b:pack):int=
  let top=b.mapit(it[0]).min
  let bot=b.mapit(it[0]).max
  let lef=b.mapit(it[1]).min
  let rig=b.mapit(it[1]).max
  dump((top,bot,lef,rig))
  for g in b: 
    #~ echo g," ",g.right,g.right in b
    #~ echo g," ",g.down,g.down in b
    #~ echo g," ",g.down.right,g.down.right in b
    if g.right in b and g.down in b and g.down.right notin b:
      echo g," top left angle"
      return 1
  0
  
proc anablock(b:pack):int=
 if b.len==1:
   echo "single block"
   return 1
 if b.isrect>0:
   echo "rectangle simple"
   return b.isrect
 return b.lshaped
 return 0
proc p2(txt:string)=
  var M=readmap(txt)
  M.locateblocks
  for b in M.blocks:
    echo b," : ",b.anablock
  
  


when isMainModule:

  echo "examples\n"
  echo "exp1: ", p1(dex1)
  p2(dex2)
  p2(dex3)

  echo "Main:\n"
  echo "p1: ", p1(dp1)
