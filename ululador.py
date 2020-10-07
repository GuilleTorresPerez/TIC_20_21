#Haz un programa que lea una cadena y sustituya las vocales
#por la letra u. palabra de 10

def ululador():
    a = 'a'
    e = 'e'
    i = 'i'
    o = 'o'
    u = 'u'
    palabra=raw_input("Introduce la palabra ")
    longitudPalabra =(len(palabra)) 
    print "La longitud de la palabra es ",longitudPalabra

    for cont in range(0,longitudPalabra):
        if (palabra[cont] == a or palabra[cont] == e or palabra[cont] == i or palabra[cont] == o):
            print 'u'
        else:
            print palabra[cont]


ululador()
        
