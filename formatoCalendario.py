def formatoCalendario():
    dia=input("Inserte el dia ")
    while dia<1 or dia>31:
        print"El numero debe ser entre 1 y 31"
        dia=input("Inserte el dia ")


    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    numero=input("Inserte el numero del mes ")
    while numero>12 or numero<1:
        print"El numero debe ser entre 1 y 12"
        numero=input("Inserte el numero del mes ")
    mes=meses[numero-1]

    ano=input("Inserte el ano ")

    print "La fecha es el ", dia, "de ",mes, "de ", ano
    input ("press enter to exit")

formatoCalendario()
