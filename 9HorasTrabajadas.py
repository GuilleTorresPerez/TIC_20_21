
#Escribir una función eque devuelva el salario semanal
#de un trabajador en base a las horas trabajadas
#y el pago por hora trabajada. Las horas ordinarias (40 primeras horas
#de trabajo) a 30 euros/hora y las horas siguientes a 1.5 veces el precio
#de la hora ordinaria

def ejercicio9():
    horasTotales=input("Cuantas horas extras: ")
    precioNormal=30
    precioExtra=1.5*precioNormal
    if horasTotales<=40:
        salario=horasTotales*precioNormal
    else:
        salario=40*precioNormal+(horasTotales-40)*precioExtra
    print "El salario es ", salario

ejercicio9()
