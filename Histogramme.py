
#On ajoute d'abord les bibliothèques requises

import numpy as numpy
from Fonctions import *
import matplotlib.pyplot as plt
from matplotlib import colors
from matplotlib.ticker import PercentFormatter

graine = 0
tirage = []
liste = []
nb_occurences = []
nce = []
index_nb = []
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
comptage = numpy.array(tirage)
for i in range(1, 46):
    index_nb.append(i)
    count = numpy.count_nonzero(comptage == i)
    nb_occurence.append(count)
    print(i,"=", count, "fois")

histo(index_nb, nb_occurence)


print(count)

