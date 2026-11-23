#~ import sequtils

#~ type
  #~ Match = (int, int)
  #~ Journee = seq[Match]

# Itérateur closure permettant la récursion
#~ iterator toutesLesJournees(equipes: seq[int]): Journee {.closure.} =
  #~ if equipes.len == 0:
    #~ yield @[]
  #~ else:
    #~ let premier = equipes[0]
    #~ let reste = equipes[1 .. ^1]
    
    #~ for i, adversaire in reste:
      #~ let match: Match = (premier, adversaire)
      #~ var restantes = reste
      #~ restantes.delete(i)
      
      #~ for sousJournee in toutesLesJournees(restantes):
        #~ yield @[match] & sousJournee

# Exemple d'utilisation pour 8 équipes (0 à 7)
#~ let equipes = toSeq(0 .. 7)
#~ var compteur = 0

#~ for journee in toutesLesJournees(equipes):
  #~ inc compteur
  #~ if compteur <= 5:
  #~ echo "Journée #", compteur, " : ", journee

#~ echo "Nombre total de journées distinctes : ", compteur # Affiche 105
import tables
type
  Match = (int, int)
  Journee = seq[Match]

var cache = initTable[set[int8], seq[Journee]]()
proc toutesLesJourneesCache(equipes: set[int8]): seq[Journee] =
  if equipes in cache:
    return cache[equipes]
  if equipes.len == 2:
    var paires: seq[int] = @[]
    for e in equipes: paires.add(int(e))
    return @[ @[ (paires[0], paires[1])]]
  var premier: int8 = -1
  for e in equipes:
    premier = e
    break
  var reste = equipes
  reste.excl(premier)
  for adversaire in reste:
    let match: Match = (int(premier), int(adversaire))
    var prochainReste = reste
    prochainReste.excl(adversaire)
    for sousJournee in toutesLesJourneesCache(prochainReste):
      result.add(@[match] & sousJournee)
  cache[equipes] = result

# Test avec 8 équipes (0 à 7)
let equipes: set[int8] = {0'i8, 1, 2, 3, 4, 5, 6, 7}
let journees = toutesLesJourneesCache(equipes)
echo journees
echo "Total généré : ", journees.len # 105
echo "Sous-problèmes mis en cache : ", cache.len # Seulement 51 entrées !

var X:set[uint8]
var t=25
for x in 1'u8..t.uint8:X.incl(x)
echo X
for x in X:echo x
import utils
echo X.first()

import std/algorithm

proc toAdj(n: Net, portals: int): seq[seq[int]] =
  result = newSeq[seq[int]](portals + 1)
  for l in n: result[l.o].add l.d
