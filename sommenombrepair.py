def somme_nombres_pair(list):
    somme=0
    for item in list:
        if ((item%2)==0):
            somme=somme+item
    return print(somme)

somme_nombres_pair([3,7,11])