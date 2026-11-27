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
var dex7 = rex(nfs, 7)
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
  
proc cover(b: pack): int =
  var hid, vid: Table[pos, int]
  var nh, nv = 0
  for p in b:
    if p.left notin b:
      var q = p
      while q in b: hid[q] = nh; q = q.right
      inc nh
    if p.up notin b:
      var q = p
      while q in b: vid[q] = nv; q = q.down
      inc nv
  var adj = newSeq[seq[int]](nh)
  for p in b: adj[hid[p]].add vid[p]
  var matchV = newSeqWith(nv, -1)
  proc tryK(u: int, seen: var seq[bool]): bool =
    for v in adj[u]:
      if seen[v]: continue
      seen[v] = true
      if matchV[v] < 0 or tryK(matchV[v], seen):
        matchV[v] = u
        return true
    false
  for u in 0 ..< nh:
    var seen = newSeq[bool](nv)
    if tryK(u, seen): inc result
  
proc p2(txt:string):int=
  var M=readmap(txt)
  M.locateblocks
  return M.blocks.mapit(it.cover).sum
  


when isMainModule:
  echo "examples\n"
  echo "exp1: ", p1(dex1)
  echo "exp2_1: ",p2(dex2)
  echo "exp2_2: ",p2(dex3)
  echo "exp3_1: ",p2(dex4)
  echo "exp3_2: ",p2(dex5)
  echo "exp3_3: ",p2(dex6)
  #~ echo "exp3_t: ",p2(dex7)

  echo "Main:\n"
  echo "p1: ", p1(dp1)
  echo "p2: ", p2(dp2)
  echo "p3: ", p2(dp3)
