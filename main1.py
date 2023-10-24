# mini projet - plus grand nombre pair -python

# liste contenant des nombres 
liste=[8,1,10,3,7,24,35]

# méthode retournant le plus grand nombre pair de la liste passer en paramètre
def plus_grand_nombre_pair(liste):
   
    # 'nombre' variable dans laquel on stocke la valeur du nombre pair le plus grand, on initialise la variable à zéro
    nombre=0

    # on boucle sur la liste
    for item in liste:
        
        # on vérifie si le nombre est pair
        if(item%2==0 ):
            # on vérifie si item est supérieur au nombre
            if(item>nombre):
                nombre=item
    
    # on affiche le nombre final ou 'none' si il n'y a pas de nombre pair
    if (nombre ==0):
        return print(None)
    else:
        return print(nombre)

# on appelle la méthode en passant en paramètre la liste de nombre
plus_grand_nombre_pair(liste)