def PGCD(nombre1,nombre2):
    r = nombre1%nombre2
    
    if (r==0):
        return print(nombre2)
    #PGCD(nombre2,r)
    while(r!=0):
        nombre1=r
        r=nombre2%r
        nombre2=nombre1
    return print(nombre2)

PGCD(25,20)   
    