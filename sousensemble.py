# mini projet - sortir les sous ensembles d'une liste avec une somme égale à 'k'

def ensemble(liste,k):
    sousensemble=[]
    sousensembles=[]
    for item in liste:
        sousensemble.append(item)
        if (sum(sousensemble)==k):
            sousensembles.append(sousensemble)  
        if (sum(sousensemble)>k):
            sousensemble=[]
# 