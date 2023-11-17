import random


def lancer_piece_truquee():
    if random.random() < 2/3:
        return "Pile !"
    else:
        return "Face !"

nombre_total_lancers = 1000

resultats = [lancer_piece_truquee() for _ in range(nombre_total_lancers)]

nombre_pile = resultats.count("Pile !")

print(f"Nombre de lancers de Pile : {nombre_pile} sur {nombre_total_lancers} (en moyenne 2 sur 3)")
