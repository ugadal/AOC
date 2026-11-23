import std/[enumerate, math, os, sequtils, sets, strutils, tables]
import utils
import sugar
import memo
import algorithm
type
  Node = string
  Graph = Table[Node, HashSet[Node]]
  link = tuple [o, d: int]
  Net = seq[link]
  Pool = set[int8]
  pairs = (int,int)
  Adj = seq[seq[int]]


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

proc toadj(n:Net,portals:int):Adj=
  result = newSeq[seq[int]](portals+1)
  for l in n:result[l.o].add l.d

proc parseShortcuts(s: string): Net =
  for line in s.splitLines:
    let v = line.splitWhitespace
    let a = v[0].parseInt
    let b = v[1].parseInt
    result.add (a, b)
    result.add (b, a)

proc bfs(adj: Adj, s: int, dist, queue: var seq[int]) =
  dist.fill(-1)
  dist[s] = 0
  var head, tail = 0
  queue[tail] = s; inc tail
  while head < tail:
    let u = queue[head]; inc head
    for v in adj[u]:
      if dist[v] < 0:
        dist[v] = dist[u] + 1
        queue[tail] = v; inc tail

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

proc totalstrain(n: Net, portals: int): int =
  (1..portals).toseq.mapit(n.strain(it)).sum

proc ntotalstrain(adj: Adj): int =
  ## Somme des distances entre toutes les paires ordonnées (u, v).
  var dist = newSeq[int](adj.len)
  var queue = newSeq[int](adj.len)
  for s in 1 ..< adj.len:
    bfs(adj, s, dist, queue)
    for d in dist:
      if d > 0: result += d
      
proc oneline(a, b: int): Net =
  result.add((a, b))
  result.add((b, a))
proc oneline(p:pairs): Net =
  oneline(p[0],p[1])
proc oneline(line: string): Net =
  let v = line.split(" ")
  let a = v[0].parseint
  let b = v[1].parseint
  oneline(a, b)


proc resonance(portals: int, shortcuts: string, dn: int = 1): int =
  let MN = mknet(portals, dn)
  let long=ntotalstrain(MN.toadj(portals))
  var extra: Net
  for line in shortcuts.splitlines: extra &= oneline(line)
  var full = MN & extra
  let short =full.toadj(portals).ntotalstrain
  long-short

proc np2(portals: int, shortcuts: string, dn: int = 1): int =
  var BN = mknet(portals, dn)
  let long=ntotalstrain(BN.toadj(portals))
  var extra: Net
  for line in shortcuts.splitlines: extra &= oneline(line)
  BN &= extra
  result = low(int)
  for x in 1 ..< portals:
    for y in x+1 .. portals:
      let cr = oneline(x, y)
      let T = BN & cr
      let tv=T.toadj(portals).ntotalstrain
      result = max(result, long-tv)
iterator crystals(p: int): seq[int] =
  let s = p div 8
  for offset in 1 .. s:
    yield countup(offset,p,s).toseq

proc journee(pool: Pool): seq[seq[pairs]] {.memoized.} =
  if pool.len==2:
    let tp=pool.toseq
    let tm:pairs=(tp[0].int,tp[1].int)
    return @[@[ tm ]]
  let a=pool.first()
  let targets=pool-{a}
  for b in targets:
    let match: pairs = (int(a), int(b))
    let cj: seq[pairs] = @[match]
    for ssJ in journee(targets-{b}):
      result.add(cj & ssJ)
proc fp3(portals: int, shortcuts: string, dn: int = 1): int =
  var M = mknet(portals, 3)
  var long = M.totalstrain(portals)
  for line in shortcuts.splitlines: M &= oneline(line)
  var p3 = low(int)
  for n in crystals(portals):
    var z:Pool={}
    for it in n:z.incl(it.int8)
    for j in journee(z):
      var T=M
      for mat in j:
        T&=oneline(mat)
      #~ p3 = max(p3, long-T.totalstrain(portals))
      p3 = max(p3, long-T.toadj(portals).ntotalstrain)
  return p3
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
  echo "p3_func: ",fp3(portals,shortcuts)

  echo "\n\nexamples:\n"

  portals = rex(nfs, 1).split(": ")[1].parseint
  shortcuts = rex(nfs, 2)
  echo "exp1: ", resonance(portals, shortcuts, 1)
  echo "exp2: ", np2(portals, shortcuts, 3)
  portals = rex(nfs, 3).split(": ")[1].parseint
  shortcuts = rex(nfs, 4)
  echo "exp3_1: ",fp3(portals,shortcuts)
  portals = rex(nfs, 5).split(": ")[1].parseint
  shortcuts = rex(nfs, 6)
  echo "exp3_2: ",fp3(portals,shortcuts)
