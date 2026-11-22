import sequtils

type
  Match = (int, int)
  Journee = seq[Match]

# Itérateur closure permettant la récursion
iterator toutesLesJournees(equipes: seq[int]): Journee {.closure.} =
  if equipes.len == 0:
    yield @[]
  else:
    let premier = equipes[0]
    let reste = equipes[1 .. ^1]
    
    for i, adversaire in reste:
      let match: Match = (premier, adversaire)
      var restantes = reste
      restantes.delete(i)
      
      for sousJournee in toutesLesJournees(restantes):
        yield @[match] & sousJournee

# Exemple d'utilisation pour 8 équipes (0 à 7)
let equipes = toSeq(0 .. 7)
var compteur = 0

for journee in toutesLesJournees(equipes):
  inc compteur
  #~ if compteur <= 5:
  echo "Journée #", compteur, " : ", journee

echo "Nombre total de journées distinctes : ", compteur # Affiche 105
