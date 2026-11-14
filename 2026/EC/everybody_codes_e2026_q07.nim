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
    #~ dump(lpp)
  return lpp
proc bfs(pp:problem,recid:int,power:int):problem=
  var lpp=pp
  var justexploded,exploded : seq[int] = @[]
  var stack,newstack = initDeque[tuple[id:int,en:int]]()
  stack.addLast((recid,power))
  while stack.len>0:
    newstack.clear
    #~ dump(stack)
    for t in stack:
      lpp[t.id].energy+=t.en
      #~ dump((t.id,lpp[t.id]))
      if t.en==1:continue
      for c in lpp[t.id].conn:
        newstack.addLast((c,t.en-1))
    justexploded = @[]
    for k,v in lpp:
      if v.energy>=1000000:
        justexploded.add(k)
    for k in justexploded:
      for c in lpp[k].conn:
        newstack.addLast((c,10))
      exploded.add(k)
      lpp.del(k)    
    stack=newstack.filterit(it.id notin exploded).todeque
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
rules=getrules(rp(nfs,3))
var tr=0;
for k in rules.keys:
  let v=rules.bfs(k,10).getE
  if v>tr:
    tr=v
    echo k," ",v
echo "p3: ",tr
