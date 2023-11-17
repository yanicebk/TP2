import random

resultat_lancer = random.randint(0, 100)

if resultat_lancer < 50:
    resultat = "Pile !"
else:
    resultat = "Face !"

print(resultat)
