#Escribe un programa que lea las edades de 10
#alumnos y devuelva la edad del mayor, la edad
#del menor, la edad media y la diferencia de edades entre
#el mayor y el menor

def edad_media():
    
    print"Introduzca la edad del alumno 1"
    Alumno = input()
    edadMayor=Alumno
    edadMenor=Alumno
    sumaEdades=Alumno
    
    for cont in range(2, 11):
        print"Introduzca la edad del alumno",cont
        Alumno = input()
        sumaEdades=sumaEdades+Alumno
        if Alumno > edadMayor:
            edadMayor=Alumno
        if Alumno < edadMenor:
            edadMenor=Alumno

    diferencia=edadMayor-edadMenor
    edadMedia=sumaEdades/(cont-1)

    print "El número de alumnos es",cont
    print"La edad mayor es ", edadMayor
    print"La edad menor es ", edadMenor
    print"La diferencia entre la edad mayor y la edad menor es ",diferencia
    print"La suma de las edades es ", sumaEdades
    print"La edad media es", edadMedia

edad_media()
        
