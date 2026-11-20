# utils.nim
import std/[os, strutils]

let nfs* = getAppFilename().extractFilename.splitFile.name

proc rp*(nfs: string, p: int): string =
  let chemin=nfs & "_p" & $p & ".txt"
  if fileExists(chemin):
    readFile(chemin).strip
  else:
    ""

proc rex*(nfs: string, p: int): string =
  readFile(nfs & "_ex.txt").strip.split("\n\n")[p-1]
proc rps*(nfs: string, p: int,sub:int): string =
  readFile(nfs & "_p" & $p & ".txt").strip.split("\n\n")[sub-1]
