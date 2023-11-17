BASE = 4
fromage = 800.0
eau = 2
ail = 2
pain = 400

nbConvives = int(input("Entrez le nombre de personne(s) conviées à la fondue : "))

nouveauFromage = fromage * nbConvives / BASE
nouvelleEau = eau * nbConvives / BASE
nouvelAil = ail * nbConvives / BASE
nouveauPain = pain * nbConvives / BASE

print(f"Pour faire une fondue fribourgeoise pour {nbConvives} personne(s), il vous faut :")
print(f"- {nouveauFromage} gr de fromage")
print(f"- {nouvelleEau} dl d'eau")
print(f"- {nouvelAil} gousse(s) d'ail")
print(f"- {nouveauPain} gr de pain")
