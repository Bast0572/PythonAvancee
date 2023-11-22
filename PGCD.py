def PGCD(nombre1,nombre2):
    r = nombre1%nombre2
    
    if (r==0):
        return print(nombre2)
    PGCD(nombre2,r)

PGCD(60,100)   
    