import std/[strutils, algorithm]

#~ let d = "4<3 2<5 3>1 1>2 1<5 4<1 3>2 4<2 3>5 4<5"
##
### 1. On extrait la liste de tous les caractères uniques présents (ex: ['1', '2', '3', '4', '5'])
##var elements: seq[char] = @['1', '2', '3', '4', '5']
##
### 2. On trie notre liste avec une fonction de comparaison personnalisée
##elements.sort(proc (x, y: char): int =
##  # Si dans la chaîne 'd' on trouve que x est plus petit que y (ex: "x<y" ou "y>x")
##  if ($x & "<" & $y) in d or ($y & ">" & $x) in d:
##    return -1 # x doit être avant y
##  elif ($y & "<" & $x) in d or ($x & ">" & $y) in d:
##    return 1  # y doit être avant x
##  else:
##    return 0
##)
##
##echo elements # Affichera l'ordre exact directement !

proc comparerRegles(x, y: char, regles: string): int =
  if ($x & "<" & $y) in regles or ($y & ">" & $x) in regles:
    return -1
  elif ($y & "<" & $x) in regles or ($x & ">" & $y) in regles:
    return 1
  else:
    return 0
let d = "4<3 2<5 3>1 1>2 1<5 4<1 3>2 4<2 3>5 4<5"
var elements = @['1', '2', '3', '4', '5']

# 2. On utilise une fonction anonyme/sucre syntaxique pour injecter la ligne actuelle 'd'
elements.sort(proc (x, y: char): int = comparerRegles(x, y, d))

echo elements
