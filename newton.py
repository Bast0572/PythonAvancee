def newton(nombre):
    value=0
    while ((value*value)<nombre):
        value=value+1

    carre1= value
    carre2= value-1
    carre= (carre1+carre1)/2
    val=carre*2
    while((val-carre)>(1*10**-6)):
        val=carre
        carre=(carre+2/carre)/2
    
    return print(carre)


newton(2)