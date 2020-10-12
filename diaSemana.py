def diaSemana():
    diasSemana = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
    numero=input("Inserte un numero ")

    while numero>7 or numero<1:
        print"Inserte un numero entre 1 y 7"
        numero=input("Inserte un numero ")

    dia=diasSemana[numero-1]
    print "El dia de la semana correspondiente es ", dia
    input ("press enter to exit")

diaSemana()
