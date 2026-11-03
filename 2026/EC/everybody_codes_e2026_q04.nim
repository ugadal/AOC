import std/os
import sequtils
import strutils
import math
import algorithm
import regex

let nfs = currentSourcePath.extractFilename.splitFile.name
echo nfs

let da1 = nfs & "_p1.txt"
echo da1
let d = """id=1 quest=1 part=1 time=187
id=3 quest=1 part=1 time=413
id=5 quest=1 part=3 time=744
id=2 quest=1 part=3 time=745
id=4 quest=1 part=2 time=558
id=1 quest=1 part=2 time=299
id=1 quest=1 part=3 time=362
id=4 quest=1 part=3 time=1268
id=4 quest=1 part=1 time=457
id=5 quest=1 part=1 time=257
id=2 quest=1 part=1 time=192
id=3 quest=1 part=3 time=1168
id=5 quest=1 part=2 time=346
id=3 quest=1 part=2 time=455
id=2 quest=1 part=2 time=562"""
var m = RegexMatch2()
for l in d.splitlines:
  echo l
  #~ for m in findAll(l, re2"=(\d+)"):
    #~ echo l[m.group(0)]
  echo findAll(l,re2"=(\d+)").mapit(l[it.group(0)].parseint)
  echo findAll(l,re2"(\d+)").mapit(l[it.group(0)].parseint)
  echo findAll(l, re2"\d+").mapIt(l[it.boundaries].parseInt)
  #~ echo l.findAllSubstr(re2"\d+").mapIt(it.parseInt)
  echo l.split(" ").mapit(it.split("=")[1].parseint)
  echo l.findAllBounds(re2"\d+").mapIt(l[it].parseInt)
