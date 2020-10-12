def mes():
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    numero=input("Inserte un numero ")

    while numero>12 or numero<1:
        print"Inserte un numero entre 1 y 12"
        numero=input("Inserte un numero ")

    dia=meses[numero-1]
    print "El mes correspondiente es ", dia
    input ("press enter to exit")

mes()
