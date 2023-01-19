
#On ajoute d'abord les bibliothèques requises

import numpy as numpy

from numpy.random import default_rng


graine = 0
tirage = []
liste = []
#liste_nombre =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45]

choix = input("Utiliser une seed aléatoire? o/n")

if  choix == 'o' :
    print("Utilisation d'une seed aléatoire pour le tirage")
    numpy.random.seed(seed=None)
elif choix == 'n' :
    seed = input("Entrer la seed :")
    print("La seed sélectionnée est :", seed)
    numpy.random.seed(seed=graine)

nbtirage = int(input("Entrer le nombre de tirage :"))
#on remplit un tableau de nbtirage lignes
for i in range(0, nbtirage) :
    liste = numpy.random.choice(range(1, 46), size=5, replace=False)
    if len(tirage) == 0 :
        tirage.append(list(liste))
    else :
        tirage = numpy.vstack([tirage,list(liste)])
print(tirage)