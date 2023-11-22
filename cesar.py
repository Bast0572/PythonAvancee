def cesar(chaine,valeur):
    char=''
    chaine2=""
    for item in chaine:
        if item==' ':
            chaine2=chaine2+item
        else:
            chaine2=chaine2+(chr(ord(item)+valeur))
    return print(chaine2)

cesar("Bonjour le monde",3)


def cesarInverse(chaine, valeur):
    char = ''
    chaine2 = ""
    for item in chaine:
        if item == ' ':
            chaine2 = chaine2+item
        else:
            chaine2 = chaine2+(chr(ord(item)-valeur))
    return print(chaine2)

cesarInverse("Erqmrxu oh prqgh", 3)