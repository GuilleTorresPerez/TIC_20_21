#Escribe un programa que lea las edades de 10
#alumnos y devuelva la edad del mayor, la edad
#del menor, la edad media y la diferencia de edades entre
#el mayor y el menor

def edad_media():
    edadMayor=0
    edadMenor=0
    diferencia=0
    sumaEdades=0
    
    for cont in range(1, 11):
        print("Introduzca la edad del alumno "+cont)
        Alumno = input()
        sumaEdades=sumaEdades+Alumno

        if Alumno > edadMayor:
            edadMayor=Alumno
        if Alumno < edadMenor:
            edadMenor=Alumno

    print"La edad mayor es ", edadMayor
    print"La edad menor es ", edadMenor
    diferencia=edadMayor-edadMenor
    print"La suma de las edades es ", sumaEdades

edad_media()
        
        
        
        
