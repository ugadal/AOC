import std/[enumerate, math, os, sequtils, sets, strutils, tables]
import utils
import sugar
type
  Node = string
  Graph = Table[Node, HashSet[Node]]

proc mkgraph(portals: int, shortcuts: string, directn: int = 1): Graph =
  proc addedge(g: var Graph, u, v: Node) =
    g.mgetorput(u, initHashSet[Node]()).incl(v)
    g.mgetorput(v, initHashSet[Node]()).incl(u)
  proc addedge(g: var Graph, couple: seq[Node]) =
    g.addedge(couple[0], couple[1])
  var pool = (1..portals).toseq
  pool.add(pool)
  for x in 1 .. portals:
    var nx = pool[x-1]
    for y in 1 .. directn:
      var ny = pool[x+y-1]
      result.addedge($nx, $ny)
  if shortcuts.len > 0:
    for line in shortcuts.splitlines:
      result.addedge(line.split(" "))

proc rep(G: Graph) =
  for k, v in G:
    echo k, " ", v

proc getstepsfrom(g: Graph, start: Node): int =
  var visited = initHashSet[Node]()
  var tovisit = [start].toHashSet
  var step = 0
  while tovisit.len > 0:
    #~ dump((result,step,visited,tovisit))
    var newstack = initHashSet[Node]()
    for o in tovisit:
      result+=step
      for d in g[o]:
        if d notin visited: newstack.incl(d)
      visited.incl(o)
    tovisit = newstack-visited
    step+=1

proc p1(portals: int, shortcuts: string, dn: int = 1): int =
  let G = mkgraph(portals, "", dn)
  let long = (1..portals).toseq.mapit(G.getstepsfrom($it)).sum
  let F = mkgraph(portals, shortcuts, dn)
  let short = (1..portals).toseq.mapit(F.getstepsfrom($it)).sum
  long-short

proc addcr(g: Graph, u, v: Node): Graph =
  result=g
  result.mgetorput(u, initHashSet[Node]()).incl(v)
  result.mgetorput(v, initHashSet[Node]()).incl(u)

proc p2(portals: int, shortcuts: string, dn: int = 1): int =
  var v = low(int)
  let G=mkgraph(portals,"",dn)
  let H=mkgraph(portals,shortcuts,dn)
  let long = (1..portals).toseq.mapit(G.getstepsfrom($it)).sum
  var c = (1..portals).toseq
  for ix in 0 ..< portals-1:
    for iy in ix+1 ..< portals:
      var T=H.addcr($ix,$iy)
      let short = (1..portals).toseq.mapit(T.getstepsfrom($it)).sum
      v = max(v, long-short)
  return v
when isMainModule:
  let nfs = splitFile(currentSourcePath).name
  var portals = rps(nfs, 1, 1).split(": ")[1].parseint
  var shortcuts = rps(nfs, 1, 2)
  echo "p1: ", p1(portals, shortcuts)
  portals = rps(nfs, 2, 1).split(": ")[1].parseint
  shortcuts = rps(nfs, 2, 2)
  echo "p2: ", p2(portals, shortcuts, 3)
  #~ echo "examples"
  #~ portals = rex(nfs, 1).split(": ")[1].parseint
  #~ shortcuts = rex(nfs, 2)
  #~ echo "p1: ", p1(portals, shortcuts, 1)
  #~ echo "p2: ", p1(portals, shortcuts&"\n1 5", 3)
  #~ echo "p2p: ", p2(portals, shortcuts, 3)
