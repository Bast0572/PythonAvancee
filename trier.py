# fonction qui prend en paramèter une liste
def est_triee(liste):

    # la variable 'valeur' prend la valeur du premier élément de la liste 
    valeur =liste[0]
    # on boucle sur chac élément de la liste
    for item in liste:

        # si la valeur de l'item est supérieur ou égale à la valeur de 'valeur', 'valeur' prend la valeur de l'item et on continue
        if (item>=valeur):
            valeur=item
        # si la valeur d'item est inférieur à la valeur de 'valeur' on s'arrète la liste n'est pas triée par ordre croissant 
        else:
           # on affiche False
           return print(False)
    # on affiche True        
    return print(True)

# on apelle la méthode en passant en paramètre une liste de nombre
est_triee([1,2,3,3,4,6])