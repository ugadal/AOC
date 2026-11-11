import std/os
import sequtils
import strutils
import math
import algorithm
import regex
import tables
import sugar
import strscans
import sets
import complex
import hashes

let nfs = currentSourcePath.extractFilename.splitFile.name

proc rp(p:int):string=
  let fn= nfs & "_p" & $p & ".txt"
  readfile(fn).strip

proc rex(p:int):string=
  let fn= nfs & "_ex.txt"
  readfile(fn).strip.split("\n\n")[p-1]

proc createGrid(al: seq[string]): tuple[grid: Table[Complex64, char], sp: Complex64, rows: int, cols: int] =
  var g = initTable[Complex64, char]()
  let rows = al.len
  let cols = if rows > 0: al[0].len else: 0
  for row, line in al:
    for c, s in line:
      let pos = complex(c.float, row.float)
      g[pos] = s
  let sr = (rows.float - 1.0) / 2.0
  let sc = (cols.float - 1.0) / 2.0
  let startPos = complex(sc, sr)
  g[startPos] = '#'
  return (g, startPos, rows, cols)

let al=rp(3)
#~ let al=rex(1)
var (G, sp, R, C) = createGrid(al.splitlines)

const directions = [
  complex(-1.0, -1.0), complex(0.0, -1.0), complex(1.0, -1.0),
  complex(-1.0,  0.0),                     complex(1.0,  0.0),
  complex(-1.0,  1.0), complex(0.0,  1.0), complex(1.0,  1.0) ]
const disk = [
complex(-1.0, -2.0), complex(0.0, -2.0), complex(1.0, -2.0),
complex(-2.0, -1.0), complex(-1.0, -1.0), complex(0.0, -1.0), complex(1.0, -1.0), complex(2.0, -1.0),
complex(-2.0, 0.0),  complex(-1.0, 0.0),                      complex(1.0, 0.0),  complex(2.0, 0.0),
complex(-2.0, 1.0),  complex(-1.0, 1.0),  complex(0.0, 1.0),  complex(1.0, 1.0),  complex(2.0, 1.0),
complex(-1.0,  2.0), complex(0.0,  2.0), complex(1.0,  2.0) ]
iterator around(pos: Complex64): Complex64 =
  for dir in directions:
    let voisinPos = pos + dir
    if voisinPos in G:
      yield voisinPos
var toadd : seq[Complex64] = @[]
while true:
  toadd= @[]
  for pos,s in G:
    if s != '#':
      if countIt(around(pos), G[it] in {'#', '1'})>=5:
        if countIt(around(pos), G[it] in {'#'})>=1:
          toadd.add(pos)
  if toadd.len>0:
    for pos in toadd:
      G[pos]='#'
  else:break
echo "part 1: ",countit(G.values, it=='#')
proc printGrid(grid: Table[Complex64, char], rows, cols: int) =
  for row in 0 ..< rows:
    for col in 0 ..< cols:
      let pos = complex(col.float, row.float)
      stdout.write grid.getOrDefault(pos, ' ')
    echo "" 
for pos,s in G: 
  if s!='#':G[pos]='.'
iterator sandaround(pos: Complex64): char =
  for dir in directions:
    let voisinPos = pos + dir
    if voisinPos in G:
      yield G[voisinPos]
    else: yield '.'
iterator treesaround(pos: Complex64): char =    
  for dir in disk:
    let np =pos+dir
    yield G.getOrDefault(np, '.')
while true:
  toadd= @[]
  for pos,s in G:
    if s == '#':
      if countIt(sandaround(pos), it in {'.'})>=1:toadd.add(pos)
      elif countIt(sandaround(pos), it in {'.', '='})>=5:
        toadd.add(pos)
  if toadd.len>0:
    for pos in toadd:
      G[pos]='='
  else:break
echo "part 2: ",countit(G.values, it=='=')
toadd = @[]
for pos,s in G:
  if s=='#':
    if allIt(toseq(treesaround(pos)),it=='#'):
      toadd.add(pos)
for pos in toadd:G[pos]='@'
for rrr in 1..2:
  toadd = @[]
  for pos,s in G:
    if s=='#':
      let ar=toseq(sandaround(pos))
      if ar.countit(it=='@')>=4 and ar.countit(it=='=')==0:
        toadd.add(pos)
  for pos in toadd:G[pos]='@'
echo "part 3: ",countit(G.values, it=='@')
printGrid(G,R,C)
