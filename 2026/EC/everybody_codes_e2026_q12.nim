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
var dex4 = rex(nfs, 4)
var dex5 = rex(nfs, 5)
var dex6 = rex(nfs, 6)
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

proc anablock(b:pack):int=
  if b.len==1:   return 1
  let top=b.mapit(it[0]).min
  let bot=b.mapit(it[0]).max
  let lef=b.mapit(it[1]).min
  let rig=b.mapit(it[1]).max
  let h=bot-top+1
  let w=rig-lef+1
  if (bot-top+1)*(rig-lef+1)==b.len: return min(bot-top+1,rig-lef+1)
  for (coin, vert, horiz) in [((top, lef), down, right),
                              ((top, rig), down, left),
                              ((bot, lef), up,   right),
                              ((bot, rig), up,   left)]:
    if coin notin b:
      var p = coin
      var nh = 0
      while p notin b: 
        p=p.vert    
        inc nh
      p = coin
      var nw = 0
      while p notin b: 
        p = p.horiz
        inc nw
      return min([h, w, (h - nh) + (w - nw)])  
  echo "hole in a box ",b.len
  var tl:pos
  block found:
    for r in top .. bot:
      for c in lef .. rig:
        if (r,c) notin b:
          tl=(r,c)
          break found
  var br=tl
  while br.right notin b : br=br.right
  while br.down notin b : br=br.down
  dump((top,lef,tl," ",bot,rig,br))
  var TLB = b
  dump(TLB.len)
  for r in top .. br[0]:
    for c in lef .. tl[1]:
      if (r,c) in b:TLB.excl((r,c))
  #~ dump(TLB.len)
  dump(TLB.len)
  #~ TLB.keepitif( it[0]<tl[0])
  #~ dump(TLB.len)
  #~ echo tl[0]-top+tl[1]-lef+bot-br[0]+rig-br[1]
  #~ return tl[0]-top+tl[1]-lef+bot-br[0]+rig-br[1]

proc p2(txt:string):int=
  var M=readmap(txt)
  M.locateblocks
  return M.blocks.mapit(it.anablock).sum
  


when isMainModule:
  echo "examples\n"
  echo "exp1: ", p1(dex1)
  echo "exp2_1: ",p2(dex2)
  echo "exp2_2: ",p2(dex3)
  echo "exp3_1: ",p2(dex4)
  echo "exp3_2: ",p2(dex5)

  echo "Main:\n"
  echo "p1: ", p1(dp1)
  echo "p2: ", p2(dp2)
