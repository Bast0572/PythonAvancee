def recherche_sous_chaines(chaine,sous_chaine):
    point=0
    occurence=0
    rightchain= False
    realrightchain=False
    for item in chaine:
        if item==sous_chaine[0]:
            
            for i in range(len(sous_chaine)-1):
                if sous_chaine[i]==chaine[occurence+i]:
                    rightchain=True
                else:
                    rightchain=False
                    break
        if(rightchain==True and realrightchain==False):
            realrightchain=True
            point = occurence


        occurence=occurence+1
    if(realrightchain==True):
        return print(point)
    else:
        return print('-1')
    
recherche_sous_chaines("Bonjour tout le monde","jour")

