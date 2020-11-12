def cantidad():
    numero=input("Inserte un numero de 4 cifras")
    suma=0
    cont=3

    for cont in range (3,0):
        divisor=10^cont
        cociente=numero/divisor
        print cociente
        suma=suma+cociente
        numero=numero%divisor
    

cantidad()
    
