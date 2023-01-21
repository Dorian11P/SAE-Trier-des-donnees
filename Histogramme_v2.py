
#On ajoute d'abord les bibliothèques requises

import numpy as numpy
from Fonctions import *
import matplotlib.pyplot as plt
from matplotlib import colors
from matplotlib.ticker import PercentFormatter

graine = 0
tirage = []
liste = []
nb_occurence = []
nce = []
index_nb = []


choix = input("Charger un fichier ou générer un nouveau tirage? fichier/tirage")

if  choix == 'fichier' :

    nom_fich = input("Entrer le nom du fichier csv/npy/txt (même dossier que programme) :")
    if nom_fich.endswith('.npy'):
        print("fichier NPY détecté")
        tirage = numpy.load(nom_fich)
    elif nom_fich.endswith('.csv'):
        print("fichier CSV détecté")
        tirage = numpy.genfromtxt(nom_fich, delimiter=',')
    elif nom_fich.endswith('.txt'):
        print("fichier TXT détecté")
        file = open(nom_fich, "r")
        File_data = numpy.loadtxt(nom_fich, dtype=int)
        tirage = File_data
        print(File_data)
    print(tirage)
    num_rows, num_cols = tirage.shape
    nbtirage = num_rows
    comptage =numpy.array(tirage)
    print(nbtirage)
elif choix == 'tirage' :
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


choix = choix = input("Sauvegarder en: binaire/csv/txt")
if  choix == 'binaire' :
    save_binary(tirage)
elif choix == 'csv' :
    save_csv(tirage)
elif choix == 'txt':
    save_txt(tirage)




