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

let da1 = nfs & "_p1.txt"
let da2 = nfs & "_p2.txt"
let ex1="""010100100100001101000
111101001000001110000
101111011000101010011
001000101010000100000
000110100110011001100
000001110111111000000
101100010101011110000
001101100000001010011
001001001111010001001
100011011110011010101
001100101110010010000"""

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

var al=ex1.splitlines
var (G, sp, R, C) = createGrid(al)

const directions = [
  complex(-1.0, -1.0), complex(0.0, -1.0), complex(1.0, -1.0),
  complex(-1.0,  0.0),                     complex(1.0,  0.0),
  complex(-1.0,  1.0), complex(0.0,  1.0), complex(1.0,  1.0) ]
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
      # On affiche le caractère s'il existe, sinon un espace vide
      stdout.write grid.getOrDefault(pos, ' ')
    echo "" # Retour à la ligne à la fin de chaque rangée
#~ printGrid(G,R,C)
for pos,s in G: 
  if s!='#':G[pos]='.'
#~ printGrid(G,R,C)  
iterator sandaround(pos: Complex64): char =
  for dir in directions:
    let voisinPos = pos + dir
    if voisinPos in G:
      yield G[voisinPos]
    else: yield '.'
    
while true:
  toadd= @[]
  for pos,s in G:
    if s == '#':
      if countIt(sandaround(pos), it in {'.'})>=1:toadd.add(pos)
      elif countIt(sandaround(pos), it in {'.', '='})>=5:
        toadd.add(pos)
  dump(toadd.len)
  if toadd.len>0:
    for pos in toadd:
      G[pos]='='
  else:break
  #~ printGrid(G,R,C)
echo "part 2: ",countit(G.values, it=='=')
