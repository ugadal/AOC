import std/[enumerate, math, os, sequtils, sets, strutils, tables]
import utils
import sugar
type
  Node = string
  Graph = Table[Node, HashSet[Node]]
  link = tuple [o, d: int]
  Net = seq[link]


proc mknet(portals: int, directn: int = 1): Net =
  var pool = (1..portals).toseq
  pool.add(pool)
  for x in 1 .. portals:
    var nx = pool[x-1]
    for y in 1 .. directn:
      var ny = pool[x+y-1]
      result.add((nx, ny))
      result.add((ny, nx))

proc mknet(portals: int): Net =
  mknet(portals, 1)

proc mknet(portals: int, shortcuts: string, directn: int = 1): Net =
  result = mknet(portals, directn)
  if shortcuts.len > 0:
    for line in shortcuts.splitlines:
      let od = line.split(" ")
      result.add((od[0].parseint, od[1].parseint))
      result.add((od[1].parseint, od[0].parseint))

proc strain(n: Net, start: int): int =
  var visited = initHashSet[int]()
  var tovisit = [start].toHashSet
  var step = 0
  while tovisit.len > 0:
    var newstack = initHashSet[int]()
    for origin in tovisit:
      result+=step
      for l in n.filterit(it.o == origin):
        if l.d notin visited: newstack.incl(l.d)
      visited.incl(origin)
    tovisit = newstack-visited
    step+=1

proc totalstrain(n: Net, portals:int):int=
  (1..portals).toseq.mapit(n.strain(it)).sum
  
proc oneline(a, b: int): Net =
  result.add((a, b))
  result.add((b, a))

proc oneline(line: string): Net =
  let v = line.split(" ")
  let a = v[0].parseint
  let b = v[1].parseint
  oneline(a, b)


proc resonance(portals: int, shortcuts: string, dn: int = 1): int =
  let MN = mknet(portals, dn)
  let long = (1..portals).toseq.mapit(MN.strain(it)).sum
  var extra: Net
  for line in shortcuts.splitlines: extra &= oneline(line)
  var full = MN & extra
  let short = (1..portals).toseq.mapit(full.strain(it)).sum
  long-short

proc np2(portals: int, shortcuts: string, dn: int = 1): int =
  var BN = mknet(portals, dn)
  let long = (1..portals).toseq.mapit(BN.strain(it)).sum
  var extra: Net
  for line in shortcuts.splitlines: extra &= oneline(line)
  BN &= extra
  result = low(int)
  for x in 1 ..< portals:
    for y in x+1 .. portals:
      let cr = oneline(x, y)
      let T = BN & cr
      let tv = (1..portals).toseq.mapit(T.strain(it)).sum
      result = max(result, long-tv)

when isMainModule:
  echo "Main:\n"
  let nfs = splitFile(currentSourcePath).name
  var portals = rps(nfs, 1, 1).split(": ")[1].parseint
  var shortcuts = rps(nfs, 1, 2)
  echo "p1: ", resonance(portals, shortcuts)
  portals = rps(nfs, 2, 1).split(": ")[1].parseint
  shortcuts = rps(nfs, 2, 2)
  echo "p2: ", np2(portals, shortcuts, 3)
  portals = rps(nfs, 3, 1).split(": ")[1].parseint
  shortcuts = rps(nfs, 3, 2)

  echo "\n\nexamples:\n"
  portals = rex(nfs, 1).split(": ")[1].parseint
  shortcuts = rex(nfs, 2)
  echo "exp1: ", resonance(portals, shortcuts, 1)
  echo "exp2: ", np2(portals, shortcuts, 3)
  portals = rex(nfs, 3).split(": ")[1].parseint
  shortcuts = rex(nfs, 4)
  var M=mknet(portals,3)
  echo M.totalstrain(portals)
  portals = rex(nfs, 5).split(": ")[1].parseint
  shortcuts = rex(nfs, 6)
  M=mknet(portals,3)
  echo M.totalstrain(portals)
  #~ echo "exp31: ", resonance(portals, shortcuts, 1)
  #~ echo "exp2: ", np1(portals, shortcuts, 3)
  #~ echo MN
