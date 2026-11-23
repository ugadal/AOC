import std/[enumerate, math, os, sequtils, sets, strutils, tables]
import utils
import sugar
import memo
import algorithm
type
  link = tuple [o, d: int]
  Net = seq[link]
  Pool = set[int8]
  pairs = (int,int)
  Adj = seq[seq[int]]

