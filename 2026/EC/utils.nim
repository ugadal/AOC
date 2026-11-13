# utils.nim
import std/[os, strutils]

let nfs* = getAppFilename().extractFilename.splitFile.name

proc rp*(nfs: string, p: int): string =
  readFile(nfs & "_p" & $p & ".txt").strip

proc rex*(nfs: string, p: int): string =
  readFile(nfs & "_ex.txt").strip.split("\n\n")[p-1]
