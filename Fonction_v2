import numpy as numpy
import re
# save numpy array as npy file
from numpy import asarray
from numpy import save
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

#recherche itérative
def recherche_dichotomique( element, liste_triee ):
    a = 0
    b = len(liste_triee)-1
    m = (a+b)//2
    while a < b :
        if liste_triee[m] == element :
            return m
        elif liste_triee[m] > element :
            b = m-1
        else :
            a = m+1
        m = (a+b)//2
    return a

#recherche récursive
def recherche_dichotomique_recursive( element, liste_triee, a = 0, b = -1 ):
    if a == b :
        return a
    if b == -1 :
        b = len(liste_triee)-1
    m = (a+b)//2
    if liste_triee[m] == element :
        return m
    elif liste_triee[m] > element :
        return recherche_dichotomique_recursive(element, liste_triee, a, m-1)
    else :
        return recherche_dichotomique_recursive(element, liste_triee, m+1, b)
# Programme principale pour tester le code ci-dessus



#pour la sauvegarde/chargment
def save_binary(data):
    print("sauvegarde en cours")
    numpy.save('binary_file.npy', data)

def save_csv(data):
    numpy.savetxt('csv_file.csv', data, fmt='%d', delimiter=",")

def save_txt(data):
    file = open("txt_file.txt", "w+")

    for i in data:
    # Saving the 2D array in a text file
        content = str(i).replace("[", '').replace("]", '')
        file.write(content + "\n")
    file.close()
