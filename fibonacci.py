def fibonnaci(nombre):
    if nombre<2:
        return print(range(nombre))
    suite=['0','1']
    for i in range(nombre-2):
        num =int(suite[i])+int(suite[i+1])
        suite.append(str(num))
    return print(' '.join(suite))

fibonnaci(45)