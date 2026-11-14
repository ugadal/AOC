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
import deques

type info = tuple [energy: int, conn:seq[int]]
type problem = Table[int,info]
proc getrules(da:string):problem=
  for line in da.splitlines:
    var values = line.split(", ").mapit(it.split("=")[1])
    let id=values[0].parseint
    let en=values[1].parseint
    let con=values[2].split(",").mapit(it.parseint)
    result[id]=(en,con)
proc getmaxcon(pp:problem):int=
  var rec,recid=0
  for k,v in pp:
    let tl=v.conn.len
    if tl>rec:
      rec=tl
      recid=k
  return recid
proc dfs(pp:problem,power:int):problem=
  var lpp=pp
  var stack : seq[tuple[id:int,en:int]]
  stack.add((lpp.getmaxcon,power))
  while stack.len>0:
    let t=stack.pop
    lpp[t.id].energy+=t.en
    if t.en==1:continue
    for c in lpp[t.id].conn:
      stack.add((c,t.en-1))
  return lpp
proc ndfs(pp:problem,recid:int,power:int):problem=
  var lpp=pp
  var stack : seq[tuple[id:int,en:int]]
  stack.add((recid,power))
  while stack.len>0:
    let t=stack.pop
    lpp[t.id].energy+=t.en
    if t.en==1:continue
    for c in lpp[t.id].conn:
      stack.add((c,t.en-1))
  return lpp

import std/[tables, sets]

proc nbfs(pp: problem, recid: int, power: int): problem =
  var lpp = pp
  var exploded = initHashSet[int]()
  var justexploded: seq[int] = @[]
  
  var stack, newstack: Table[int, CountTable[int]]
  stack[recid] = toCountTable([power])

  while stack.len > 0:
    newstack.clear()
    justexploded.setLen(0)

    for tid, counts in stack:
      if tid in exploded: continue
      
      var totalAdded = 0
      for p, qty in counts:
        totalAdded += p * qty
      lpp[tid].energy += totalAdded

      for p, qty in counts:
        if p > 1:
          for c in lpp[tid].conn:
            newstack.mgetOrPut(c, initCountTable[int]()).inc(p - 1, qty)

      if lpp[tid].energy >= 1000000:
        justexploded.add(tid)

    for k in justexploded:
      for c in lpp[k].conn:
        newstack.mgetOrPut(c, initCountTable[int]()).inc(10, 1)
      exploded.incl(k)
      lpp.del(k)

    swap(stack, newstack)

  return lpp

  
proc getE(pp:problem):int=
  result=pp.values.toseq.mapit(it.energy).sum
var rules:problem
rules=getrules(rex(nfs,1))
echo "ex1p1: ",dfs(rules,5).getE
echo "ex1p2: ",dfs(rules,10).getE
rules=getrules(rex(nfs,2))
echo "ex2p2: ",dfs(rules,10).getE
rules=getrules(rp(nfs,1))
echo "p1: ",dfs(rules,5).getE
rules=getrules(rp(nfs,2))
echo "p2: ",dfs(rules,10).getE
rules=getrules(rp(nfs,3))
var tr=0;
for k in rules.keys:
  let v=rules.nbfs(k,10).getE
  if v>tr:
    tr=v
    #~ echo k," ",v
echo "p3: ",tr
