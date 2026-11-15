import std/os
import sequtils
import strutils
import math
#~ import algorithm
#~ import regex
import tables
import sugar
#~ import strscans
import sets
#~ import complex
import hashes
import strmisc
let nfs = currentSourcePath.extractFilename.splitFile.name
import utils
#~ import deques
var dex1 = rex(nfs, 1)
type
  coord = tuple [row: int, col: int]
  map = Table[coord, int]

proc getmap(da: string): map =
  for r, row in da.splitlines.toseq:
    for col, c in row:
      if c != '.':
        result[(r, col)] = parseInt($c)


proc `+=`(a: var coord, b: coord) =
  a.row += b.row
  a.col += b.col

proc shade(m: map, d: coord): map =
  for pos in m.keys:
    result[pos] = 0
  for pos, v in m:
    if v > 1:
      var s = v
      var lp = pos
      while s > 1:
        lp += d
        if lp notin m: break
        s -= 1
        result[lp] = max(result[lp], s)


proc printmap(m: map) =
  var mr = m.keys.toseq.mapit(it.row).max
  var mc = m.keys.toseq.mapit(it.col).max
  #~ var pos:coord
  for row in 0 .. mr:
    for col in 0 .. mc:
      let pos: coord = (row, col)
      if pos in m:
        if m[pos] == -2:
          stdout.write 'a'
        elif m[pos] == -1:
          stdout.write 'b'
        elif m[pos] == 0:
          stdout.write 'c'
        else:
          stdout.write m[pos]
      else:
        stdout.write '.'
    echo ""
  echo "==================="
proc printunshaded(m: map, dir: coord) =
  var mr = m.keys.toseq.mapit(it.row).max
  var mc = m.keys.toseq.mapit(it.col).max
  var shade: map = m.shade(dir)

  #~ var pos:coord
  for row in 0 .. mr:
    for col in 0 .. mc:
      let pos: coord = (row, col)
      if pos in m and m[pos] > shade[pos]:
        stdout.write m[pos]
      else:
        stdout.write '.'
    echo ""
  echo "======================"

proc growing(m: map, dir: coord): map =
  let sh = m.shade(dir)
  for pos, v in m:
    if v > sh[pos]:
      result[pos] = v

proc countgrowing(m: map, dir: coord): int =
  m.growing(dir).len

var M = getmap(dex1)
echo "ex1: ", M.countgrowing((1, 1))
var dp1 = rp(nfs, 1)
var dp2 = rp(nfs, 2)
var dp3 = rp(nfs, 3)
M = getmap(dp1)
echo "p1: ", M.countgrowing((1, 1))
const DD: array[6, coord] = [(1, 1), (1, -1), (0, -2), (-1, -1), (-1, 1), (0, 2)]
M = getmap(dex1)
echo "ex1p2: ", DD.mapit(M.countgrowing(it)).sum
M = getmap(dp2)
echo "p2: ", DD.mapit(M.countgrowing(it)).sum
iterator dd(): coord {.closure.} =
  while true:
    for dir in DD:
      yield dir

proc newshade(m: map, d: coord): tuple[nm: map, sold, ene: int] =
  result.nm = m
  let g = m.growing(d)
  result.ene = g.len
  for v in result.nm.mvalues:
    if v <= 0:
      v += 1
  for pos, v in g:
    if v == 9:
      result.sold += 1
      result.nm[pos] = -2
    else:
      result.nm[pos] += 1

M = getmap(dex1)
var z = dd
var (nm, warriors, energy) = M.newshade(z())

var sol, ene: int
while warriors < 100000:
  (nm, sol, ene) = nm.newshade(z())
  warriors+=sol
  energy+=ene
echo "ex1p3: warriors: ", warriors, " energy: ", energy
M = getmap(dp3)
z = dd
(nm, warriors, energy) = M.newshade(z())

while warriors < 100000:
  (nm, sol, ene) = nm.newshade(z())
  warriors+=sol
  energy+=ene
echo "p3: warriors: ", warriors, " energy: ", energy
