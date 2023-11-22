def frequence_caracteres(chaine):
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ']
    for item1 in alphabet:
        somme=0
        for item2 in chaine:
           if (item1==item2):
              somme= somme+1
        print(item1+" : "+str(somme))  

frequence_caracteres("ceci est unne phrase")