#  mini projet retourner le deuxième plus grand nombre


# fonction qui prend en paramètre une liste de nombre
def plus_grand_deuxieme_nombre(liste):
    
    # on vérifie si la liste contient moins de 2 éléments ou non
    if (len(liste)<2):

        # on retourne et on affiche None
        return print(None)
    
    # on initialise deux variables à 0 pour stocker les valeurs du plus grand nombre et du second plus grand nombre
    valeur_plus_grand =0
    valeur_plus_grand2=0
   
    # on parcourt la liste
    for item in liste:

        # si item est plus grand que que valeur_plus_grand, valeur_plus_grand2 prend la valeur de valeur_plus_grand et valeur_plus_grand prend la valeur d'item 
        if (item>valeur_plus_grand):
            valeur_plus_grand2=valeur_plus_grand
            valeur_plus_grand=item
    # on retourne le deuxième plus grand nombre
    return print(valeur_plus_grand2)
# on appelle la méthode avec en paramètre une liste de nombre
plus_grand_deuxieme_nombre([1,2,3,4,9,10,54])
        