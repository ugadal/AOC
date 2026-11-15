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
var dex1=rex(nfs,1)
type coord = tuple [row:int,col:int]
type map = Table[coord, int]

proc getmap(da:string):map=
  var v:int
  var pos:coord
  for r,row in da.splitlines.toseq:
    for col,s in row:
      pos=(r,col)
      if s=='.':continue
      else:v=parseInt($s)
      result[pos]=v
      
proc mv(a:coord,b:coord):coord=
  result.row=a.row+b.row
  result.col=a.col+b.col
proc shade(m:map,d:coord):map=
  #~ var lm=m
  var s:int
  var lp:coord
  for pos,v in m:
    result[pos]=0
  for pos,v in m:
    if v>1:
      s=v
      lp=pos
      while s>1:
        lp=lp.mv(d)
        if lp notin m:break
        s-=1
        result[lp]=max(result[lp],s)
proc printmap(m:map) =
  var mr=m.keys.toseq.mapit(it.row).max
  var mc=m.keys.toseq.mapit(it.col).max
  #~ dump((mr,mc))
  var pos:coord
  for row in 0 .. mr:
    for col in 0 .. mc:
      let pos: coord = (row, col)
      if pos in m:
        if m[pos]== -2:
          stdout.write 'a'
        elif m[pos]== -1:
          stdout.write 'b'
        elif m[pos]== 0:
          stdout.write 'c'
        else:
          stdout.write m[pos]
      else:
        stdout.write '.'
    echo ""
  echo "==================="
proc printunshaded(m:map,dir:coord) =
  var mr=m.keys.toseq.mapit(it.row).max
  var mc=m.keys.toseq.mapit(it.col).max
  #~ dump((mr,mc))
  var shade : map = m.shade(dir)
  
  var pos:coord
  for row in 0 .. mr:
    for col in 0 .. mc:
      let pos: coord = (row, col)
      if pos in m and m[pos]>shade[pos]:
        stdout.write m[pos]
      else:
        stdout.write '.'
    echo ""
  echo "======================"
proc growing(m:map,dir:coord):map =
  var shade : map = m.shade(dir)
  var P=m.keys.toseq
  for p in P:
    if m[p]>shade[p]:
      result[p]=m[p]
proc countgrowing(m:map,dir:coord):int =
  return m.growing(dir).len

var M=getmap(dex1)
echo "ex1: ",M.countgrowing((1,1))
var dp1=rp(nfs,1)
var dp2=rp(nfs,2)
var dp3=rp(nfs,3)
M=getmap(dp1)
echo "p1: ",M.countgrowing((1,1))
var DD : seq[coord]
DD.add((1,1))
DD.add((1,-1))
DD.add((0,-2))
DD.add((-1,-1))
DD.add((-1,1))
DD.add((0,2))
M=getmap(dex1)
echo "ex1p2: ",DD.mapit(M.countgrowing(it)).sum
M=getmap(dp2)
echo "p2: ",DD.mapit(M.countgrowing(it)).sum
iterator dd():coord {.closure.} =
  while true:
    for dir in DD:
      yield dir
proc newshade(m:map,d:coord) : tuple[nm:map,sold:int,ene:int] =
  var lm=m
  var G = m.growing(d)
  result.ene=G.len
  result.sold=G.values.toseq.filterit(it==9).len
  for pos,v in lm:
    if v<=0:
      lm[pos]+=1
  for pos,v in G:
    if v==9:
      lm[pos]= -2
    else:
      lm[pos] += 1
  
  result.nm = lm
M=getmap(dex1)
var z=dd
var (nm, warriors, energy) = M.newshade(z())
echo "warriors: ",warriors," energy: ",energy
nm.printmap

var sol, ene: int
while warriors<100000:
  (nm, sol, ene) = nm.newshade(z())
  warriors+=sol
  energy+=ene
  echo "warriors: ",sol," energy: ",ene
  #~ nm.printmap
echo "warriors: ",warriors," energy: ",energy
M=getmap(dp3)
z=dd
(nm, warriors, energy) = M.newshade(z())
echo "warriors: ",warriors," energy: ",energy
nm.printmap

#~ var sol, ene: int
while warriors<100000:
  (nm, sol, ene) = nm.newshade(z())
  warriors+=sol
  energy+=ene
  echo "warriors: ",sol," energy: ",ene
  nm.printmap
echo "warriors: ",warriors," energy: ",energy
