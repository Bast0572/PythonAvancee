def recherche_naive(liste, param):
    for i in range(len(liste)-1):
        if liste[i] == param:
            return print(i)

    return print('-1')
