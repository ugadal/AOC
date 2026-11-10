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
var G=initTable[Complex64,char]()
#~ var al=ex1.splitlines
#~ var al=toseq(open(da1).lines)
var al=toseq(open(da2).lines)
let R = al.len       # Nombre total de lignes
let C = al[0].len     # Longueur de la première ligne (largeur)
let sr=(R-1)/2
let sc=(C-1)/2
for row,line in al:
  #~ dump((row,line))
  for c,s in line:
    let pos=complex(c.float,row.float)
    #~ if s=='1':G[pos]='#'
    #~ else:G[pos]="."
    G[pos]=s
#~ dump((R,C))
#~ dump((sr,sc))
let sp=complex(sc,sr)
G[sp]='#'
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
