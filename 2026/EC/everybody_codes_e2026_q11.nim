import std/[enumerate, math, os, sequtils, sets, strutils, tables]
import utils
import sugar
type
  Node = string
  Graph = Table[Node, HashSet[Node]]
  #~ Vec = tuple[x, y: int]
  #~ Ghost = object
    #~ pos, dir: Vec
    #~ hits: int
  #~ Signature = seq[tuple[pos, dir: Vec]]

#~ const
  #~ left: Vec = (-1, 0)
  #~ right: Vec = (1, 0)
  #~ up: Vec = (0, -1)
  #~ down: Vec = (0, 1)
  #~ defaultLimit = 10_000
  #~ hugeLimit = int(1_000_000_000_000)

#~ func `+`(a, b: Vec): Vec = (a.x + b.x, a.y + b.y)
#~ func turnRight(d: Vec): Vec = (-d.y, d.x)
#~ func reverse(d: Vec): Vec = (-d.x, -d.y)

#~ func signature(ghosts: seq[Ghost]): Signature =
  #~ ghosts.mapIt((pos: it.pos, dir: it.dir))

#~ proc parseWalls(txt: string): HashSet[Vec] =
  #~ for row, line in enumerate(txt.splitLines):
    #~ for col, ch in line:
      #~ if ch == '#':
        #~ result.incl((col, row))

      #~ proc parseGhosts(txt: string): seq[Ghost] =
        #~ for row, line in enumerate(txt.splitLines):
          #~ for col, ch in line:
            #~ case ch
            #~ of '<': result.add Ghost(pos: (col, row), dir: left)
            #~ of '>': result.add Ghost(pos: (col, row), dir: right)
            #~ of 'v': result.add Ghost(pos: (col, row), dir: down)
            #~ of '^': result.add Ghost(pos: (col, row), dir: up)
            #~ else: discard

          #~ proc step(walls: HashSet[Vec], ghosts: var seq[Ghost], limit: int) =
            #~ for g in ghosts.mitems:
              #~ let next = g.pos + g.dir
              #~ if next in walls:
      #~ g.dir = g.dir.turnRight
      #~ inc g.hits
              #~ else:
      #~ g.pos = next

              #~ # collisions : plusieurs fantômes sur la même case -> demi-tour
              #~ var occupancy = initCountTable[Vec]()
              #~ var occupancy : CountTable[Vec]
              #~ for g in ghosts:
    #~ occupancy.inc g.pos
              #~ for g in ghosts.mitems:
    #~ if occupancy[g.pos] > 1:
      #~ g.dir = g.dir.reverse
      #~ inc g.hits

  #~ ghosts.keepItIf(it.hits < limit)

              #~ proc nextVanish(walls: HashSet[Vec], start: seq[Ghost], limit: int):
    #~ tuple[ghosts: seq[Ghost], elapsed: int] =
              #~ if start.len == 0:
    #~ return
              #~ var
    #~ seen = initTable[Signature, int]() # état -> instant où on l'a vu
    #~ ghosts = start
    #~ iter = 0
    #~ sig = signature(ghosts)
              #~ while not seen.hasKeyOrPut(sig, iter):
    #~ inc iter
    #~ step(walls, ghosts, limit)
    #~ if ghosts.len != start.len: # disparition avant même d'avoir bouclé
      #~ return (ghosts, iter)
    #~ sig = signature(ghosts)

              #~ let
    #~ cycleStart = seen[sig]
    #~ cycleLen = iter - cycleStart

              #~ # état au début du cycle, pour comparer les hits
              #~ var atStart = start
              #~ for _ in 1 .. cycleStart:
    #~ step(walls, atStart, limit)
              #~ var atEnd = ghosts

              #~ # 2. combien de cycles complets peut-on sauter sans qu'un fantôme disparaisse ?
              #~ var cycles = high(int)
              #~ for (s, e) in zip(atStart, atEnd):
    #~ let gain = e.hits - s.hits
    #~ if gain > 0:
      #~ cycles = min(cycles, (limit - e.hits) div gain)
  #~ if cycles == high(int):
    #~ raise newException(ValueError, "aucun fantôme n'atteindra jamais la limite")

  #~ # 3. saut (on garde un cycle de marge, pas à pas ensuite)
  #~ let skip = max(cycles - 1, 0)
  #~ for i in 0 ..< atEnd.len:
    #~ atEnd[i].hits += (atEnd[i].hits - atStart[i].hits) * skip
  #~ iter += cycleLen * skip

  #~ # 4. fin de course
  #~ let count = atEnd.len
  #~ while atEnd.len == count:
    #~ step(walls, atEnd, limit)
    #~ inc iter
  #~ (atEnd, iter)

              #~ proc part1(txt: string): int =
  #~ let walls = parseWalls(txt)
  #~ var ghosts = parseGhosts(txt)
  #~ for _ in 1 .. 10:
    #~ step(walls, ghosts, defaultLimit)
  #~ ghosts.mapIt(it.hits).sum

              #~ proc totalVanishTime(txt: string, limit: int): int =
  #~ ## Parties 2 et 3 : temps cumulé jusqu'à la disparition de tous les fantômes.
  #~ let walls = parseWalls(txt)
  #~ var ghosts = parseGhosts(txt)
  #~ while ghosts.len > 0:
    #~ let (remaining, elapsed) = nextVanish(walls, ghosts, limit)
    #~ ghosts = remaining
    #~ result += elapsed
proc mkgraph(portals: int, shortcuts: string): Graph =
  proc addedge(g: var Graph, u, v: Node) =
    g.mgetorput(u, initHashSet[Node]()).incl(v)
    g.mgetorput(v, initHashSet[Node]()).incl(u)
  proc addedge(g: var Graph, couple: seq[Node]) =
    g.addedge(couple[0], couple[1])
  for x in 1 .. portals:
    let y = (x mod portals) + 1
    result.addedge($x, $y)
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
    var newstack = initHashSet[Node]()
    for o in tovisit:
      result+=step
      for d in g[o]:
        if d notin visited: newstack.incl(d)
      visited.incl(o)
    tovisit = newstack
    step+=1
proc p1(portals:int,shortcuts:string):int=
  let G = mkgraph(portals, " ")
  let long= (1..portals).toseq.mapit(G.getstepsfrom($it)).sum
  let F = mkgraph(portals, shortcuts)
  let short= (1..portals).toseq.mapit(F.getstepsfrom($it)).sum
  long-short
when isMainModule:
  let nfs = splitFile(currentSourcePath).name
  let portals = rps(nfs, 1,1).split(": ")[1].parseint
  let shortcuts = rps(nfs,1,2)
  dump(portals)
  dump(shortcuts)
  echo "p1: ",p1(portals,shortcuts)
