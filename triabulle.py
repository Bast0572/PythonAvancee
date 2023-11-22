def triabulle(liste):

    valeur1=0
    valeur2=0
    for j in range(len(liste)):
        for i in range( len(liste)-1):
            value1=liste[i]
            value2=liste[i+1]
            if (value1>value2):
                liste[i]=value2
                liste[i+1]=value1
    return print(liste)

triabulle([9,4,6,2,8,1,7,3,5])