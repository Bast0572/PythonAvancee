def recherche_binaire(liste,param):
    for i in range(len(liste)-1):
        if liste[i]==param:
            return print(i)
    
    return print('-1')

recherche_binaire([1,2,3,4,5,7,8,9],6)