# mini - projet faire une fonction qui renvoie la médiane d'une liste



# fonction qui prend en paramètre un liste
def mediane(liste):

    # trie la liste en ordre croissant
    liste=sorted(liste)

    # on verifie si la liste contient un nombre pair d'éléments 
    if (len(liste)%2!=0):
        # on renvoie l'élément de la liste se trouvant au milieu de la liste
        return print(liste[int(len(liste)/2)])
    else:
        # on renvoie la moyenne des éléments des deux valeurs du milieu de la liste
        return print((liste[int(len(liste)/2)]+liste[int(len(liste)/2)-1])/2)
    

# on appelle la fonction avec en paramètre une liste de nombre
mediane([1,5,8,10,6])
mediane([1,5,8,6,7,10])