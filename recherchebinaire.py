def recherche_binaire(liste, param):
    debut = 0
    fin = len(liste)-1

    while debut <= fin:
      milieu = (debut+fin)//2
      if liste[milieu] == param:
            return print(milieu)
      else:
           if liste[milieu] > param:
                fin = fin-1
           else:
                debut = debut+1

    return print('-1')

recherche_binaire([1,2,3,4,5,7,8,9],5)

