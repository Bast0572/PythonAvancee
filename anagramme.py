def anagramme(mot1,mot2):
    alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    
    for item in alphabet:
        lettre1=mot1.count(item)
        lettre2=mot2.count(item)
        if (lettre1!=lettre2):
            return print(False)
        
    return print(True)

anagramme('bonjour','bonjiur')