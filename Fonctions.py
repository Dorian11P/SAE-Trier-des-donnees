import numpy as numpy

import matplotlib.pyplot as plt
from matplotlib import colors
from matplotlib.ticker import PercentFormatter
def histo(index_nb,nb_occurence):
    fig, ax = plt.subplots()

    nombres_index = index_nb
    counts = nb_occurence

    ax.bar(nombres_index, counts)

    ax.set_ylabel("Nombre d'occurences")
    ax.set_xlabel("Nombres")
    ax.set_title('Occurences de chaques nombres de 1 à 45')
    ax.legend(title='Occurence des nombres dans le tirage')

    plt.show()

def tri_cocktail(tab):
    echange=True
    debut=0
    fin=len(tab)-2
    while echange:
        echange=False
        for i in range(0,len(tab)-1):
            if tab[i]>tab[i+1]:
                tab[i],tab[i+1]=tab[i+1],tab[i]
                echange=True
        for i in range(len(tab)-2,-1,-1):
            if tab[i]>tab[i+1]:
                tab[i],tab[i+1]=tab[i+1],tab[i]
                echange=True
#do
# Programme Python pour l'implémentation du tri par insertion
def tri_insertion(tab):
    # Parcour de 1 à la taille du tab
    for i in range(1, len(tab)):
        k = tab[i]
        j = i-1
        while j >= 0 and k < tab[j] :
                tab[j + 1] = tab[j]
                j -= 1
        tab[j + 1] = k


# Programme principale pour tester le code ci-dessus


