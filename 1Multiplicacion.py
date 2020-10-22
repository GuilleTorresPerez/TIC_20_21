def multiplicacion():
    PrimerNumero=input("Inserte un numero ")
    SegundoNumero=input("Inserte otro numero ")
    TercerNumero=input("Inserte otro numero ")
    CuartoNumero=input("Inserte otro numero ")

    while PrimerNumero==0 or SegundoNumero==0 or TercerNumero==0 or CuartoNumero==0:
        print"Inserte un numero que no sea 0"
        PrimerNumero=input("Inserte un numero ")
        SegundoNumero=input("Inserte otro numero ")
        TercerNumero=input("Inserte otro numero ")
        CuartoNumero=input("Inserte otro numero ")

    resultado=PrimerNumero*SegundoNumero*TercerNumero*CuartoNumero
    print "El resultado es ", resultado

    input("Press key to escape")

multiplicacion()
