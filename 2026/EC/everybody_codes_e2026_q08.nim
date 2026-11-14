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
var da=rex(nfs,1)
echo da
type coord = tuple [row:int,col:int]
var map : Table[coord,int]
var pos : coord
var v:int
for r,row in da.splitlines.toseq:
  for col,s in row:
    pos=(r,col)
    if s=='.':v=0
    else:v=parseInt($s)
    echo pos," ",v
