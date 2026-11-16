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
var dp1 = rp(nfs, 1)
var dp2 = rp(nfs, 2)
var dp3 = rp(nfs, 3)

echo dex1
echo dp1
dump(dp2)
